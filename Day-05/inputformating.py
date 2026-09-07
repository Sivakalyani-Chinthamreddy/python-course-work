Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#input formating
a=input()
kalyani
a
'kalyani'
b=input("enter a name": )
SyntaxError: invalid syntax
b=input("enter a name:" )
enter a name:siva kalyani
b
'siva kalyani'
c=int(input("enter total marks:" ))
enter total marks:98
c
98
d=float(input("enter price of product:" ))
enter price of product:99.4
d
99.4
#split
names=input()
siva kalyani chinthamreddy
names
'siva kalyani chinthamreddy'
names.split()
['siva', 'kalyani', 'chinthamreddy']
Names=input().split(',')
siva,kalyani,chinthamreddy
Names
['siva', 'kalyani', 'chinthamreddy']
k=input().split(',')
k=input().split(',')
kk ss rr
SyntaxError: invalid syntax
kk,ss,rr
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    kk,ss,rr
NameError: name 'kk' is not defined
k
["k=input().split('", "')"]
names=input()
kalyani pavani chinthamreddy
names.split()
['kalyani', 'pavani', 'chinthamreddy']
names
'kalyani pavani chinthamreddy'
names=list(input("enter the names:").split())
enter the names:siva kalyani chinthamreddy
names
['siva', 'kalyani', 'chinthamreddy']
names=tuple(input("enter the names:").split())
enter the names:siva-kalyani-chinthamreddy
names
('siva-kalyani-chinthamreddy',)
names=tuple(input("enter the names:").split('-'))
enter the names:siva-kalyani-chinthamreddy
names
('siva', 'kalyani', 'chinthamreddy')
marks=input().split()
45 67 89 98
marks
['45', '67', '89', '98']
marks=list(map(int))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    marks=list(map(int))
TypeError: map() must have at least two arguments.
marks=list(map(int,input("Enter a nuber:").split()))
Enter a nuber:34 45 67 89
marks
[34, 45, 67, 89]
mamarks=tuple(map(int,input("Enter a nuber:").split()))
Enter a nuber:98 98 97
mamarks
(98, 98, 97)
mamarks=tuple(map(int,input("Enter a nuber:").split()))
Enter a nuber:456789
mamarks
(456789,)
print(mamarks)
(456789,)
marks=tuple(map(int,input("Enter a nuber:").split()))
Enter a nuber:kalyani
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    marks=tuple(map(int,input("Enter a nuber:").split()))
ValueError: invalid literal for int() with base 10: 'kalyani'
marks=tuple(map(float,input("Enter a nuber:").split()))
Enter a nuber:56 78
marks
(56.0, 78.0)
marks=input().split()
89 68 48
marks
['89', '68', '48']
kk=set(map(int,marks))
89 68 48
SyntaxError: invalid syntax
kk
{48, 89, 68}
a,b,c=int(input().split())
45 67 89
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a,b,c=int(input().split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#packing and unpacking
a,b=[1,2]
a
1
b
2
email,password=input("enter email and password:" )split()
SyntaxError: invalid syntax
email,password=input("enter email and password:" ).split()
enter email and password:k@gmail.com 1234
email
'k@gmail.com'
password
'1234'
name,marks=input("Enter name and marks:" ).split()
Enter name and marks:kalyani 98
name
'kalyani'
marks
'98'
int(marks)
98
name,marks=list(map(int,input("Enter name and marks:" ).split()))
Enter name and marks:kalyani 98
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    name,marks=list(map(int,input("Enter name and marks:" ).split()))
ValueError: invalid literal for int() with base 10: 'kalyani'
s1m,s2m,s3m=list(map(int,input("Enter name and marks:" ).split()))
Enter name and marks:34 56 98
s1m
34
s2m
56
s3m
98
s1m,s2m,s3m=list(map(float,input("Enter name and marks:" ).split()))
Enter name and marks:45 67 89
s1m
45.0
k=input()
98
type(k)
<class 'str'>
>>> #eval
>>> name=eval(input("enter a name: "))
enter a name: kalyani
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    name=eval(input("enter a name: "))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'kalyani' is not defined
>>> name=eval(input("enter a name: "))
enter a name: 67
>>> type(name)
<class 'int'>
>>> name=eval(input("enter a name: "))
enter a name: kalyani
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    name=eval(input("enter a name: "))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'kalyani' is not defined
>>> name=eval(input("enter value: "))
enter value: [1,2,34,8]
>>> name
[1, 2, 34, 8]
>>> type(name)
<class 'list'>
>>> name=eval(input("enter value: "))
enter value: {3,5,7,9}
>>> name
{9, 3, 5, 7}
>>> type(name)
<class 'set'>
>>> name=eval(input("enter value: "))
enter value: ('kalyani',6,4.6)
>>> name
('kalyani', 6, 4.6)
>>> type(name)
<class 'tuple'>
