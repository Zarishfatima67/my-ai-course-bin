#Question no 1
#Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
#(Celsius * 9/5) + 32) 

Celsius=int(input("Enter temperature in Celsius:"))
Fahrenheit=(Celsius*9/5+32)
print('Tempeature in Fahrenhiet:',Fahrenheit)

#Question 2: 
#Calculate Area of a Rectangle 
length=float(input('Enter the Length:'))
width=float(input('Enter the width:'))
Area=length*width
print('area of rectangle is:',Area)

#Question 3: 
#Calculate Compound Interest 
#Use the formula: 
#CI = P * (1 + R/100)**T - P 
#Where P = principal, R = rate, T = time

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time: "))
CI = P * (1 + R / 100) ** T - P
print("Compound Interest =", CI)



#Question 4: 
#Perimeter of a Rectangle - Take length and width as input and calculate the perimeter.
length=float(input('Enter the Length:'))
width=float(input('Enter the width:'))
print(type(length))
print(type(width))
#caluate the peremiter
perimeter=2*(length+width)
print('perimeter of the rectangle:', perimeter)


#Question 5: 
#Average of Three Numbers - Input three numbers and print their average. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average of the three numbers is:", average)

#Question 6: 
#Square and Cube of a Number - Ask the user for a number and display its square and cube. 
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square =", square)
print("Cube =", cube)

#Question 7: 
#Distribute Items Equally - You have n candies and k students. 
#Write a program to find: 
#how many candies each student gets 
#how many are left
n = int(input("Enter number of candies: "))
k = int(input("Enter number of students: "))
each_student = n // k
left_candies = n % k
print("Each student gets =", each_student)
print("Candies left =", left_candies)

#Question 8: 
#Calculate Profit or Loss 
#Input cost price and selling price. Display either: 
#Profit and amount, or 
#Loss and amount, or 
#No Profit No Loss


costprice = float(input("Enter Cost Price: "))
sellingprice = float(input("Enter Selling Price: "))
if sellingprice > costprice:
    profit = sellingprice - costprice
    print("Profit =", profit)
elif costprice > sellingprice:
    loss = costprice - sellingprice
    print("Loss =", loss)

else:
    print("No Profit No Loss")


#Question 9: 
#Total Marks and Percentage 
#Input marks of 5 subjects. Print: 
#Total marks 
#Percentage 
#Average 

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100
average = total / 5
print("Total Marks =", total)
print("Percentage =", percentage)

#Question 10: 
#Salary Calculator 
#Input basic salary. Calculate: 
 #HRA = 20% of basic 
 #DA = 15% of basic 
#Total Salary = Basic + HRA + DA

basicsalary = float(input("Enter Basic Salary: "))
HRA = 0.20 * basicsalary
DA = 0.15 * basicsalary
totalsalary = basicsalary + HRA + DA
print("HRA =", HRA)
print("DA =", DA)
print("Total Salary =", totalsalary)

#Question 11: 
#Age in Months and Days 
#Input your age in years. Calculate and print age in: 
# Months 
#Days (approximate)

ageyears = int(input("Enter your age in years: "))
months = ageyears * 12
days = ageyears * 365   

print("Age in Months =", months)
print("Age in Days =", days)

#Question 12: 
#Currency Converter (USD to PKR) 
#Input amount in USD. Convert using a fixed exchange rate.

exchange_rate = 278 
usd = float(input("Enter amount in USD: "))
pkr = usd * exchange_rate
print("Amount in PKR =", pkr)

#Question 13: 
#Sum of First N Natural Numbers 
#Input a number n, calculate sum of first n natural numbers. 
#Formula: sum = n * (n + 1) / 2

n = int(input("Enter a number: "))
sum = n * (n + 1) / 2
print("Sum of first", n, "natural numbers =", sum)


#Question 14: 
#Percentage of Correct Answers 
#Input total questions and correct answers, and calculate the percentage score.

totalquestions = int(input("Enter total number of questions: "))
correctanswers = int(input("Enter number of correct answers: "))
percentage = (correctanswers / totalquestions) * 100
print("Percentage Score =", percentage, "%")

#Question 15: 
#Speed, Distance, and Time 
#Input distance and time, and calculate speed.

distance = float(input("Enter distance: "))
time = float(input("Enter time: "))
speed = distance / time
print("Speed =", speed)

#Question 16: 
#Calculate Body Mass Index (BMI) 
#Input weight (kg) and height (m), then calculate: 
#BMI = weight / (height ** 2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

BMI = weight / (height ** 2)
print("BMI =", BMI)

#Question 17: 
#Convert Minutes to Hours and Minutes 
#Input number of minutes and convert to hours and remaining minutes. 
#Example: 130 minutes → 2 hours 10 minutes

minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(minutes, "minutes =", hours, "hours", remaining_minutes, "minutes")
