
import math
print(5//2)
print(13%3)
print(8**0.5)
print("")

pi = math.pi
print(pi)
print(math.cos(0.5))
print("")


print(round(5.67,1))

#print statements, multiple items
print(4,3,5,6, "Score:" + str(300))
print("hello", end= " ")
print("world")
print("")



# input function
#my_input = input("Write a number:")
#print(int(my_input) + 3)

print("hello".upper())
print("")


# str, int and float
y = 3.2
y = int(y)
y = float(y)
y = str(y)
print("$" + y)
print("")

# escape codes
print("escape\" me\\ \n next \t line")
print("")
# Concatenation


# Loops
# While loops
done = False
while not done:
    pass
    #print("hello")
    #done = False
#print("end loop")


x = 0
while x < 100:
    print(x)
    x += 5


# For loops and ranges
for i in range(10):
    print(i)


for i in range(10,20, 5):
    print(i)


# Keep a running total
total = 0
for i in range(1,101):
    total += i
print(total)

# Nested loops
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                pass

for q in range(10):
    for r in range(10):
        print("*", end = " ")
    print()

# continue, break and else
for i in range(10):
    if i == 0:
        continue
    print(100/i)

for i in range(-5, 5):
    print(100/i)


for i in range(100):
    if i == 50:
        break
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("done")







