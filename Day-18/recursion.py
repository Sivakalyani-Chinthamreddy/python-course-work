#function calling itself is called recursion
#functions needs to be updated and it have base conditioon and if it reaches to base condition it hse to stop
'''
def function(args):
    if base condition:
    #stop recursion using
    rturn
    #update function
    function(args)
calling function
function()
'''
'''#from 1 to 10 with recursion
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)
#from 10 to 1
def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)'''
#String
def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)
display("python",0)

