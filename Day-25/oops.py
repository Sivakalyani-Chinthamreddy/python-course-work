'''class Amazon:
    pass

siva=Amazon()
kalyani=Amazon()'''

class flipkart():
    discount = 30
    @classmethod
    def updateddis(cls):
        cls.discount=40
        print("updated discount",cls.discount)

        '''@staticmethod
        def msg():
            print(f'{flipkart.dicscount} is going on grb the products----------')'''
    def info(self,name,phno,address):
        self.name=name
        self.phno=phno
        self.address=address
        print("welcome to flipkart ",self.name)
    @staticmethod
    def banner():
     print(f'{flipkart.discount} is going on grb the products----------')
siva=flipkart()
siva.info('siva',98765432,'hyd')
siva.updateddis()
siva.banner()



kalyani=flipkart()
kalyani.info('kalyani',4567890,'ap')
kalyani.updateddis()
kalyani.banner()


pavani=flipkart()
pavani.info('pavani',23456789,'ong')
pavani.updateddis()
pavani.banner()
