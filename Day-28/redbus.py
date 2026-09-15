class Redbus:
    bus={i: "Available" for i in range(1,11)}

    def displayseats(self):
        print("------abc bus----------")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])

    def booking(self,seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i]=="Available":
                Redbus.bus[i]="Booked"
                print(f"Your seat - {seatno} is booked")
                break
        else:
            print(f"this seat {seatno} is already bokked")


class Driver():
    def __init__(self,name,phno,email,age):
        self.name=name
        self.phno=phno
        self.__email=email
        self.__age=age
    def Driverdetails()


class user(Redbus):
    def __init__(self,name,email,phno):
        self.name=name
        self.eamil=email
        self.phno=phno
        print(f'welcome to Redbus {self.name}')
user1=user('kalyani','kalyani@gmail.com',123456)
user1.displayseats()
user1.booking(4)
user1.displayseats()
user1.booking(4)
user1=Driver("sai",12345,'sai@gmail.com',45)
print(user1.Driverdetails())




