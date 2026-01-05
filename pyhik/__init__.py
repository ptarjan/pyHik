"""pyhik - Python library for Hikvision camera/NVR events."""

from pyhik.hikvision import (
    HikCamera,
    inject_events_into_camera,
    get_video_channels,
    Recording,
    RecordingDay,
    VideoChannel,
)
from pyhik.constants import __version__, VALID_NOTIFICATION_METHODS

__all__ = [
    'HikCamera',
    'inject_events_into_camera',
    'get_video_channels',
    'Recording',
    'RecordingDay',
    'VideoChannel',
    'VALID_NOTIFICATION_METHODS',
    '__version__'
]
