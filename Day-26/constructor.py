class Instagram:
    def __init__(self,username,password):#__init__is a special method this called automatically when object created
        self.username=username
        self.password=password
        print(f"welcome to instagram {self.username}")

kalyani=Instagram('kalyani','1234')
siva=Instagram('siva','1111111111111234')