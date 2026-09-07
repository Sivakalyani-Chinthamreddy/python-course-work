Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#python operator
#Airthamatic operator
a=5
b=2
a+b
7
a-b
3
a*5
25
a**7
78125
a**2
25
b**2
4
a/2
2.5
a//2
2
a%2
1
b%2
0
#comparision operators
s=10
k=37
s<k
True
s>k
False
s<=k
True
s>=k
False
#Assignment operator
a=10
a
10
a=a+10
a
20
a+=78
a
98
a -+78
20
a-=78
a
20
a=100
a-=25
a
75
a*=3
a
225
a //+2
112
a=4
a //=2
a
2
a/=2
a
1.0
a%=2
a
1.0
#logical operators
a=True
b=False
a and b
False
a or b
True
a
True
not a
False
3/2==5 and 2/2==1
False
3/2==5 or 2/2==1
True
3//2==5 or 2//2==1
True
True
True
#membership operators
#membership operators(is only for str,list,tuple and dict)
s="kalyani chinthareddy"
'k' in s
True
"kalyani" in s
True
"kalyani" not in s
False
"siva" not in s
True
l=[1,3,5,7,"kalyani"]
"ka" in l
False
1 in l
True
5 in l
True
'kalyani' not in l
False
'ka' not in l
True
t=(1,3,8)
3 in t
True
8 not in t
False
s={'kalyani',3,5,7,9}
s
{'kalyani', 3, 5, 7, 9}
'kalyanui' in s
False
'kalyani' in s
True
"k' in s
SyntaxError: unterminated string literal (detected at line 1)
"k" in s
False
d={'sname':'kalyani', 'id':2,'course':'pfs'}
d
{'sname': 'kalyani', 'id': 2, 'course': 'pfs'}
'sname' in s
False
'sname' in d
True
'kalyani' in d
False
'kalyani' not in d
True
#identical operator
#if both the variables have same object reference or same id it gives true or else false
l=[1,2,3]
m=[1,2,3]
id(l)
1527838440960
id(m)
1527838384704
i is m
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    i is m
NameError: name 'i' is not defined
>>> l is m
False
>>> i is not m
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    i is not m
NameError: name 'i' is not defined
>>> l is not m
True
>>> f=l
>>> f
[1, 2, 3]
>>> id(f)
1527838440960
>>> f is l
True
>>> f is m
False
>>> f is not m
True
>>> #Bitwise operators
>>> 11 &  12
8
>>> 8 | 3
11
>>> 4 ^ 20
16
>>> 8<<2
32
>>> 16<<2
64
>>> 2<<2
8
>>> 4<<2
16
>>> 4>>2
1
>>> 2>>2
0
>>> 3>>2
0
