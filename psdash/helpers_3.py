from datetime import datetime
import socket
import sys
import json
from typing import Iterable, Set, Dict, Any


ITER_COUNT = 1000 * 1000


def timeit(method):
    def timed(*args, **kw):
        s = datetime.now()
        result = method(*args, **kw)
        e = datetime.now()

        print(method.__name__, '(%r, %r)' % (args, kw), e - s)
        return result
    return timed


_PY3 = (lambda x: [x for x in [False]] and None or x)(True)
"""
    Return True if 'Python >= 3' else False

    If you want to detect pre-Python 3 and don't want to import anything...
        you can (ab)use list comprehension scoping changes
     """
if _PY3:
    try:
        basestring = str
    except:
        pass


# @timeit
def is_iterable(s):
    """Return True if s is a non-string sequence and is iterable."""
    if isinstance(s, basestring):
        return False
    else:
        try:
            _ = iter(s)
            # getattr(s.__iter__)
            return True
        except (AttributeError, TypeError):
            return False


def is_hashable(s):
    """Return True if s is hashable."""
    try:
        _ = s.__hash__().__hash__
        return True
    except IndexError:
        return False
    # return hasattr(s, __hash__)


def socket_constants(prefix):
    return dict((getattr(socket, n), n) for n in dir(socket) if n.startswith(prefix))


socket_families = socket_constants('AF_')
socket_types = socket_constants('SOCK_')


def quick_show(_iter: Dict[Any, Any], separators: Set[str] = ("=> ", ': ')) -> Any:
    try:
        for i in _iter:
            if is_iterable(i):
                quick_show(i)
            elif is_hashable(i):
                print(i, separators[1], quick_show(_iter[i]))
            else:
                print(i)
    except IndexError:
        print(_iter, separators[0])


def get_test_json() -> json:
    test_json: str = '/Volumes/Data/skeptycal/bin/utilities/python/test/test2.json'
    with open(test_json) as f:
        json_file = json.load(f)
        out_file = json.dumps(json_file, skipkeys=True,
                              ensure_ascii=True, check_circular=True,
                              allow_nan=True, indent=2, separators=(",", ':'))


if __name__ == "__main__":
    # quick_show(socket_families)
    # quick_show(socket_types)
    quick_show(globals())
    print('*'*79)
    print()

    # quick_show(get_test_json())
