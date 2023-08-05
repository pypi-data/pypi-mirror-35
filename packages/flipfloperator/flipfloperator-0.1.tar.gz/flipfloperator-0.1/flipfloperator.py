r"""
Implementation of the flip-flop operator in Python.

#sorrynotsorry

>>> for i in range(1, 20 + 1):
...     if ꓺ(i == 5, i == 10):
...         print(i)
5
6
7
8
9
10

>>> for line in '''
... zero indentation
... indent
... inside block
... dedent
... after the block
... indent
... another block
... dedent
... end of file
... '''.strip().split('\n'):
...     if ꓺ(line.startswith('indent'), line.startswith('dedent')):
...         print('  ' + line)
...     else:
...         print(line)
zero indentation
  indent
  inside block
  dedent
after the block
  indent
  another block
  dedent
end of file

>>> def bobo_nickname_finder(phrase):
...     name = []
...     phrase = phrase.replace('.', '').replace(',', '')
...     for word in phrase.split():
...         if ꓺ(word == 'Monsieur', word == 'Bobo'):
...             name.append(word)
...     return ' '.join(name)
>>> bobo_nickname_finder('''
... I have had a great day with this large boy, Monsieur Bobo.
... You may also know him as Monsieur 'Chonky' Bobo, or Monsieur
... 'Loves to Eat the Food' Bobo.
... ''')
"Monsieur Bobo Monsieur 'Chonky' Bobo Monsieur 'Loves to Eat the Food' Bobo"
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
