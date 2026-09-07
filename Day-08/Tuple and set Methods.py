Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple
t=()
type(t)
<class 'tuple'>
t=tuple()
t
()
t=(1,2,3,4)
t
(1, 2, 3, 4)
t=(1)
t
1
t=(1,)
t
(1,)
t=(2,2,2,3)
t
(2, 2, 2, 3)
t=(89,78,67,56)
t
(89, 78, 67, 56)
t=(1,'dtr',[1,2,],{1:5},8+9j,True)
t
(1, 'dtr', [1, 2], {1: 5}, (8+9j), True)
t=(1,'dtr',[1,2,],{1:5},8+9j,True,(1,3))
t
(1, 'dtr', [1, 2], {1: 5}, (8+9j), True, (1, 3))
t=('ka')
t
'ka'
t=('ka',)
t
('ka',)
#tuple operations
t=(1,2,3)
s=(8,9,7)
t+s
(1, 2, 3, 8, 9, 7)
t*5
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t[0]
1
t[-1]
3
s[2]
7
t[::-1]
(3, 2, 1)
t=(1,67,90,'python',True,"java",{1,4})
t[::-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
t[::-1]
({1, 4}, 'java', True, 'python', 90, 67, 1)
t[:4]
(1, 67, 90, 'python')
t[-1:-5:-1]
({1, 4}, 'java', True, 'python')
1 in t
True
'pyhton' in t
False
'java' in t
True
'z' in t
False
8 not in t
True
t=(1,2,3,4,66,77,55,66,99,3,4,2)
t
(1, 2, 3, 4, 66, 77, 55, 66, 99, 3, 4, 2)
max(t)
99
min(t)
1
sorted(t)
[1, 2, 2, 3, 3, 4, 4, 55, 66, 66, 77, 99]
sum(t)
382
t
(1, 2, 3, 4, 66, 77, 55, 66, 99, 3, 4, 2)
t.index(2)
1
t.find(3)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    t.find(3)
AttributeError: 'tuple' object has no attribute 'find'
t,index(66)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    t,index(66)
NameError: name 'index' is not defined
t.index(55)
6
t.index(2)
1
t.rindex(2)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    t.rindex(2)
AttributeError: 'tuple' object has no attribute 'rindex'. Did you mean: 'index'?
len(t)
12
t.count(66)
2
t=(1,2,0)
all(t)
False
any(t)
True
t=(1,2,3)
t
(1, 2, 3)
a,b,c=t
a
1
b
2
c
3
t=(1,3,4,[1,2,3],5)
t[3]
[1, 2, 3]
t.append(5)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    t.append(5)
AttributeError: 'tuple' object has no attribute 'append'
t[3].append(5)
t
(1, 3, 4, [1, 2, 3, 5], 5)
t[3].pop()
5
t
(1, 3, 4, [1, 2, 3], 5)
t[4].insert(1,89)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t[4].insert(1,89)
AttributeError: 'int' object has no attribute 'insert'
t[4].extend(1,2,3)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t[4].extend(1,2,3)
AttributeError: 'int' object has no attribute 'extend'
#set
s={}
type(s)
<class 'dict'>
s=set()
type(S)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined
type(s)
<class 'set'>
s={1,2,3,4}
s
{1, 2, 3, 4}
s={78,909090,1,579809}
s
{1, 909090, 579809, 78}
s={9,9,9,9}
s
{9}
s=set()
s.add(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s.add(1,2,3,4,5)
TypeError: set.add() takes exactly one argument (5 given)
s.add(1)
s.add(4.5)
s.add("str")
s.add(4+9j)
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,2,3,4))
s.add({1:3})
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.add({1:3})
TypeError: unhashable type: 'dict'
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
s.add(False)
s
{False, 1, 4.5, (1, 2, 3, 4), 'str', (4+9j)}
#set operations
a={1,2,3,4,5}
b={4,5,7,8,9}
2 in a
True
2 not in b
True
6 in a
False
6 not in b
True
#union
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
#intersection
a & b
{4, 5}
#difference
a - b
{1, 2, 3}
b - a
{8, 9, 7}
#symmetric
a^b
{1, 2, 3, 7, 8, 9}
#subset and superset
{1}<=a
True
{6}<=a
False
{1,4}>=a
False
a>={1,4}
True
a>={9,10}
False
a.isdisjoint(b)
False
a={1,2,3,4,5,6,7}
sorted(a)
[1, 2, 3, 4, 5, 6, 7]
a=(89,67,1,90,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
a={89,67,1,90,3}
soretd(a)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    soretd(a)
NameError: name 'soretd' is not defined. Did you mean: 'sorted'?
sorted(a)
[1, 3, 67, 89, 90]
max(a)
90
min(a)
1
len(a)
5
any(a)
True
all({1,"",False})
False
sum(a)
250
a={1,2,3,45}
c=a
c.add(21)
a
{1, 2, 3, 45, 21}
c
{1, 2, 3, 45, 21}
c=a.copy()
a
{1, 2, 3, 45, 21}
c
{1, 2, 3, 21, 45}
c.add(89)
a
{1, 2, 3, 45, 21}
c
{1, 2, 3, 21, 89, 45}
>>> a={1,2,3,4,5}
>>> a.add(6)
>>> a.update(190,99,0}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> a.update(190,99,0)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    a.update(190,99,0)
TypeError: 'int' object is not iterable
>>> a.add(update(190,99,0))
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    a.add(update(190,99,0))
NameError: name 'update' is not defined
>>> a.update({90,890,8})
>>> a
{1, 2, 3, 4, 5, 6, 8, 90, 890}
>>> a.update({1,2,3})
>>> a
{1, 2, 3, 4, 5, 6, 8, 90, 890}
>>> a.pop()
1
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    a.remove(1)
KeyError: 1
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    a.remove(1)
KeyError: 1
>>> a.discard(1)
>>> a
{2, 3, 4, 5, 6, 8, 90, 890}
>>> a.remove(5)
>>> a
{2, 3, 4, 6, 8, 90, 890}
