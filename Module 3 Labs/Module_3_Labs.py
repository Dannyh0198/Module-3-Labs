# SSgt Daniel Hayward. Module 3 Labs. 21/09/21

#3.1.1.4 LAB: Questions and answers
# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, 
# which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
n = int(input ("Input N:"))
print(n >= 100)

# 3.1.1.10 LAB: Comparison operators and conditional execution
# Spathiphyllum, more commonly known as a peace lily or white sail plant,  
# is one of the most popular indoor houseplants that filters out harmful toxins from the air.
# Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.
plant = (input("What houseplant do you have?: "))
if plant == "Spathinphyllum":
    print ("Spathiphyllum is the best plant ever!")

# 3.1.1.11 LAB: Essentials of the if-else statement
# Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people.
# The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short)
# had to be paid once a year, and was evaluated using the following rule:
# if the citizen's income was not higher than 85,528 thalers, 
# the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Note: this happy country never returns money to its citizens. 
# If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.
income = float(input("Enter the annual income: "))
if income <= 85528:
    tax = ((income*0.18)-556.2)
else:
    tax = 14839.2 + ((income-85528)*0.32)
if tax <= 0:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#3.1.1.12 LAB: Essentials of the if-elif-else statement
# As you surely know, due to some astronomical reasons, years may be leap or common. 
# The former are 366 days long, while the latter are 365 days long.
# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year
# It would be good to verify if the entered year falls into the Gregorian era, 
# and output a warning otherwise: Not within the Gregorian calendar period
year = int(input("Enter a year: "))
if year <1582:
    year = ("Not within the Gregorian calendar period")
elif year % 4 != 0 :
    year = ("Common Year")
elif year % 100 != 0:
    year = ("Leap year")
elif year % 400 != 0:
    year = ("Common Year")
else: 
    year = ("Leap year")
print (year)