import itertools
from typing import Iterable


def pairwise(iterable: Iterable):
    """Iterate over elements two by two.
    input: [1,2,3,4]
    output -> (1,2), (2,3), (3, 4)
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def iter_slice(iterable: bytes, n: int):
    """Yield slices of size n and says if each slice is the last one.
    input b'12345' 3
    output -> (b'123', False), (b'45', True)
    """
    start = 0
    stop = start + n
    final_offset = len(iterable)

    while True:
        if start >= final_offset:
            break

        rv = iterable[start:stop]
        start = stop
        stop = start + n
        yield rv, start >= final_offset
