#prog01 Check whether employee age is above 21 and salary is above 30000
age,sal=map(int,input("enter vage and sal").split())
if age>21 and sal>30000:
      print("eligible")
else:
        print("not eligible")   
        

age,sal=map(int,input("enter vage and sal").split())
print(age >21 and sal>30000)

#prog02 Check whether student passed in two subjects
mark1,mark2=map(int,input("enter marks").split())
if mark1>35 and mark2>35:
    print("pass")
else:
    print("fail")
    
#prog03 Check whether entered value is between two ranges
num=int(input("enter number"))
max,min=map(int,input("enter numbers").split())
if num>min and num<max:
    print("limit")
else:
    print("not")
    
#prog04 Check whether username and password are correct
orgpass=101
orguser="renu"
passw=int(input("enter password"))
name=input("enter userna")
if orgpass==passw and orguser==name:
    print("correct")
else:
    print("not")
    
#prog05  Check whether temperature is within safe range
temp,lower,upper=map(float,input("enter temp").split())
if temp<lower and temp>upper:
    print("in range")
else:
    print("not in range")
    
#prog06 Check whether both entered numbers are even
num=int(input("enter number"))
num1=int(input("enter number"))
if num%2==0 and num1 %2==0:
    print("even")
else:
    print("odd")

#prog07 Check whether both entered numbers are positive
num1,num2=map(int,input("enter numbers").split())
if num1>0 and num2>0:
    print("+ve")
else:
    print("-ve")
    
#prog08 Check whether person is eligible for driving
age=int(input("enter age"))
licence=input("enter licence")
if age>18 and licence=="yes":
    print("eligible")
else:
    print("not eligible")
    
#prog09 Check whether project progress meets deadline condition
day,prog=map(int,input("enter day and prog").split())
if day>5 and prog>75:
    print("eligible")
else:
    print("not eligible")
    
#prog10 Check whether attendance and marks satisfy eligibility
atten,maeks=map(int,input("enter atten and marks").split())
if atten>75 and maeks>35:
    print("pass")   
else:
    print("fail")
    
#prog11 Check whether entered role is Admin or Manager
role=input("enter role")
if role=='admin' or role=='manager':
    print("accept")
else:
    print("reject")
    
#prog12 Check whether student scored distinction in any one subject
a,b,c=map(int,input("enter numbers").split())
if a>70 or b>70 or c>70:
    print("pass")
else:
    print("fail")
    
#prog13 Check whether entered day is weekend
day=input("enter day")
if day=="sunday" or day=="saturday":
    print("weekend")
else:
    print(" not a weekday")

#prog14 Check whether selected category matches two possible values
cat=input("enter category")
if cat=="A" or cat=="B":
    print("valid category")
else:
    print("invalid category")

#prog15 Check whether salary or experience satisfies requirement
sal,exp=map(int,input("enter sal and exp").split())
if sal >30000 or exp>3:
    print("eligible")
else:
    print("not eligible")

#prog16 Check whether temperature is extremely low or high
temp,lower,upper=map(float,input("enter temp").split())
if temp<lower or temp>upper:
    print("not in range")
else:
    print("in range")
#prog17 Check whether entered username matches predefined values
user=input("enter username")
if user=="admin" or user=="manager":
    print("login successfull")
else:
    print("login failed")
#prog18  Check whether selected option belongs to given choices
option = input("Enter option: ")
if option == "A" or option == "B" :
    print("Option")
else:
    print("no")

#prog19 Check whether entered city matches allowed cities
city = input("Enter city: ")
if city == "Hyderabad" or city == "Chennai" or city == "Delhi":
    print("City allowed")
else:
    print("City not allowed")

#prog20 Check whether entered number matches predefined valuesinput("Enter number: "))
if num == 5 or num==10:
    print("Number matched")
else:
    print("Number not matched")

#prog21 Check whether user is not admin
user=input("enter name")
if not user=="admin":
    print("not an admin")
else:
    print("admin")
    
#prog22 Check whether entered number is not positiveinput("enter number"))
if not num>0:
    print("not postive")
else:
    print("postive")

#prog23 Check whether entered value is not empty
num=input("enter number")
if not num=="":
    print("not emputy")
else:
    print("empty") 

#prog24  Check whether file is not available
file=input("enter file name")
if not file:
    print("file not available")
else:
    print("file available")
    
#prog25 Check whether employee is not active
active=False
if not active:
    print("active")
else:
    print("not active")

#prog26  Check whether project status is not completed
project=input("enter project name")
if not project=="No":
    print("project assigned")
else:
    print("project not assigned")
    
#prog27  Check whether password is not correct
password = input("Enter password")
if not password == "python123":
    print("Password is not correct")
else:
    print("Password is correct")  

#prog28  Check whether temperature is not safe
temp = int(input("Enter temperature: "))
if not (temp >= 20 and temp <= 30):
    print("Temperature is not safe")
else:
    print("Temperature is safe")

#prog29 Check whether selected option is not allowed
option = input("Enter option: ")
if not option== "A":
    print("Selected option is not allowed")
else:
    print("Selected option is allowed")

#prog30  Check whether marks are not passing marks
marks = int(input("Enter marks: "))
if not (marks >= 35):
    print("Not passing marks")
else:
    print("Passing marks")