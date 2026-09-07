Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#output formating
1=2
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a=1
b=2
c="kalyani"
print(a,b,c)
1 2 kalyani
print("a=",a,"b=",b ,"c=",c)
a= 1 b= 2 c= kalyani
print("a=",a,"b=",b,"c=",c sep('')
      
SyntaxError: '(' was never closed

priprint("a=",a,"b=",b,"c=",c sep(''))
      
SyntaxError: invalid syntax
priprint("a=",a,"b=",b,"c=",c,sep(''))
      
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    priprint("a=",a,"b=",b,"c=",c,sep(''))
NameError: name 'priprint' is not defined
print("a=",a,"b=",b,"c=",c,sep(''))
      
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print("a=",a,"b=",b,"c=",c,sep(''))
NameError: name 'sep' is not defined. Did you mean: 'set'?
print("a=",a,"b=",b,"c=",c,sep='')
      
a=1b=2c=kalyani
print("a=",a,"b=",b,"c=",c,sep'\n')
      
SyntaxError: invalid syntax
print("a=",a,"b=",b,"c=",c,sep='\n')
...       
a=
1
b=
2
c=
kalyani
>>> print("a=",a,"b=",b,"c=",c,sep='\n',end='\@')
...       
a=
1
b=
2
c=
kalyani\@
>>> print("a=",a,"b=",b,"c=",c,sep='\n',end='\@\n')
...       
a=
1
b=
2
c=
kalyani\@
>>> print(f'{a},{b},{c}')
...       
1,2,kalyani
>>> print(f'a={a},b={b},c={c}')
...       
a=1,b=2,c=kalyani
>>> print('a=%d,b=%d,c=%s'%(a,b,c))
...       
a=1,b=2,c=kalyani
>>> print('a={},b={},c={}'.formate(a,b,c))
...       
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print('a={},b={},c={}'.formate(a,b,c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> print('a={},b={},c={}'.format(a,b,c))
...       
a=1,b=2,c=kalyani
