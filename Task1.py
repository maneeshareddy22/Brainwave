user=['a','b','c','d']
mails=["a@gmail.com","b@gmail.com","c@gmail.com","d@gmail.com"]
phnno=["9848485773","3859274644","2937593758","9346226370"]
pas=["123","456","789","101"]
acc=[100,200,300,400]
def signup():
    name=input("Enter username: ")
    passwor=input("Enter password:")
    confirmpassword=input("Enter confirm password: ")
    mail=input("Enter mailid: ")
    phonenum=input("Enter phone number: ")
    amount=int(input("Enter deposit amount: "))
    user.append(name)
    mails.append(mail)
    pas.append(passwor)
    phnno.append(phonenum)
    acc.append(amount)
    return name,passwor,confirmpassword,mail,phonenum,amount
while True:
    mch=input("do you want to login or signup: ")
    if(mch=="login"):
        print(user)
        p=input("Enter your name: ")
        i=user.index(p)
        if p in user:
            password=input("Enter your password: ")
            if(password==pas[i]):
                print("login successful")
                while True:
                    ch=int(input("Enter your choice 1:withdraw 2:deposit 3:checkbalance 4:logout: "))
                    if(ch==1):
                        print("withdraw")
                        wa=int(input("Enter how much ammount you want to withdraw: "))
                        if(wa>acc[i]):
                            print("you don't have enough balance in your account")
                        else:
                            acc[i]=acc[i]-wa
                    elif(ch==2):
                        print("deposit")
                        am=int(input("How much you want to deposit: "))
                        acc[i]=acc[i]+am
                    elif(ch==3):
                        print("Checkbalance")
                        print (acc[i])
                    elif(ch==4):
                        print("logout")
                        break
                    else:
                        print("choose correct option")

            else:
                print("please enter valid password")
        else:
            print("Not eligible")
    elif(mch=="signup"):
        signup()
    else:
        print("choose correct option")
