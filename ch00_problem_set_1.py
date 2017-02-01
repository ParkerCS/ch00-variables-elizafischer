import math
#SECTION 1 - MATH OPERATORS AND VARIABLES (20PTS TOTAL)

#PROBLEM 1 (From Math Class to Code - 2pts)
print("Problem #1")

# Print the answer to the math question:
# 3(60x^2 + 3x/9) + 2x - 4/3(x) - sqrt(x)
# where x = 12.83
x = 12.83
your_answer = 3 * ((60 * (x**2) + (3 * (x)/9))  + (2*(x)) - (4/(3*(x))) - ( x ** 0.5 ))
print(your_answer)
print("")



#PROBLEM 2 (Set your alarm - 3pts)
print("Problem #2")
#You look at the clock and see that it is currently 1:00PM.
# You set an alarm to go off 728 hours later.
# At what time will the alarm go off? Write a program that prints the answer.
# Hint: for the best solution, you will need the modulo operator.
clock = 1
clock_time = str("1:00 PM" )
print(clock_time)
print("An alarm will go off 728 hours later than this time.")
time = 728//12
print(time)
time = time//12
print(time)
clock += time
print ("Alarm goes off at " + str(clock) +":00")

# Lee - Should go off at 9:00.  You took your origial time and did two floor operations which would always reduce it to 1 regardless of the time.  You could have taken the time after the first floor and added it to the current time (-1)


print("")

#PROBLEM 3 (Wholesale Books - 3pts)
print("Problem #3")
#The cover price of a book is $27.95, but bookstores get a 50 percent discount.
#Shipping costs $4 for the first copy and 75 cents for each additional copy.
# Calculate the total wholesale costs for 68 copies to the nearest penny.
book = 27.95
discount = 0.5
subtract = book * discount
print("Subtract = " + str(subtract))
book -= subtract
shipping = (68 - 1) * 0.75
print("Shipping = " + str(shipping))
total= book + shipping + 4
float(total)
total = (round(total, 2))
print("Total wholesale cost: $" + str(total))
print("")


#PROBLEM 4 (Dining Room Chairs - 3pts)
print("Problem #4")
# You purchase eight chairs for your dining room.
# You pay for the chairs plus sales tax at 9.5%
# Make a program that prints the amount to the nearest penny using the variables below
# Use the round(float, digits) function to get to nearest penny
chair_price = 189.99
tax_percent = 0.095
units = 8

chair_price_plustax = (chair_price * tax_percent) + chair_price
print("A chair costs about $" + str(chair_price_plustax) + " with tax")
float(chair_price_plustax)
total_chair =  chair_price_plustax * 8
float(total_chair)
total_chair = round(total_chair, 2)
print("8 chairs with tax costs $" + str(total_chair))
print("")


#PROBLEM 5 (Area of Circle - 3pts)
print("Problem #5")
# Write code that can compute the area of circle.
# Create variables for radius and pi (3.14159)
# The formula, in case you do not know, is radius times radius times pi.
# Print the outcome of your program as follows:
# The surface area of a circle with radius ... is ...
print("Circle area calculator!")
my_input = input("Write the radius of your choice:")
pi = math.pi
my_input = ((float(my_input) **2) * pi) # ERROR HERE CORRECTED
float(my_input)
my_input = round(my_input , 2)
print("The area of your circle is " + str(my_input))
print()

# Lee - You need to change it to a number before doing any calculations (-1)

#PROBLEM 6 (Coin counter - 4pts) (modulo and floor operators, save results and add together)
print("Problem #6")
# Write code that classifies a given amount of money (which you store in a variable named count),
# as greater monetary units. Your code lists the monetary equivalent in dollars, quarters,
# dimes, nickels, and pennies.
# Your program should report the maximum number of dollars that fit in the amount,
# then the maximum number of quarters that fit in the remainder after you subtract the dollars,
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters,
# and so on for nickels and pennies.
# The result is that you express the amount as the minimum number of coins needed.
count = 492.94
dollar_number = 492
quarter_number = 1,970
dime_number = 4,929
nickel_number = 9,858
penny_number = 49,294
print(str(dollar_number) + " dollars, " + str(quarter_number) +" quarters, " + str(dime_number) +" dimes, " + str(nickel_number) + " nickels and " + str(penny_number) + " pennies that can fit into $492.94.")

dollar = round(count // 1)
quarter = round((count - dollar) // 0.25)
dime = round((count - dollar - (quarter / 4)) // 0.10)
nickel = round((count - dollar - (quarter / 4) - (dime / 10)) //0.05)
penny = round((count - dollar - (quarter/4) - (dime / 10) - (nickel/ 20)) // 0.01)
print("There are " + str(dollar) + " dollars, "+ str(quarter) + " quarters, " + str(dime) + " dimes, " + str(nickel) + " nickels and " + str(penny) + " pennies.")

# Lee - Looks like you did a lot of work to get this answer.  You did not need the first part, but nice work.


print("")
#PROBLEM 7 (Variable Swap - 2pts)
print("Problem #7")
# Can you think of a way to swap the values of two variables that does not
# need a third variable as a temporary storage?
# In the code below, try to implement the swapping of the values of 'a' and 'b' without using a third variable.
# To help you out, the first step to do this is already given.
# You just need to add two more lines of code.
a = 17
b = 23
print( "a = "+ str(a), "and b = "+ str(b))
a += b # this is the first line to help you out
# add two more lines of code here to cause swapping of a and b
b = a -b
a -= b
print( "a =", a, "and b =", b)

