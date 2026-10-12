import math

# Convert inputs from strings to floats
X1 = float(input("What is the value of X1: "))
Y1 = float(input("What is the value of Y1: "))
X2 = float(input("What is the value of X2: "))
Y2 = float(input("What is the value of Y2: "))

# Calculate the distance between (X1, Y1) and (X2, Y2)
distance = math.sqrt(math.pow(X2 - X1, 2) + math.pow(Y2 - Y1, 2))
print("Distance between the two points:", distance)

# Using built-in math functions makes calculating complex equations efficient and straightforward.
