def greet(fname, lname):
    print(f'Hello {fname}, {lname}')


def increment(num, incr=1):
    num += incr
    return num

# Ali drives car


def append(list1, val):
    list1.append(val)


def add(a, b):
    return a + b


greet('Python', 'Programming')
greet('Adil', 'Farooq')

n = 5
print(f'BEFORE:: {n}')
increment(n)
print(f'AFTER:: {n}')

l = ['Apple', 'Orange', 'Cherry', 'Mango']
print(f'BEFORE:: {l}')
append(l, 'Banana')
print(f'AFTER:: {l}')

result = add(5, 6)
print(f'RESULT:: {result}')

n = 5
print(f'BEFORE:: {n}')
n = increment(n)
print(f'AFTER:: {n}')
print(f'BEFORE:: {n}')
n = increment(n, 2)
print(f'AFTER:: {n}')


def sentence(subject='', verb='', obj=''):
    print(f"{subject} {verb} {obj}")


sentence('Ali', 'drives', 'car')
sentence(obj='bike', subject='Ahmad',  verb='rides')

l2 = ['Akmal', 'runs', 'on Foot']
sentence(*l2)


def arbitrary_args(*a):
    print(a)


arbitrary_args(1, 2, 3, 4, 5, 'Ali')


def add_and_multiply(a, b):
    return a + b, a * b


anm = add_and_multiply

print(add_and_multiply(5, 6))
print(anm(10, 3))


def multiply(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


print(multiply(2, 4))
