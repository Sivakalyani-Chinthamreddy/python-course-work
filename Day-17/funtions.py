
#defining a function
'''def functionname(argument):
       #statement
       return(optional)
#calling a function
functionname(parameter)'''

def gst(price):
    print("Originoal price",price)
    print("final price",price+price*0.18)

gst(1000)
gst(2000)
gst(5000)
gst(100)
gst(55)
gst(563)
#3 table
def table(n):
    print("----------------------------------------------")
    print(f'{n} table')
    print("----------------------------------------------")
    for i in range(1,11):
        print(f'{n}*{i}={n*i}')
table(3)
#tables from 1 to 20
for i in range(1,21):
    table(i)
#check leap year
def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "leap year"
    else:
        return "Not a leap year"
print(isleap(2012))
print(isleap(2025))
print(isleap(2020))
#number is prime or not
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "not a prime"
        else:
            return "prime"
print(prime(11))
print(prime(17))
#positional argument
def details(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
    print("----------------------------")

details("kalyani","kalyani@gail.com","kalyani$134")
details("kalyani$134","kalyani@gail.com","kalyani")
details("kalyani@123","kalyani","kalyani@gail")

#keyword argument
def details(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
    print("----------------------------")

details(name="kalyani",email="kalyani@gail.com",pwd="kalyani$134")
details(pwd="kalyani$134",email="kalyani@gail.com",name="kalyani")
details(pwd="kalyani$123",name="kalyani",email="kalyani@gail")

#deafult argument
def details(name,email,pwd=None,phno=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
    print("phno:",phno)
    print("----------------------------")

details("kalyani","kalyani@gail.com","567888888888888")
details("kalyani$134","kalyani@gail.com","kalyani","4567")
details("kalyani@123","kalyani","kalyani@gail")

#variable length argument
def details(*name):
    print("names:",name)

details("kalyani")
details("siva","python")
details("kalyan","flask","sql")

#if we want out put as key value pairs
def details(**name):
    print("name:",name)

details(name="kalyani")
details(name="siva",course="python")
details(mame="kalyan",course="flask",database="sql")



