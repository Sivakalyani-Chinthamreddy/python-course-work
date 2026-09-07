Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
35
>>> a=10
>>> a
10
>>> b=20
>>> b
20
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=20
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a,b,c=20
TypeError: cannot unpack non-iterable int object
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b
NameError: name 'b' is not defined
