from functools import partial, total_ordering
from typing import Any, TYPE_CHECKING

import attrs

from naff.client.const import MISSING, T, Missing
from naff.client.utils.attr_converters import optional as optional_c
from naff.client.utils.serializer import dict_filter
from naff.models.discord.asset import Asset
from naff.models.discord.color import COLOR_TYPES, Color, process_color
from naff.models.discord.emoji import PartialEmoji
from naff.models.discord.enums import Permissions
from .base import DiscordObject

if TYPE_CHECKING:
    from naff.client import Client
    from naff.models.discord.guild import Guild
    from naff.models.discord.user import Member
    from naff.models.discord.snowflake import Snowflake_Type

__all__ = ("Role",)


def sentinel_converter(value: bool | T | None, sentinel: T = attrs.NOTHING) -> bool | T:
    if value is sentinel:
        return False
    elif value is None:
        return True
    return value


@attrs.define(eq=False, order=False, hash=False, kw_only=True)
@total_ordering
class Role(DiscordObject):
    _sentinel = object()

    name: str = attrs.field(repr=True)
    color: "Color" = attrs.field(repr=False, converter=Color)
    hoist: bool = attrs.field(repr=False, default=False)
    position: int = attrs.field(repr=True)
    permissions: "Permissions" = attrs.field(repr=False, converter=Permissions)
    managed: bool = attrs.field(repr=False, default=False)
    mentionable: bool = attrs.field(repr=False, default=True)
    premium_subscriber: bool = attrs.field(
        repr=False, default=_sentinel, converter=partial(sentinel_converter, sentinel=_sentinel)
    )
    _icon: Asset | None = attrs.field(repr=False, default=None)
    _unicode_emoji: PartialEmoji | None = attrs.field(
        repr=False, default=None, converter=optional_c(PartialEmoji.from_str)
    )
    _guild_id: "Snowflake_Type" = attrs.field(
        repr=False,
    )
    _bot_id: "Snowflake_Type | None" = attrs.field(repr=False, default=None)
    _integration_id: "Snowflake_Type | None" = attrs.field(repr=False, default=None)  # todo integration object?

    def __lt__(self: "Role", other: "Role") -> bool:
        if not isinstance(self, Role) or not isinstance(other, Role):
            return NotImplemented

        if self._guild_id != other._guild_id:
            raise RuntimeError("Unable to compare Roles from different guilds.")

        if self.id == self._guild_id:  # everyone role
            # everyone role is on the bottom, so check if the other role is, well, not it
            # because then it must be higher than it
            return other.id != self.id

        if self.position < other.position:
            return True

        if self.position == other.position:
            # if two roles have the same position, which can happen thanks to discord, then
            # we can thankfully use their ids to determine which one is lower
            return self.id < other.id

        return False

    @classmethod
    def _process_dict(cls, data: dict[str, Any], client: "Client") -> dict[str, Any]:
        data.update(data.pop("tags", {}))

        if icon_hash := data.get("icon"):
            data["icon"] = Asset.from_path_hash(client, f"role-icons/{data['id']}/{{}}", icon_hash)

        return data

    async def fetch_bot(self) -> "Member | None":
        """
        Fetch the bot associated with this role if any.

        Returns:
            Member object if any

        """
        if self._bot_id is None:
            return None
        return await self._client.cache.fetch_member(self._guild_id, self._bot_id)

    def get_bot(self) -> "Member | None":
        """
        Get the bot associated with this role if any.

        Returns:
            Member object if any

        """
        if self._bot_id is None:
            return None
        return self._client.cache.get_member(self._guild_id, self._bot_id)

    @property
    def guild(self) -> "Guild":
        """The guild object this role is from."""
        return self._client.cache.get_guild(self._guild_id)  # pyright: ignore [reportGeneralTypeIssues]

    @property
    def default(self) -> bool:
        """Is this the `@everyone` role."""
        return self.id == self._guild_id

    @property
    def bot_managed(self) -> bool:
        """Is this role owned/managed by a bot."""
        return self._bot_id is not None

    @property
    def mention(self) -> str:
        """Returns a string that would mention the role."""
        return f"<@&{self.id}>" if self.id != self._guild_id else "@everyone"

    @property
    def integration(self) -> bool:
        """Is this role owned/managed by an integration."""
        return self._integration_id is not None

    @property
    def members(self) -> list["Member"]:
        """List of members with this role"""
        return [member for member in self.guild.members if member.has_role(self)]

    @property
    def icon(self) -> Asset | PartialEmoji | None:
        """
        The icon of this role

        !!! note
            You have to use this method instead of the `_icon` attribute, because the first does account for unicode emojis
        """
        return self._icon or self._unicode_emoji

    @property
    def is_assignable(self) -> bool:
        """
        Can this role be assigned or removed by this bot?

        !!! note
            This does not account for permissions, only the role hierarchy

        """
        return (self.default or self.guild.me.top_role > self) and not self.managed

    async def delete(self, reason: str | Missing = MISSING) -> None:
        """
        Delete this role.

        Args:
            reason: An optional reason for this deletion

        """
        await self._client.http.delete_guild_role(self._guild_id, self.id, reason)

    async def edit(
        self,
        *,
        name: str | None = None,
        permissions: str | None = None,
        color: Color | COLOR_TYPES | None = None,
        hoist: bool | None = None,
        mentionable: bool | None = None,
    ) -> "Role":
        """
        Edit this role, all arguments are optional.

        Args:
            name: name of the role
            permissions: New permissions to use
            color: The color of the role
            hoist: whether the role should be displayed separately in the sidebar
            mentionable: whether the role should be mentionable

        Returns:
            Role with updated information

        """
        color = process_color(color)

        payload = dict_filter(
            {"name": name, "permissions": permissions, "color": color, "hoist": hoist, "mentionable": mentionable}
        )

        r_data = await self._client.http.modify_guild_role(self._guild_id, self.id, payload)
        r_data = dict(r_data)  # to convert typed dict to regular dict
        r_data["guild_id"] = self._guild_id
        return self.from_dict(r_data, self._client)

    async def move(self, position: int, reason: str | Missing = MISSING) -> "Role":
        """
        Move this role to a new position.

        Args:
            position: The new position of the role
            reason: An optional reason for this move

        Returns:
            The role object

        """
        await self._client.http.modify_guild_role_positions(
            self._guild_id, [{"id": self.id, "position": position}], reason
        )
        return self
