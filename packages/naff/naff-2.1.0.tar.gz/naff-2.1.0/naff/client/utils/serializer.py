from base64 import b64encode
from datetime import datetime, timezone
from io import IOBase
from pathlib import Path
from typing import Optional

from attr import fields, has

from naff.client.const import MISSING, T
from naff.models.discord.file import UPLOADABLE_TYPE, File

__all__ = ("no_export_meta", "export_converter", "to_dict", "dict_filter_none", "dict_filter", "to_image_data")

no_export_meta = {"no_export": True}


def export_converter(converter) -> dict:
    """Makes it easier to quickly type attr export converter metadata."""
    return {"export_converter": converter}


def to_dict(inst) -> dict:
    """
    Converts an instance to a dict.

    Args:
        inst: The instance to convert.

    Returns:
        The processed dict.

    """
    attrs = fields(inst.__class__)

    if (converter := getattr(inst, "as_dict", None)) is not None:
        d = converter()
        for a in attrs:
            if a.metadata.get("no_export", False):
                d.pop(a.name, None)
        return d

    d = {}

    for a in attrs:
        if a.metadata.get("no_export", False):
            continue

        raw_value = getattr(inst, a.name)
        if raw_value is MISSING:
            continue

        if (c := a.metadata.get("export_converter", None)) is not None:
            value = c(raw_value)
        else:
            value = _to_dict_any(raw_value)

        if isinstance(value, (bool, int)) or value:
            d[a.name] = value

    return d


def _to_dict_any(inst: T) -> dict | list | str | T:
    """
    Converts any type to a dict.

    Args:
        inst: The instance to convert.

    Returns:
        The processed dict.

    """
    if has(inst.__class__):
        return to_dict(inst)
    elif isinstance(inst, dict):
        return {key: _to_dict_any(value) for key, value in inst.items()}
    elif isinstance(inst, (list, tuple, set, frozenset)):
        return [_to_dict_any(item) for item in inst]
    elif isinstance(inst, datetime):
        if inst.tzinfo:
            return inst.isoformat()
        else:
            return inst.replace(tzinfo=timezone.utc).isoformat()
    else:
        return inst


def dict_filter_none(data: dict) -> dict:
    """
    Filters out all values that are None.

    Args:
        data: The dict data to filter.

    Returns:
        The filtered dict data.

    """
    return {k: v for k, v in data.items() if v is not None}


def dict_filter(data: dict) -> dict:
    """
    Filters out all values that are MISSING sentinel and converts all sets to lists.

    Args:
        data: The dict data to filter.

    Returns:
        The filtered dict data.

    """
    filtered = data.copy()
    for k, v in data.items():
        if v is MISSING:
            filtered.pop(k)
        elif isinstance(v, set):
            filtered[k] = list(v)
    return filtered


def to_image_data(imagefile: Optional[UPLOADABLE_TYPE]) -> Optional[str]:
    """
    Converts an image file to base64 encoded image data for discord api.

    Args:
        imagefile: The target image file to encode.

    Returns:
        The base64 encoded image data.

    """
    match imagefile:
        case bytes():
            image_data = imagefile
        case IOBase():
            image_data = imagefile.read()
        case Path() | str():
            with open(str(imagefile), "rb") as image_buffer:
                image_data = image_buffer.read()
        case File():
            with imagefile.open_file() as image_buffer:
                image_data = image_buffer.read()
        case _:
            return imagefile

    mimetype = _get_file_mimetype(image_data)
    encoded_image = b64encode(image_data).decode("ascii")

    return f"data:{mimetype};base64,{encoded_image}"


def _get_file_mimetype(filedata: bytes) -> str:
    """
    Gets the mimetype of a file based on file signature.

    Args:
        filedata: The file data to process.

    Returns:
        The mimetype of the file.

    """
    if filedata.startswith((b"GIF87a", b"GIF89a")):
        return "image/gif"
    elif filedata.startswith(b"\x89PNG\x0D\x0A\x1A\x0A"):
        return "image/png"
    elif filedata.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    elif filedata[0:4] == b"RIFF" and filedata[8:12] == b"WEBP":
        return "image/webp"
    else:
        return "application/octet-stream"
