#1 to 10
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
#if we write print before recursion it will give nrml order if we give after recursion it will give reverse order

display(1)
 #10 to 1
def display(n):
    if n==11:
        return
    display(n+1)
#if we write print before recursion it will give nrml order if we give after recursion it will give reverse order
    print(n)
display(1)
#print string
def display(n,s):
    if s==len(n):
        return
    print(n[s])
    display(n,s+1)
display("codegnan",0)
#reverse a string
def display(n,s):
    if s==len(n):
        return
    display(n,s+1)
    print(n[s])
display("codegnan",0)

def display(s,ind):
    if ind==s[4]:
        return
    print(s,end=" ")
    display(s,ind+1)
display(input())
#slicing with number
def display(s,ind,w):
    if len(s)-w+1==ind:
        return
    
    print(s[ind:ind+w])
    display(s,ind+1,w)
s=input("Enter name: ")
w=int(input("Enter width: "))
display(s,0,w)

def display(s,ind):
    if ind==len(s):
        return
    print(sum(s))
    display(s,ind+1)
s=[1,2,3]
display(s,0)
#sum of list
def display(l,ind):
    if ind==len(l):
        return 0
    return l[ind]+display(l,ind+1)
l=[23,3,45,67,23,2,9]
print(display(l,0))
#sum of digits
def display(l):
    if l==0:
        return 0
    return l%10 + display(l//10)
l=1234
print(display(l))
#factorial of n
def display(n):
    if n==1:
        return 1
    return n*display(n-1)
print(display(5))
#Fibonacci series with for loop
n=int(input("Enetr a number: "))
if n==1:
    print(0)
elif n==2:
    print(1)
else:
    a,b=0,1
    print(a,b)
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=' ')
#Fibonacci series with recursion
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(8):
    print(fib(i))








