#super method(if u have same method both for parent and child 
# and if u want to imprt properties from parent to child  we are using super())
'''class whatsappv1():
    def status(self):
        print("you can upload status for 24hrs")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("you can add music and u can react")

a=whatsappv1()
a.status()
b=whatsappv2()
b.status()'''

#multiple inheritance(when we have multiple inheritance we have to use class method)
class whatsappv1():
    def status(self):
        print("you can upload status for 24hrs")

class whatsappv2():
    def status(self):
        print("you can add music and u can react")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you can add to the cross platform")
a=whatsappv3()
a.status()