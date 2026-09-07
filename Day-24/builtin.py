import random
name=input("Enter name: ")
dob=input("Enter dob[dd-mm-yyyy]: ")
spc=['@','#','$','%','&','*','.']
password=name+random.choice(spc)+dob[0:2]
print(password)