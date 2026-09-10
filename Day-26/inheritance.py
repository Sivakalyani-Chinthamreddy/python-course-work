#single inheritance
#parent class
'''class whatsapp1():
    def message(self):
        print("you can meaasage")
lohitha=whatsapp1()
lohitha.message()

#child class
class whatsapp2(whatsapp1):#to call properties from parent to child we just need to insret parent calss name in  to child class
    def status(self):
        print("u can upload a status up to 24hrs")
kalyani=whatsapp2()
kalyani.status()
kalyani.message()

#multilevel inheritance(single child ,single grand child and single parent)
#parent class
class whatsapp1():
    def message(self):
        print("you can meaasage")
lohitha=whatsapp1()
lohitha.message()

#child class
class whatsapp2(whatsapp1):#to call properties from parent to child we just need to insret parent calss name in  to child class
    def status(self):
        print("u can upload a status up to 24hrs")
kalyani=whatsapp2()
kalyani.status()
kalyani.message()

class whatsapp3(whatsapp2):#if u want to inherit peoprties from paren and child to parent just give child class name to grand child class
    def groups(self):
        print("you can create a group and talk with so many pepole at same time")
siva=whatsapp3()
siva.groups()
siva.message()
siva.status()

#multilevel inheritance(one child multiple parents)/hybrib inheritance(if any two inheritance are there they are called hybribd inheritance)
class whatsapp1():
    def message(self):
        print("you can meaasage")
lohitha=whatsapp1()
lohitha.message()

#child class
class whatsapp2(whatsapp1):#to call properties from parent to child we just need to insret parent calss name in  to child class
    def status(self):
        print("u can upload a status up to 24hrs")
kalyani=whatsapp2()
kalyani.status()
kalyani.message()

class whatsapp3():#if u want to inherit peoprties from paren and child to parent just give child class name to grand child class
    def groups(self):
        print("you can create a group and talk with so many pepole at same time")
siva=whatsapp3()
siva.groups()
#siva.message()
#siva.status()

class whatsapp4():
    def communities(self):
        print("you combine multiple groups")

class whatsapp5(whatsapp2,whatsapp3,whatsapp4):
    def channels(self):
        print("you can post to huge people ")
pavani=whatsapp5()
pavani.channels()
pavani.communities()
pavani.message()
pavani.status()
pavani.groups()'''

#heirarical inheritance(single parent multiple childs)
class whatsapp1():
    def message(self):
        print("you can meaasage")

class whatsapp2(whatsapp1):#to call properties from parent to child we just need to insret parent calss name in  to child class
    def status(self):
        print("u can upload a status up to 24hrs")

class whatsapp3(whatsapp1):#if u want to inherit peoprties from paren and child to parent just give child class name to grand child class
    def groups(self):
        print("you can create a group and talk with so many pepole at same time")

class whatsapp4(whatsapp1):
    def communities(self):
        print("you combine multiple groups")

class whatsapp5(whatsapp1):
    def channels(self):
        print("you can post")
siva=whatsapp1()
siva.message()
kalyani=whatsapp2()
kalyani.status()
pavani=whatsapp3()
pavani.groups()
monika=whatsapp4()
monika.communities()
priya=whatsapp5
priya.channels()