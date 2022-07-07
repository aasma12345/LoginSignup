def register():
    db=open("login.txt",mode="r")
    username=input("create username: ")
    password=input("create password: ")
    password1=input("create password1: ")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d, f))
   
    
    if password != password1:
        print("password doesnt match ")
        register()
    else:
        if len(password)<=6:
            print("password too short restart: ")
            register()
        elif username in d:
            print("username exits")
            register()
        else:
            a=open("login.txt","a")
            a.write(username+", "+password+"\n")
            print("successfull")

def access():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    db=open("login.txt",mode="r")
    if not len(username or password)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d, f))
        try:
            if data[username]:
                try:
                    if password==data[username]:
                        print("login successfull")
                        print("Hi,",username)
                    else:
                        print("password or username incorrect")
                except:
                    print("incorecct password or username")
            else:
                print("username or password  dosent exits")
        except:
            print("username or password doesnt exits")
    else:
        print("please enter a value")
def home(option=None):
    option=input("Login | signup: ")
    if option=="Login":
        access()
    elif option=="signup":
        register()
    else:
        print("please Enter an option")
home()


    
