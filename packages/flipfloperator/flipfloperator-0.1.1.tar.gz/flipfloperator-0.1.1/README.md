# Flipfloperator

This package implements the flip-flop operator in Python.

Install the package:

```
$ pip install flipfloperator
```

And then import the operator into your code:

```
from flipfloperator import ꓺ
```

## Examples

Want to print out numbers between 1 to 20, but only after you reach 5 and stop
when you reach 10?

```
>>> for i in range(1, 20 + 1):
...     if ꓺ(i == 5, i == 10):
...         print(i)
5
6
7
8
9
10
```

A handy text indenter:

```
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
```

And you too can find adorable cat nicknames in text:

```
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
```
