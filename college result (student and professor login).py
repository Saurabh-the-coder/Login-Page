# WAP to take login as student or professor.. take input of student marks from professor and student can view his result
def Login_p():
    print("Welcome to Staff login")
    usr=(input("Enter your user name: "))
    pwd=(input("Enter your password: "))
    if(usr=='Aaryan' and pwd=='Lexis'):
        Welcome_p()
   
    else:
        print("Wrong credentials or invalid input, please try again")
        exit
def Login_s():
    usr=(input("Enter your user name: "))
    pwd=(input("Enter your password: "))
    if(usr=='student' and pwd=='student'):
        Welcome_s()
    else:
        print("Wrong credentials or invalid input\n* Please contact Admin Department for your Credentials")
        exit

def Welcome_p():
    print("Welcome to Lexis Education Club Staff Section\n")
    print("1. Enter student record\n2. View your profile\n3. Logout")
    switch=int(input("Enter your choice number: "))
    if switch==1:
        Switch_p1()
    elif switch==2:
        Switch_p2()
    elif switch==3:
        Switch_p3()
    else:
        print("Please enter valid input")
        Welcome_p()

def Welcome_s():
    print("Welcome to Lexis Education Club Student Section\n")
    print("1. Check your result \n2. View your profile\n3. Logout")
    switch=int(input("Enter your choice number: "))
    if switch==1:
        Switch_s1()
    elif switch==2:
        Switch_s2() 
    elif switch==3:
        Switch_s3()
    else:
        print("Please enter valid input")
        Welcome_s()
    
def Switch_p1():
    name=input("Enter the name of the student: ")
    rollno=int(input("Assign the roll number of the student: "))
    marks=int(input("Enter student marks: "))
    print("Data saved")
    switch=int(input("Enter 1 to go back to the main menu or Enter 2 to enter more data, Enter 3 to Logout: "))
    if switch==1:
        Welcome_p()
    elif switch==2:
        Switch_p1()
    elif switch==3:
        Login_p()
    else:
        print("invalid entry")
        Welcome_p()
     
def Switch_p2():
    print("1. Name: Aaryan\n2.Designation: CEO\n3. Go back\n")
    switch= input("Please enter any key to go to welcomne page")
    Welcome_p()

def Switch_p3():
    Login_p()

def Switch_s1():
    print("You passed with Merit")
    switch=input("enter any key to go back to the Welcome screen: ")
    Welcome_s()

def Switch_s2():
    print("1. Name: Aaryan\n2. Degree: MSc in International Business and Finance\n3. Go back")
    switch=input("Press any key to go back to the welcome screen: ")
    Welcome_s()

def Switch_s3():
    Login_s()

login=input("If you are a student enter 's', if you are a professor, enter'p', or enter exit to exit this program: ")
if login=='p':
    Login_p()
    """if(usr=='Aaryan' and pwd=='Lexis'):
        Welcome_p()
        if switch==1:
            Switch_p1()
        elif switch==2:
            Switch_p2()
        elif switch==3:
            Switch_p3()
        else:
            print("Please enter valid input")
            Welcome_p()
    else:
        print("Wrong credentials or invalid entry")
        Login_lexis()"""
elif login=='s':
    Login_s()

elif login=='exit':
    exit
""" if(usr=='student' and pwd=='studentlexis'):
        Welcome_s()    
        if switch==1:
            Switch_s1()
        elif switch==2:
            Switch_s2() 
        elif switch==3:
            Switch_s3()
        else:
            print("Please enter valid input")
else:
    print("Please enter valid input")
    Login_lexis()
"""