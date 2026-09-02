#List comprehension is a short and simple way to create a list using a single line of code.
#append 1 to 11
l=[i for i in range(1,11)]
print(l)

#append only even numbers
l=[i for i in range(2,11,2)]
print(l)

#append factors of n
n=18
l=[i for i in range(1,n) if n%i==0]
print(l)

#palce even numbers wirh even and odd with 0
x=[1,2,3,4,5,6,7,8,9]
y=[i if i%2==0 else 0 for i in x]
print(y)



#print nested list
l=[]
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)

#print nested list with list comp
l=[[j for j in range(1,4)] for i in range(3)]
print(l)

#print the nested dictionary
s={i:i*i for i in range(1,11)}
print(s)
