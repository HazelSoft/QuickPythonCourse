"""
append
insert
remove
pop
index
sort
reverse
copy
clear

"""

a_list = ['Orange', 'Mango', 'Peach',
          'Banana', 'Plum', 'Melon']

print(a_list)

# append
a_list.append('Grapes')
print(f'After appending: {a_list}')

# insert
a_list.insert(3, 'Cherry')
print(f'After insert: {a_list}')

# remove
a_list.remove('Cherry')
print(f'After remove: {a_list}')

# pop
popped_element1 = a_list.pop()
popped_element2 = a_list.pop(3)
print(f'After pop: {a_list}')
print(f'Popped Element: {popped_element1}')
print(f'Popped Element by Index: {popped_element2}')

# index
print(f"Index of Mango: {a_list.index('Mango')}")
#print(f"Index of Falsa: {a_list.index('Falsa')}")
print(f'After : {a_list}')

# sort
a_list.sort(reverse=True)
print(f'Sorted : {a_list}')

# clear
a_list.clear()
print(f'Cleared : {a_list}')
