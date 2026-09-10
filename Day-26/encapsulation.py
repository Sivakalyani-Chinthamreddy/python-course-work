'''class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password#provate
        self._post=[]#protected

    def getpassword(self):
        return self.__password
    @property
    def accesspost(self):
        return self._post

kalyani=Instagram('kalyani','1234')

print(kalyani.username)
print(kalyani.getpassword())
print(kalyani.accesspost)'''

#for updating
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password#provate
        self._post=[]#protected

    def getpassword(self):
        return self.__password
    def updatepass(self,newpassword):
        self.__password=newpassword
    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)



kalyani=Instagram('kalyani','1234')
print(kalyani.username)
print(kalyani.getpassword())
print(kalyani.accesspost)

kalyani.username='kalyani_123'
print(kalyani.username)

kalyani.updatepass('kalyani@123')
print(kalyani.getpassword())


kalyani.accesspost='python img'
kalyani.accesspost='flask'
kalyani.accesspost='project'
print(kalyani.accesspost)

