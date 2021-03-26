s=[];p=[];personal=[];pc=[]
count=0;event=[];event_count=0

def createevent(event_count):
    e=[]
    print("Which type you want to create ");
    print("Enter name of the Event :",end="");e.append(input().strip())
    print("Enter Organiser name :",end="");e.append(input().strip())
    print("About the Event :",end="");e.append(input())
    print("Venue of the Event :",end="");e.append(input().strip())
    print("No of Rooms Allocated :",end="");e.append(int(input()))
    print("Date and Time of the event :");e.append(input().strip())
    print("Food Available :",end="");e.append(input().strip())
    if(e[6].lower()=="yes"):
        print("Food that can be afford :",end="");e.append(input().split())
    print("Event created")
    event.append(e)

def currentevent():
    for i in range(len(event)):
        if(len(event[i])==0):
            break
        else:
            print(i+1,event[i][0])
    print("To know the details select any one number: ");
    w=oneevent()

def oneevent():
    f=int(input())
    print("Event name : ",event[f-1][0])
    print("Organiser : ",event[f-1][1])
    print("Description : ",event[f-1][2])
    print("Venue : ",event[f-1][3])
    print("Rooms Remaining : ",event[f-1][4])
    print("Date and Time of the event : ",event[f-1][5])
    print("Food Available : ",event[f-1][6])
    if((event[f-1][6]).lower()=="yes"):
        print("Food offered : ",*event[f-1][7])
    return f-1

def admin():
    while(1):
        print("Username : ",end="");login=input().strip()
        print("Password : ",end="");passw=input().strip()
        if(login=="admin" and passw=="12345"):
            print("Hi Admin")
            while(1):
                print("What do you like to do")
                print("1. Create Event 2. Current Events 3.Back")
                q=int(input())
                if(q==1):
                    createevent(event_count);break
                elif(q==2):
                    currentevent();break
                    break;
                else:
                    print("Enter a correct input")
            return 0
        else:
            print("Invalid login")

def register(q):
    print("Enter the number of the event that u want to register : ")
    reg=oneevent();p=[]
    pc.append(personal[q][0]);pc.append(reg)
    if(event[reg][4]!=0):
        print("If you want room 1.Yes 2.no")
        if(int(input())==1):
            print("Room is allocated");event[reg][4]-=1;pc.append(1)
        else:
            pc.append(0)
    else:
        pc.append(0)
    if((event[reg][6]).lower()=="yes"):
        print("If you want food 1.Yes 2.no")
        if(int(input())==1):
            for i in range(len(event[reg][7])):
                print(i+1,event[reg][7][i])
                print("If you want? 1.Yes 2.No")
                if(int(input())==1):
                    p.append(i)
            print("Food is allocated");pc.append(p)
        else:
            pc.append(p)
    else:
        pc.append(p)
    print("Registration Successful")
           
def student(count):
    while(1):
        print("1. Login or 2. Sign up")
        r=int(input())
        if(r==1):
            print("Email Id :",end="");login=input().strip()
            print("Password :",end="");passw=input().strip()
            flag=0
            for i in range(len(s)):
                if(s[i]==login and passw==p[i]):
                    print("Welcome,"+login);flag=i+1;break
            if(flag!=0):
                currentevent();
                print("If U want to register in a event \r 1. Register 2.Exit")
                if(int(input())==1):
                    register(flag-1);
                break
            else:
                print("Invalid Email Id or password")
            return 0;
        elif(r==2):
            t=[]
            print("Enter your Email Id :",end=" ");email=input().strip()
            if(email in s):
                print("Email Id already exists")
            else:
                t.append(email);s.append(email)
                print("Enter your First name :",end=" ");t.append(input().strip());
                print("Enter your Last name :",end=" ");t.append(input().strip())
                print("Enter your college name :",end=" ");t.append(input().strip())
                print("Enter the passed out year :",end=" ");t.append(input().strip())
                print("Enter password :");p.append(input().strip())
                print("User is created\r Now you can Login");count+=1
                personal.append(t)
            return 0;
        else:
            print("Enter a correct input")
while(1):  
    print("1. Admin 2.Student 3.Exit")
    x=int(input())
    if(x==1):
        admin()
    elif(x==2):
        student(count)
    elif(x==3):
        exit()
    else:
        print("Invalid input")
