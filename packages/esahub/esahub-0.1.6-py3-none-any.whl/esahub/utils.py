# coding=utf-8
from __future__ import print_function
import os
import sys
import datetime as DT
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse, parserinfo
from dateutil.tz import tzutc
import re
import json
from distutils.spawn import find_executable
from collections import OrderedDict


PY2 = sys.version_info < (3, 0)
DATE_FMT = '%Y-%m-%dT%H:%M:%SZ'


# -----------------------------------------------------------------------------
# Python 2/3 compatibility.
# -----------------------------------------------------------------------------
def _which(exe):
    """Returns path of `exe` if found, else None."""
    return find_executable(exe)


_range = range if not PY2 else xrange


def eprint(*args, **kwargs):
    """Print to stderr"""
    print(*args, file=sys.stderr, **kwargs)


# -----------------------------------------------------------------------------
# Datetime parsing and formatting
# -----------------------------------------------------------------------------
def parse_datetime(value, dayfirst=False, force=None):
    """
    Parse a date time string.

    Parameters
    ----------
    force : str, optional
        - 'date' : Force return of a single datetime object.
        - 'range' : Force return of a range of datetime objects.

    Returns
    -------

    """
    def _parse_single_value(value):
        # Only extract the datetime parts that are actually given!
        defaults = [DT.datetime(1, 1, 1, 0, 0, 0),
                    DT.datetime(2, 2, 2, 2, 2, 2)]
        info = parserinfo(dayfirst=dayfirst)
        parsed = [parse(value, info, default=d) for d in defaults]
        start = parsed[0]

        if start == parsed[1]:
            # All attributes have been provided,
            # i.e. an exact date has been passed.
            return (start, start)

        # Determine which attributes have actually been specified.
        attrs = ['year', 'month', 'day', 'hour', 'minute', 'second']
        given_attrs = set(
            [attr for attr in attrs if
             getattr(parsed[1], attr) == getattr(parsed[0], attr)])

        # If some attributes are left out, return a time span.
        if given_attrs == set(['year']):
            end = start + relativedelta(years=1)
        elif given_attrs == set(['year', 'month']):
            end = start + relativedelta(months=1)
        elif given_attrs == set(['year', 'month', 'day']):
            end = start + relativedelta(days=1)
        elif given_attrs == set(['year', 'month', 'day', 'hour']):
            end = start + relativedelta(hours=1)
        else:
            return (start, start)

        return (start, end)

    splitters = ['to', '-', ',']
    try:
        stripped = value.strip()
        # Check for open ended date range:
        for s in splitters:
            if stripped.startswith(s):
                parsed = _parse_single_value(stripped.lstrip(s))
                return (None, parsed[1])
            elif stripped.endswith(s):
                parsed = _parse_single_value(stripped.rstrip(s))
                return (parsed[0], None)
        # Treat as single date
        parsed = _parse_single_value(value)
        return parsed

    except ValueError as e:
        #
        # Attempt to split into pair of values
        # if explicitly given a range
        #
        for splitter in splitters:
            if splitter in value:
                parts = value.split(splitter)
                if len(parts) > 2:
                    limit = len(parts) // 2
                    parts = (splitter.join(parts[:limit]),
                             splitter.join(parts[limit:]))
                parts = [_.strip() for _ in parts]
                start, end = [_parse_single_value(_) if bool(_) else None
                              for _ in parts]
                start = start[0]
                end = end[1]
                return start, end

    raise ValueError("Could not parse as datetime: %s" % value)


def to_date(string, fmt=None, output='str'):
    """Date to string with forced timezone information."""
    if string.startswith('UTC='):
        string = string[4:] + 'Z'
    if fmt is None:
        date_object = parse(string)
    else:
        date_object = DT.datetime.strptime(string, fmt)
    if date_object.tzinfo is None:
        date_object = date_object.replace(tzinfo=tzutc())
    if output == 'str':
        # return date_object.isoformat()
        return date_object.strftime(DATE_FMT)
    elif output == 'date':
        return date_object


def fix_product_name(product):
    return os.path.split(product)[1]


def fix_processing_level(string):
    return string.replace('Level-', 'L').strip()


def nth_char(string, n, convert=str, fmt='{}'):
    return convert(fmt.format(string[n]))


def substring(string, a, b):
    return string[a:b]


def strip(string):
    return string.strip()


def get_satellite(filename):
    f = os.path.split(filename)[1]
    return f[:f.find('_')]


def level_from_filename(filename):
    sat = get_satellite(filename)
    f = os.path.split(filename)[1]
    if sat == 'AE':
        return f[16:18]


def duration_from_filename(filename):
    sat = get_satellite(filename)
    f = os.path.split(filename)[1]
    if sat == 'AE':
        return str(int(int(f[38:47].lstrip('0'))/1000.))


# -----------------------------------------------------------------------------
# Human readable byte sizes
# -----------------------------------------------------------------------------
def b2h(num, suffix='B'):
    """Format file sizes as human readable.

    https://stackoverflow.com/a/1094933

    Parameters
    ----------
    num : int
        The number of bytes.
    suffix : str, optional
        (default: 'B')

    Returns
    -------
    str
        The human readable file size string.

    Examples
    --------
    >>> b2h(2048)
    '2.0kB'
    """
    try:
        for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z']:
            if abs(num) < 1024.0:
                return '{0:3.1f}{1}{2}'.format(num, unit, suffix)
            num /= 1024.0
        return '{0:.1f}{1}{2}'.format(num, 'Y', suffix)
    except:
        return '-'


def h2b(hstr, suffix='B'):
    """Format file sizes from human readable to bytes.

    Parameters
    ----------
    hstr : str
        The human readable size string.
    suffix : str, optional
        (default: 'B')

    Returns
    -------
    float
        The number of bytes if successfully parsed. None otherwise.

    Examples
    --------
    >>> h2b('3.5MB')
    3670016.0
    """
    m = re.search('^[0-9\.]*', hstr)
    num = float(m.group(0))
    unit = hstr.replace(m.group(0), '').lstrip().upper()
    # factor = 1.0
    for prefix in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if unit == prefix + suffix:
            return num
        num *= 1024.0
    return None


# -----------------------------------------------------------------------------
# List and dict operations
# -----------------------------------------------------------------------------
def flatten(l):
    """Flatten a list of lists.

    Parameters
    ----------
    l : list of lists
        A nested list

    Returns
    -------
    list
        A flat list
    """
    return [item for sublist in l for item in sublist]


def unique_by(l, fn):
    """Return a filtered list such that a given function is unique
    for each element of the list.

    Parameters
    ----------
    l : list
        A list of arbitrary objects.
    fn : function
        Must return a hashable object.

    Returns
    -------
    list
        A list of unique elements according to `fn`.
    """
    by_key = OrderedDict(zip([fn(_) for _ in l], l))
    return list(by_key.values())


def chunks(l, n):
    """Yield successive n-sized chunks from l.

    https://stackoverflow.com/a/312464

    Parameters
    ----------
    l : iterable
        The list or list-like object to be split into chunks.
    n : int
        The size of the chunks to be generated.

    Yields
    ------
    iterable
        Consecutive slices of l of size n.
    """
    for i in _range(0, len(l), n):
        yield l[i:i + n]


def equal_list_of_dicts(obj1, obj2, exclude=[]):
    """Check whether two lists of dictionaries are equal, independent of the
    order within the list.

    Parameters
    ----------
    obj1 : list of dict
        First object to compare
    obj2 : list of dict
        Second object to compare
    exclude : list of str, optional
        A list of keys that are to be excluded when deciding whether the lists
        of dictionaries are equal (default: []).

    Returns
    -------
    bool
        True if the two lists contain the same dictionaries, False otherwise.
    """
    for key in exclude:
        for i in obj1:
            del i[key]
        for i in obj2:
            del i[key]
    serial1 = [json.dumps(_, sort_keys=True) for _ in obj1]
    serial2 = [json.dumps(_, sort_keys=True) for _ in obj2]

    return set(serial1) == set(serial2)


def select(objects, unlist=True, first=False, **kwargs):
    """Returns a subset of `objects` that matches a range of criteria.

    Parameters
    ----------
    objects : list of dict, dict of dict
        The collection of objects to filter based on keys.
    first: bool, optional
        If True, return first entry only (default: False).
    unlist : bool, optional
        If True and the result has length 1 and objects is a list, return the
        object directly, rather than the list (default: True).
    kwargs : dict
        Criteria as key-value pairs that must be true for each item in
        `objects`.

    Returns
    -------
    list
        A list of all items in `objects` that match the specified criteria.

    Examples
    --------
    >>> select([{'a': 1, 'b': 2}, {'a': 2, 'b': 2}, {'a': 1, 'b': 1}], a=1)
    [{'a': 1, 'b': 2}, {'a': 1, 'b': 1}]
    """
    filtered_objects = objects
    if type(objects) is list:
        for key, val in kwargs.items():
            filtered_objects = [obj for obj in filtered_objects
                                if key in obj and obj[key] == val]
    elif type(objects) is dict:
        for key, val in kwargs.items():
            filtered_objects = {obj_key: obj for obj_key, obj
                                in filtered_objects.items()
                                if key in obj and obj[key] == val}
    if first:
        if type(filtered_objects) is list:
            return filtered_objects[0]
        elif type(filtered_objects) is dict:
            return filtered_objects[list(filtered_objects.keys())[0]]
    elif unlist and len(filtered_objects) == 1 and \
            type(filtered_objects) is list:
        return filtered_objects[0]
    else:
        return filtered_objects


# -----------------------------------------------------------------------------
# File system operations
# -----------------------------------------------------------------------------
def ls(directory, extensions=['.zip', '.tgz', '.nc'], subset=None, path=True):
    """Recursively list the files in a directory.

    Parameters
    ----------
    directory : str
        The path of the directory in which to search for files.
    extensions : list of str, optional
        A list of file extensions to include (default: ['.zip', '.tgz', '.nc'])
    subset : list of str, optional
        Restrict the returned list to filenames appearing in `subset`.
    path : bool, optional
        If True, return the full path of each file. Otherwise return only the
        filenames (default: True).

    Returns
    -------
    list of str
        A list of all files with matching extensions in the directory.
    """
    def _in_subset(f):
        if subset is None and os.path.splitext(f)[1].lower() in extensions:
            return True
        elif subset is not None:
            for s in subset:
                if f.startswith(s):
                    return True
            return False
        else:
            return False

    all_files = []
    for (root, subdirs, files) in os.walk(directory):
        for f in files:
            if _in_subset(f):
                if path:
                    all_files.append(os.path.join(root, f))
                else:
                    all_files.append(f)
    return all_files
