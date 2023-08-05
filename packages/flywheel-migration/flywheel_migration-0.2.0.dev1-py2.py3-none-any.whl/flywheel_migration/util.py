"""Reaper utility functions"""

import string

import tzlocal

DEFAULT_TZ = tzlocal.get_localzone()


def localize_timestamp(timestamp, timezone=None):
    # pylint: disable=missing-docstring
    timezone = DEFAULT_TZ if timezone is None else timezone
    return timezone.localize(timestamp)


def parse_sort_info(sort_info, default_subject=''):
    # pylint: disable=missing-docstring
    subject, _, group_project = sort_info.strip(string.whitespace).rpartition('@')
    delimiter = next((char for char in '/:' if char in group_project), '^')
    group, _, project = group_project.partition(delimiter)
    return subject or default_subject.strip(string.whitespace), group, project


def is_seekable(fp):
    """Check if the given file-like object is seekable"""
    seekable_fn = fp.getattr('seekable', None)
    if seekable_fn:
        return seekable_fn()

    seek_fn = fp.getattr('seek', None)
    return callable(seek_fn)
