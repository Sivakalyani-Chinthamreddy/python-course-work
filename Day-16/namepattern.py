#D name using pattern
n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#B name using pattern
n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#e 
n = int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#f 
n = int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#c
n=int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#g
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m)or (i==m and j>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#h
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==m :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#j
n=int(input("Enter a numbe: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or (i==n-1 and j<=m) or j==m or (j==0 and i>=m) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#z
n=int(input("Enter a numbe: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#x
n=int(input("Entyer size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#y
n=int(input("Enter a numbe: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#k
n=int(inpur("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i+j==n-1 and i>=m) or (i==j and i>=m):
#letter M
n=int(input("Enter a numbe: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==j and i<=m) or (i+j==n-1 and i<=m)or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter W
n=int(input("Enter a numbe: "))
m=n//2
for i in range(n):
    for j in range(n):
        if  j==0 or (i+j==n-1 and i>=m) or (i==j and i>=m) or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter v
n=int(input("Enetr size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or i-j==m or i+j==n+m-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter A
n=int(input("Enetr size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i>=m) or (j==n-1 and i>=m) or i+j==m or j-i==m or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter s
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or (j==n-1 and i>=m) or (j==0 and i<=m) or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter Q
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or (i==j and i>=m ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter I
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter L
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter N
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter O
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter P
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (j==n-1 and i<=m) or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter R
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (j==n-1 and i<=m) or i==m or(i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter T
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter U
n=int(input("Enter size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
