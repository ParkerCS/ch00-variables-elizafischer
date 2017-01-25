import math
#SECTION 1 - MATH OPERATORS AND VARIABLES (20PTS TOTAL)

#PROBLEM 1 (From Math Class to Code - 2pts)

# Print the answer to the math question:
# 3(60x^2 + 3x/9) + 2x - 4/3(x) - sqrt(x)
# where x = 12.83
x = 12.83
your_answer = 3 * ((60 * (x**2) + (3 * (x)/9))  + (2*(x)) - (4/(3*(x))) - ( x ** 0.5 ))
print(your_answer)
print("")


#PROBLEM 2 (Set your alarm - 3pts)
#You look at the clock and see that it is currently 1:00PM.
# You set an alarm to go off 728 hours later.
# At what time will the alarm go off? Write a program that prints the answer.
# Hint: for the best solution, you will need the modulo operator.
clock = 1
clock_time = str("1:00 PM" )
print(clock_time)
print("An alarm will go off 728 hours later than this time.")
time = 728//12
time = time//12
clock += time
print ("Alarm goes off at " + str(clock) +":00")



print("")

#PROBLEM 3 (Wholesale Books - 3pts)
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
# You purchase eight chairs for your dining room.
# You pay for the chairs plus sales tax at 9.5%
# Make a program that prints the amount to the nearest penny using the variables below
# Use the round(float, digits) function to get to nearest penny
chair_price = 189.99
tax_percent = 0.095
units = 8

chair_price_plustax = (chair_price * tax_percent) + chair_price
print(chair_price_plustax)

#PROBLEM 5 (Area of Circle - 3pts)
# Write code that can compute the area of circle.
# Create variables for radius and pi (3.14159)
# The formula, in case you do not know, is radius times radius times pi.
# Print the outcome of your program as follows:
# The surface area of a circle with radius ... is ...

#PROBLEM 6 (Coin counter - 4pts) (modulo and floor operators, save results and add together)
# Write code that classifies a given amount of money (which you store in a variable named count),
# as greater monetary units. Your code lists the monetary equivalent in dollars, quarters,
# dimes, nickels, and pennies.
# Your program should report the maximum number of dollars that fit in the amount,
# then the maximum number of quarters that fit in the remainder after you subtract the dollars,
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters,
# and so on for nickels and pennies.
# The result is that you express the amount as the minimum number of coins needed.


#PROBLEM 7 (Variable Swap - 2pts)
# Can you think of a way to swap the values of two variables that does not
# need a third variable as a temporary storage?
# In the code below, try to implement the swapping of the values of 'a' and 'b' without using a third variable.
# To help you out, the first step to do this is already given.
# You just need to add two more lines of code.

a = 17
b = 23
print( "a =", a, "and b =", b)
a += b # this is the first line to help you out
# add two more lines of code here to cause swapping of a and b
print( "a =", a, "and b =", b)