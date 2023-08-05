"""syphon.schema.load.py

   Copyright (c) 2017-2018 Keithley Instruments, LLC.
   Licensed under MIT (https://github.com/ehall/syphon/blob/master/LICENSE)

"""
from sortedcontainers import SortedDict


def load(filepath: str) -> SortedDict:
    """Return a `SortedDict` from a schema file.

    Args:
        filepath (str): Absolute filename of the schema file.

    Returns:
        SortedDict: Ordered archive directory storage schema.

    Raises:
        OSError: File operation error. Error type raised may be
            a subclass of OSError.
    """
    from json import loads

    result = SortedDict()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            result = SortedDict(loads(f.read()))
    except OSError:
        raise
    else:
        return result
