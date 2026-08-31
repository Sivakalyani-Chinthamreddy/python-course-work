'''#int float complex string bool and tuple are immutable data types and we are passing these by "passbyvalue" 
#immutable dtatatypes effects only inside of the function and it doesnt effect the outside function
#int
def display(n):
    n+=10
    print("inside function:",n)
n=10
display(n)
print("outside function:",n)
#float
def display(n):
    n+=1.2
    print("inside function:",n)
n=10
display(n)
print("outside function:",n)
#complex
def display(n):
    n+=1
    print("inside function:",n)
n=3+4j
display(n)
print("outside function:",n)
#string
def display(n):
    n+=" language"
    print("inside function:",n)
n="python"
display(n)
print("outside function:",n)
#bool
def display(n):
    n=False
    print("inside function:",n)
n=True
display(n)
print("outside function:",n)
#tuple
def display(n):
    n+=(5,9)
    print("inside function:",n)
n=(1,2,3)
display(n)
print("outside function:",n)
#mutable datatypes are passed by using "passbyreference"
#mutable datables effect both inside and outside functions
#we are passing values by object refence
#list
def display(n):
    n.append(5)
    print("inside function:",n)
n=[1,2,3,4]
display(n)
print("outside function:",n)
#set
def display(n):
    n.add(9)
    print("inside function:",n)
n={1,1,2,4}
display(n)
print("outside function:",n)
#dict
def display(n):
    n[4]=5
    print("inside function:",n)
n={1:2,2:3,3:4}
display(n)
print("outside function:",n)'''