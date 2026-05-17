#prog01 Check employee promotion eligibility
exper,sal=map(int,input("enter age,exper,sal").split())
if exper >5 and sal>50000:
    print("eligible for promotion")
else:
    print("not eligible")

#prog02 Check student distinction category
marks1,marks2,marks3=map(int,input("enter marks").split())
if marks1>=75 and marks2>=75 and marks3>=75:
    print("distinction")
elif marks1>=35 and marks2>=35 and marks3>=35:
    print("pass")
else:
    print("fail")

#prog03 Check website login system
user=input("enter username")
passw=int(input("enter password"))
otp=int(input("enter otp"))
if user=="John" and passw==2006 and otp==4611:
    print("login succesfull")
else:
    print("login failed")

user=["john","renu","sara"]
user2=["renu","sara"]
if user2[0] in user and user2[1] in user:
    print("login successfull")
else:
    print("not login")

#prog04 Check internet package category
speed,data,rd=map(int,input("enter speed,data,rd").split())
if speed>100 and data>500 and rd>20:
                      print("premium pla")
elif speed>20 and data>200 and rd>10:
                     print("standard paln")
else:
                     print("basic plan")

#prog05 Check job eligibility
degree=input("enter degree")
experience,age=map(int,input("enter experience,age").split())
if degree=="yes" and experience>=2 and age>21:
    print("eligible")
else:
    print("not eligible")
    
#prog06 Check flight boarding eligibility
rooms=int(input("enter number of rooms"))
days=int(input("enter number of days"))
budget=int(input("enter budget"))
if rooms>=2 and days>=3 and budget>5000:
    print("luxury booking")
elif rooms>=1 and days>=2 and budget>2000:
    print("standard booking")
else:
    print("budget booking  ")

#prog07 Check scholarship eligibility
marks = int(input("Enter Marks : "))
attendance = int(input("Enter Attendance : "))
if marks >= 35 and attendance >= 70:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")

#prog08 8. Check mobile unlock system
pin = int(input("Enter pin"))
face = input("Face Detected")
if pin == 1234 and face == "yes":
              print("Mobile Unlocked")
else:
            print("Access Denied")

#prog09  Check hotel booking eligibility
rooms = int(input("Enter Number of Rooms : "))
days = int(input("Enter Number of Days : "))
budget = int(input("Enter Budget : "))
if rooms >= 2 and days >= 3 and budget > 50000:
        print("Luxury Booking")
elif rooms >= 1 and budget > 20000:
        print("Standard Booking")
else:
        print("Budget Booking")

#prog10  Check exam topper category
sub1 = int(input("Enter Subject 1 Marks : "))
sub2 = int(input("Enter Subject 2 Marks : "))
sub3 = int(input("Enter Subject 3 Marks : "))
total = sub1 + sub2 + sub3
if total >=600:
       print("Topper")
elif total >=300:
       print("Good")
else:
       print("Fail")

#prog11. Check gym membership category
age = int(input("Enter Age : "))
weight = int(input("Enter Weight : "))
height = float(input("Enter Height : "))
if age > 21 and weight > 55 and height > 5:
         print("category good")
elif age > 18 and weight > 40:
         print("category need improvement")
else:
         print("category bad")

#prog12 Check traffic penalty system
helmet=input("helmet satus:")
lincence=input("licence status:")
spedd=int(input("enter speed:"))
if helmet=="yes" and lincence=="yes" and speed <80:
    print("no fine")
elif speed >100:
    print("fine")
else:
    print("low fine")
    
#prog13  Check movie ticket pricing
person_age = int(input("Enter your age"))
week_day = input("Enter today")
card = input("Member card (yes/no): ")
if person_age < 18 and card == "yes" and week_day == "Sunday":
    print("Half ticket discount")
elif card == "yes":
    print("Quarter discount")
else:
    print("No offer")

#prog14 Check weather alert system
temp= int(input("Temperature: "))
if temp> 40 :
    print("High heat warning")
else:
    print("Weather normal")

#prog15 Check online shopping offer
pur=int(input("enter purchase amount"))
coupon,premium=input("enter coupon and premiun status:").split()
if pur>1000 and coupon=="yes" and premium=="yes":
    print(" max discount")
elif pur>500 and coupon=="yes":
    print("medium discount")
else:
    print("no discount")

#prog16  Check server room access
card_status = input("ID available")
scan = input("Fingerprint ok")
if card_status == "yes" and scan == "yes":
    print("Welcome inside")
else:
    print("Entry denied")

#prog17  Check sports team selection
age=int(input("enter age"))
skill=int(input("enter skill level"))
if age>18 and skill>7:
    print("selected for team")
else:
    print("not selected for team")

#prog18 Check laptop purchase recommendation
budget=int(input("enter budget"))
ram=int(input("enter ram size"))
if budget>50000 and ram>16:
    print("high end laptop")
elif budget>30000 and ram>8:
    print("mid range laptop")
else:
    print("budget laptop")

#prog19 Check bank loan approval
sal=int(input("enter salary"))
exp=int(input("enter experience"))
if sal>50000 and exp>5:
    print("loan approved")  
else:
    print("loan not approved")

#prog20 Check smart home security system
camera=input("enter camera status")
alarm=input("enter alarm status")
if camera=="yes" and alarm=="yes":
    print("home secure")
else:
    print("home not secure")



