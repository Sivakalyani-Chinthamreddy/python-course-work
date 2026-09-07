Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#type conversions
#int data type
a=2
float(a)
2.0
complex(a)
(2+0j)
bool(a)
True
str(a)
'2'
list(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> #float data type
>>> b=2.7
>>> int(b)
2
>>> complex(b)
(2.7+0j)
>>> bool(b)
True
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
>>> str(b)
'2.7'
>>> #complex data type
>>> c=3+8j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(3+8j)'
bool(c)
True
list(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
#list
a=[1,4,8,9]
tuple(a)
(1, 4, 8, 9)
set(a)
{8, 1, 4, 9}
bool(a)
True
str(a)
'[1, 4, 8, 9]'
#tuple
a=(2,8,7,6)
list(a)
[2, 8, 7, 6]
bool(a)
True
set(a)
{8, 2, 6, 7}
str(a)
'(2, 8, 7, 6)'
int(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
#set
a={2,5,7}
list(a)
[2, 5, 7]
tuple(a)
(2, 5, 7)
bool(a)
True
str(a)
'{2, 5, 7}'
#Dictionary
a={'kalyani:5','kk:9'}
type(a)
<class 'set'>
list(a)
['kk:9', 'kalyani:5']
tuple(a)
('kk:9', 'kalyani:5')
a=['kalyani:5','kk:9']
type(a)
<class 'list'>
