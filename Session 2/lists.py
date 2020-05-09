"""
Collection of items defined between []
Indexed at 0
len method
Slicing
Concatenation
Removing an Element
Decomposition/Unpacking
"""

a_list = ['Orange', 'Mango', 'Peach',
          'Banana', 'Plum', 'Melon', 12, 34, True]

b_list = ['Potato', 'Lettuce', 'Carrots', 'Raddish']
print(a_list)

# Getting the first element of the list
print(a_list[0])

# getting the first character of the first element (which MUST be a string)
print(a_list[0][0])

# using teh negative index
print(a_list[-1])
print(a_list[-2])
print(a_list[-3])
print(a_list[-4])

# index out of range
# print(a_list[100])

# geting the length of the list
print(len(a_list))

# slicing
print(a_list[3: 7])

print(a_list[: 7])
print(a_list[3:])
print(a_list[:])

# Concatenation
c_list = a_list + b_list
print(c_list)

print(f'Before: {c_list[8]}')
del c_list[8]
print(f'After: {c_list[8]}')

# decomposition / Unpacking
d_list = [4, 5, 6]
a, b, c = d_list

print(f'a: {a}, b: {b}, c: {c}')
