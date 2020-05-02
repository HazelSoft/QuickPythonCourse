course_name = 'Quick Python by HazelSoft'
another_course = course_name

print(course_name)

# printing by index
print(course_name[0])
print(course_name[1])
print(course_name[2])

# -ve index will start the traversing from the end of the string
print(course_name[-1])
print(course_name[-2])
# print(course_name[100])
# Will generate "string index out of range" error

# slicing
print(course_name[1:7])
# 7 Characters starting from index 1

print(course_name[:7])
# 7 Characters starting from index 0

print(course_name[1:])
# get all characters from starting index 1 till the end of the string

print(course_name[:])
# Make a copy of the string with all the contents same as the original string

print(course_name.upper())
# Upper case conversion

print(course_name.lower())
# lower case conversion

print(course_name.title())
# title case conversion

print(course_name.find('t'))
# Gives the index of the first occurance of teh given character.
# -1 is returned if there is no character found
print(course_name.find('x'))

print(course_name.replace('o', 'e'))
# replace all the occurances of o with e

print('Python Course' in course_name)
# return true if the LHS of the in operator is present in the RHS

print(course_name.find('Python Course') != -1)
# Same as the in operator

sample_string = 'Google\'s App Engine is using Python'
print(sample_string)
