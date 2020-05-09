# if boolean expression:
#     print(1)
#     print(2)
# print(3)

if False:
    print(1)
    print(2)
print(3)

# Write a simple program tat determines if a given number is even or Odd
n = 4

if n % 2 == 0:
    print('The given number is Even')
else:
    print('The given number is Odd')

# Write a simple program that takes three numbers and determines
# which one is the greatest, which is the middle one and which is the smallest

a, b, c = (4, 3, 5)
greatest, middle, lowest = 0, 0, 0

if a > b and a > c:
    greatest = a
    if b > c:
        middle = b
        lowest = c
    else:
        middle = c
        lowest = b
elif b > a and b > c:
    greatest = b
    if a > c:
        middle = a
        lowest = c
    else:
        middle = c
        lowest = a
else:
    greatest = c
    if a > b:
        middle = a
        lowest = b
    else:
        middle = b
        lowest = a

print(f"{greatest} is the largest number given, {middle} is the second largest, {lowest} is the smallest number given")
