import logic as lg
if lg.login():
    while True:

        lg.menu()
        ch=input("Enter the choice:").upper()
        if ch=='C':
            lg.checkbalance()
        elif ch=='D':
            lg.deposite()
        elif ch=='W':
            lg.withdraw()
        elif ch=='V':
            lg.viewtranscation()
        elif ch=='E':
            print('-----------------Thankyou,visit again-------------------------')
            break
        else:
            print("please enter the valid choice")



