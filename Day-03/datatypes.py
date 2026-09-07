Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Data type
#int float complex
a=12
type(a)
<class 'int'>
`b=3.9
SyntaxError: invalid syntax
b=9.3
type(b)
<class 'float'>
c=4+7j
type(c)
<class 'complex'>
#sequential data types
#string list and tuple
k="kalyani"
type(k)
<class 'str'>
k+="chinthamreddy"
print(k)
kalyanichinthamreddy
id(k)
2190702863856
k+="siva"
print(k)
kalyanichinthamreddysiva
id(k)
2190744642192
#list is mutable
l=[1,2,3,6]
type(l)
<class 'list'>
l
[1, 2, 3, 6]
id(l)
2190745706176
l+=10
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    l+=10
TypeError: 'int' object is not iterable
l+=[10]
l
[1, 2, 3, 6, 10]
l+=['kalyani']
l
[1, 2, 3, 6, 10, 'kalyani']
#tuple
t=(1,3,7,8)
t
(1, 3, 7, 8)
id(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    id(s)
NameError: name 's' is not defined
id(t)
2190744879968
t+=(77)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t+=(77)
TypeError: can only concatenate tuple (not "int") to tuple
t.append(77)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t.append(77)
AttributeError: 'tuple' object has no attribute 'append'
#set
s={1,3,4,'kalyani'}
s
{1, 3, 4, 'kalyani'}
type(s)
<class 'set'>
s+={39]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
s+={99}
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s+={99}
TypeError: unsupported operand type(s) for +=: 'set' and 'set'
s.add{67}
SyntaxError: invalid syntax
>>> s.add(89)
>>> s
{1, 3, 4, 'kalyani', 89}
>>> id(s)
2190745569088
>>> s.add('siva')
>>> s
{1, 3, 4, 'kalyani', 'siva', 89}
>>> id(s)
2190745569088
>>> #frozen set
>>> ss={98,9,0)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> ss{7,90,89}
SyntaxError: invalid syntax
>>> ss={87,90,3}
>>> ss
{90, 3, 87}
>>> id(s)
2190745569088
>>> ss.add('kalyani')
>>> ss
{'kalyani', 90, 3, 87}
>>> {'kalyani', 90, 3, 87}
{90, 3, 87, 'kalyani'}
>>> ss=frozenset({3,9,0})
>>> type(ss)
<class 'frozenset'>
>>> ss
frozenset({0, 9, 3})
>>> #boolean
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
>>> a
True
>>> a=None
>>> type(a)
<class 'NoneType'>
