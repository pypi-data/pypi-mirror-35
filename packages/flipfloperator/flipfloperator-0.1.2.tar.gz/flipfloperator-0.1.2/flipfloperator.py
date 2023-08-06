r"""
Implementation of the flip-flop operator in Python.

#sorrynotsorry

"""

import sys

__all__ = ['ꓺ']

def serialize_locals(d):
    return tuple(sorted([
        (name, id(value))
        for name, value in d.items()
    ]))

def serialize_frames(frame):
    key = []
    refs = []
    while frame is not None:
        refs.append(frame.f_code)
        key.append(id(frame.f_code))
        key.append(frame.f_lasti)
        frame = frame.f_back
    return tuple(key), refs

_TRACES = {}

def ꓺ(flip, flop):
    parent_frame = sys._getframe().f_back
    key, refs = serialize_frames(parent_frame)
    _, state = _TRACES.get(key, (None, False))
    result = state

    if not state and flip:
        state = True
        result = state
    elif state and flop:
        state = False

    _TRACES[key] = refs, state
    return result
