a_tuple = (100, 200, 300)
b_tuple = (500, 600, 700)

print(a_tuple)
print(a_tuple[0])
print(a_tuple[-1])

#del a_tuple
# print(a_tuple)

a, b, c = a_tuple
print(f'a: {a}, b: {b}, c: {c}')

print(a_tuple[:2])
print(a_tuple[1:])
print(a_tuple[:])

print(a_tuple + b_tuple)
