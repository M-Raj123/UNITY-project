s=[];p=[];personal=[[]];
count=0
def admin():
    while(1):
        print("Username : ",end="");login=input().strip()
        print("Password : ",end="");passw=input().strip()
        if(login=="admin" and passw=="12345"):
            print("Hi Admin")
            while(1):
                print("What do you like to do")
                print("1. Create Event \r 2. Current Events ")
                q=int(input())
                if(q==1):
                    createevent();break
                elif(q==2):
                    currentevent();break
                else:
                    print("Enter a correct input")
        else:
            print("Invalid login")
def student():
    while(1):
        print("1. Login or 2. Sign up\r")
        r=int(input())
        if(r==1):
            print("Email Id :",end="");login=input().strip()
            print("Password :",end="");passw=input().strip()
            flag=0
            for i in range(count):
                if(s[i]==login and passw==p[i]):
                    print("Welcome,"+login);flag=1;break
            if(flag==1):
                break
            else:
                print("Invalid Email Id or password")
        elif(r==2):
            print("Enter your Email Id :",end=" ");email=input().strip()
            if(email in s):
                print("Email Id already exists")
            else:
                personal[count].append(email)
                print("Enter your First name :",end=" ");personal[count].append(input().strip());s.append(email)
                print("Enter your Last name :",end=" ");personal[count].append(input().strip())
                print("Enter your college name :",end=" ");personal[count].append(input().strip())
                print("Enter the passed out year :",end=" ");personal[count].append(input().strip())
                print("Enter password :");p.append(input().strip())
                print("User is created\r Now you can Login");count+=1
        else:
            print("Enter a correct input")
while(1):  
    print("1. Admin 2.Student")
    x=int(input())
    if(x==1):
        admin();break
    elif(x==2):
        student();break
    else:
        print("Invalid input")
