data={
    123456:{'name':"kalyani",'pin':1234,'balance':5000,'history':[]},
    123467:{'name':"kalyani",'pin':123,'balance':5000,'history':[]},
    123458:{'name':"kalyani",'pin':125,'balance':5000,'history':[]}
}

def login():
    global acc_num
    acc_num=int(input("Enter account number:"))
    pin = int(input("Enter pin:"))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("login succesfully")
        return True
    else:
        print("invalid login")
        return False

def menu():
    print(f"welcome to ATM,{data[acc_num]['name']}")
    print('[C]heck balance')
    print('[D]eposite')
    print('[W]ithdraw')
    print('[V]iew transcation')
    print('[E]xit')

def checkbalance():

    print(f"Hello", data[acc_num]['name'])
    print(f"current balance:",data[acc_num]['balance'])

def deposite():
    amount=int(input("Enetr the amount to deposite: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f'{amount} is deposited')
    print(f"{amount} is deposited successfully")
    checkbalance()

def withdraw():
    amount=int(input("Enter the amount to withdraw: "))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f'{amount} is withraw')
        print(f"{amount} is withdraw successfully")
        checkbalance()
    else:
        print("Insufficent funds")

def viewtranscation():
    if data[acc_num]['history']:
        print("-----------trasction history------------")
        for i in data[acc_num]['history']:
            print(i)
        else:
            print('----------end of history------------')
    else:
        print("No transction history")



    

