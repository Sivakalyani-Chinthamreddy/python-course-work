from abc import ABC,abstractmethod

class Payment(ABC):
    def source(self):
        print("Scanner/upit/mobilenumber")

    def amount(self):
        print("Enter the amount")

    def bank(self):
        print("select the bank")

    def pin(self):
        print("Enter the pin")

    @abstractmethod
    def paymentprocess(self):
        print("payment is processing")
    def paymentresult(self):
        print("payment successufully")

class HDFC(Payment):
    def paymentprocess(self):
        print("you selceted HDFC bank")

class ICIC(Payment):
    def paymentprocess(self):
        print("you selcted ICIC bank")

class APGB(Payment):
    def paymentprocess(self):
        print("you selcted APGB")

class UNION(Payment):
    def paymentprocess(self):
        print("you selcetd UNION")

user1=HDFC()
user1.source()
user1.amount()
user1.bank()
user1.pin()
user1.paymentprocess()
user1.paymentresult()


user2=ICIC()
user2.source()
user2.amount()
user2.bank()
user2.pin()
user2.paymentprocess()
user2.paymentresult()


user3=APGB()
user3.source()
user3.amount()
user3.bank()
user3.pin()
user3.paymentprocess()
user3.paymentresult()



user4=UNION()
user4.source()
user4.amount()
user4.bank()
user4.pin()
user4.paymentprocess()
user4.paymentresult()

