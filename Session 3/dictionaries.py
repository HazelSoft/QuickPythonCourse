empty_dict = {}
print(empty_dict)

dict = {'course_name': 'Python', 'credits': 3}
print(dict)
print(dict['course_name'])

dict['course_name'] = 'C++'
print(dict['course_name'])

dict['teacher'] = 'Adil'
print(dict)

del dict['teacher']
print(dict)
# print(dict['course'])

for k, v in dict.items():
    print(f"Key: {k} => Value: {v}")

for k in dict.keys():
    print(f"Key: {k} ")

for v in dict.values():
    print(f"Value: {v} ")
