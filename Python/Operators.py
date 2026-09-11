# 1. Arithmetic Operators

# Addition
from ast import And


a = 10 
b = 10 
print(a + b)

# Subtraction

print(a - b)

# Multiplication

print(a * b)

# Division
print(a/b)

#Floor division
print(a//b)

#Reminder
print(a%b)

#Power
print(a**b)

# 2. Comparison Operators
c = 10
d = 10

print(c==d)
print(c!=d)
print(c<d)
print(c>d)
print(c>=d)
# print(c<=d)

# 3. Logical Operators

# and or not

age = 20 # 20 wla ko job nhi da rhya hai 

print(age > 18 and age < 25)

print(age < 18 or age > 10)


# 4. Assignment Operators

x = 10

x += 5    # x = x + 5 → 15
x -= 3    # x = x - 3 → 12
x *= 2    # x = x * 2 → 24
x /= 4    # x = x / 4 → 6.0

# 5. Membership Operators

sequence = "ATGCGT"

print("ATG" in sequence) # T
print("XYZ" not in sequence) # T
print("ATGc" in sequence) # F


genes = ["BRCA1", "TP53", "EGFR"]

print("TP53" in genes)

