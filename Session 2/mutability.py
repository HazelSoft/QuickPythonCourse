a_int = 2
a_float = 2.3
a_string = 'Hello'
a_list = [1, 2, 3, 4, 5]

print(id(a_float))
print(id(a_string))
print(id(a_list))

print(f'Before: {id(a_int)}')
a_int += 2
print(a_int)
print(f'After: {id(a_int)}')

print(f'Before: {id(a_string)}')
b_string = a_string.replace('l', 'o')

print(f'After: {a_string} -> {id(a_string)}')
print(f'b_string: {b_string} -> {id(b_string)}')

print(f'Before: {a_list} -> {id(a_list)}')
a_list[2] = 77
print(f'After: {a_list} -> {id(a_list)}')

print(f'Before: {a_list} -> {id(a_list)}')
del a_list[2]
print(f'After: {a_list} -> {id(a_list)}')
