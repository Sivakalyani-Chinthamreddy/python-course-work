#polymorphisam
#method overriding(means changing printing sattements or changing headings in class)
class Hotstar:
    def __init__(self,name):
        print(f"--------welcome to the hotstart {name}--------------")
    def auth(self):
        print("you can login")
    def dashboard(self):
        print("you can see dashboard")
    def search(self):
        print("ypu can search")
    def history(self):
        print("you can see the history")
    def playclontrollers(self):
        print("you can pause,move")
    def ads(self):
        print("you get adds")
    def devices(self):
        print("limited devices only")
    def access(self):
        print("you can access only limited things")
    def download(self):
        print("you cant downoald")
user1=Hotstar('kalyani')
user1.auth()
user1.dashboard()
user1.search()
user1.history()
user1.playclontrollers()
user1.ads()
user1.devices()
user1.access()
user1.download()


class PremiumHotstar:
    def __init__(self,name):
        print(f"--------welcome to the hotstart {name}--------------")
    def auth(self):
        print("you can login")
    def dashboard(self):
        print("you can see dashboard")
    def search(self):
        print("ypu can search")
    def history(self):
        print("you can see the history")
    def playclontrollers(self):
        print("you can pause,move")
    def ads(self):
        print("you dont get  adds")
    def devices(self):
        print("multiple devices")
    def access(self):
        print("you can access  unlimited things")
    def download(self):
        print("you can downoald")
user2=PremiumHotstar('siva kalyani')
user2.auth()
user2.dashboard()
user2.search()
user2.history()
user2.playclontrollers()
user2.ads()
user2.devices()
user2.access()
user2.download()
