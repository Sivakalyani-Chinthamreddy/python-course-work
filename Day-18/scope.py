#Local variable:means the variable declared inside of the function and it access only inside function
'''def display():
    n=10
    print("inside function",n)

display()
print("outside of  a function",n)
#Global variable:means the varible declared outside of the function and it can access for both inside and outside of the functions
def display():
    print("inside of the function",n)
n=10
display()
print("outside of the function",n)
#global keyword makes local variable as global variable
def name():
    global n
    n="python"
    print("name of the course:",n)
name()
print("name of the course",n)
#when we are using varible as global we should not pass that varible as parameter why is it will automatically stores it as parametr
def display():
    global n
    n=12
    n+=10
    print(n)

display()
print(n)
#A non-local variable is a variable that is defined in an outer function but is used inside an inner (nested) function.
def display():
    course="python"
    def update():
        nonlocal course
        course="java"
        print("inner function:",course)
    update()
    print("outer function:",course)
display()
#buil in function scope:
#when we are using a function as variable it losses its actual funactional scope and starts act as a varible
#so never use builin function as varible
l=[1,2,5,7]
print(sum(l))
#in this sum acts as a varible
sum=78
print(sum)'''

