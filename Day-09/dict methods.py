Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dictionary is mutable orderd het and iniq/dupl
d={}
type(d)
<class 'dict'>
d={1:1,2:2,3:45,5:90}
d
{1: 1, 2: 2, 3: 45, 5: 90}

d=
SyntaxError: invalid syntax
[]
[]
d={}
d[1]=a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d[1]=a
NameError: name 'a' is not defined
d[1]=1
d[12.3]=1
d["str"]=1
d[3+9j]=1
d[(1,2,3)]=1
d[[1,2,3]}=1
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: unhashable type: 'list'
d[{1,2,3}]=1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[{1,2,3}]=1
TypeError: unhashable type: 'set'
d[{1:1,3:4}]=1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[{1:1,3:4}]=1
TypeError: unhashable type: 'dict'
d[Fasle]=1
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d[Fasle]=1
NameError: name 'Fasle' is not defined. Did you mean: 'False'?
d
{1: 1, 12.3: 1, 'str': 1, (3+9j): 1, (1, 2, 3): 1}
d={}
d[1]=1
d[2]=1.3
d[3]="str"
d[4]=6+9j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3,5}
d[8]={1:3,7:9}
d[9]=frozenset({1,7,0})
d[10]=False
d
{1: 1, 2: 1.3, 3: 'str', 4: (6+9j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3, 5}, 8: {1: 3, 7: 9}, 9: frozenset({0, 1, 7}), 10: False}
d={}
d[1]=1
d[2]=1
d
{1: 1, 2: 1}
d[1]=1
d[1]=2
d
{1: 2, 2: 1}
d[1]=1
d
{1: 1, 2: 1}
d={}
d[1]=1
d
{1: 1}
d[1]=3
d
{1: 3}
data={'name':'kalyani','batch':65,'course':'python}
      
SyntaxError: unterminated string literal (detected at line 1)
data={'name':'kalyani','batch':65,'course':'python'}
      
data
      
{'name': 'kalyani', 'batch': 65, 'course': 'python'}
'name' in data
      
True
'kalyani' in data
      
False
'batch' in data
      
True
'batch'  not in data
      
False
data
      
{'name': 'kalyani', 'batch': 65, 'course': 'python'}
data[name]
      
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    data[name]
NameError: name 'name' is not defined
data['name']
      
'kalyani'
data['course']
      
'python'
data.get('age']
      
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
data('age')
      
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    data('age')
TypeError: 'dict' object is not callable
data.get('course')
      
'python'
data.get('age')
      
data.get('age' 'key is not present')
      
data.get('age' ,'key is not present')
      
'key is not present'
data.get('batch','key is present')
      
65
data
      
{'name': 'kalyani', 'batch': 65, 'course': 'python'}
data['age']=22
      
data
      
{'name': 'kalyani', 'batch': 65, 'course': 'python', 'age': 22}
data.update['phone':456789,'py':2026]
      
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    data.update['phone':456789,'py':2026]
TypeError: 'builtin_function_or_method' object is not subscriptable
data.update{'phone':456789,'py':202}
      
SyntaxError: invalid syntax
data.update('phone':456789,'py':202)
      
SyntaxError: invalid syntax
data.update{('phone':456789,'py':202})
      
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
data.update({'phone':456789,'py':202})
      
data
      
{'name': 'kalyani', 'batch': 65, 'course': 'python', 'age': 22, 'phone': 456789, 'py': 202}
data.popitem()
      
('py', 202)
data.pop('py')
      
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    data.pop('py')
KeyError: 'py'
data.pop('age')
      
22
data('course')='python full stack '
      
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
data['course']='python full stac'
      
data
      
{'name': 'kalyani', 'batch': 65, 'course': 'python full stac', 'phone': 456789}
del data['name']
      
data
      
{'batch': 65, 'course': 'python full stac', 'phone': 456789}
data.clear()
      
data={'name':'kalyani,'age':21,'course':'python'}
      
SyntaxError: unterminated string literal (detected at line 1)
data={'name':'kalyani','age':21,'course':'python','ph':56789,'email':hk@678}
      
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    data={'name':'kalyani','age':21,'course':'python','ph':56789,'email':hk@678}
NameError: name 'hk' is not defined
data={'name':'kalyani','age':21,'course':'python','ph':56789,'email':'hk'@678}
      
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    data={'name':'kalyani','age':21,'course':'python','ph':56789,'email':'hk'@678}
TypeError: unsupported operand type(s) for @: 'str' and 'int'
data={'name':'kalyani','age':21,'course':'python','ph':56789,'email':'hk@'678}
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
data={'name':'kalyani','age':21,'course':'python','ph':56789}
      
data
      
{'name': 'kalyani', 'age': 21, 'course': 'python', 'ph': 56789}
len(data)
      
4
data.keys()
      
dict_keys(['name', 'age', 'course', 'ph'])
data.values()
      
dict_values(['kalyani', 21, 'python', 56789])
data.elements()
      
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    data.elements()
AttributeError: 'dict' object has no attribute 'elements'
data.items()
      
dict_items([('name', 'kalyani'), ('age', 21), ('course', 'python'), ('ph', 56789)])
max(data)
      
'ph'
min(data)
      
'age'
sum(data)
      
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    sum(data)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
data.count(21)
      
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    data.count(21)
AttributeError: 'dict' object has no attribute 'count'
data=m
      
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    data=m
NameError: name 'm' is not defined
data = m
      
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    data = m
NameError: name 'm' is not defined
data = {1:2,3:7}
      
data = m
      
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    data = m
NameError: name 'm' is not defined
m = data
      
m
      
{1: 2, 3: 7}
data
      
{1: 2, 3: 7}
m[7]=3
      
m
      
{1: 2, 3: 7, 7: 3}
n=d.copy()
      
n
      
{1: 3}
d
      
{1: 3}
n[6]=3
...       
>>> d
...       
{1: 3}
>>> m
...       
{1: 2, 3: 7, 7: 3}
>>> data
...       
{1: 2, 3: 7, 7: 3}
>>> data.get(2)
...       
>>> data
...       
{1: 2, 3: 7, 7: 3}
>>> data.setdefault(2,67)
...       
67
>>> data
...       
{1: 2, 3: 7, 7: 3, 2: 67}
>>> data.setdeafult(1,89)
...       
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    data.setdeafult(1,89)
AttributeError: 'dict' object has no attribute 'setdeafult'. Did you mean: 'setdefault'?
>>> data.setdefault(1,89)
...       
2
>>> da.fromkeys(["python","java","sql"],0)
...       
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    da.fromkeys(["python","java","sql"],0)
NameError: name 'da' is not defined
>>> dict.fromkeys(["python","java","sql"],99)
...       
{'python': 99, 'java': 99, 'sql': 99}
