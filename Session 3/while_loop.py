'''
while <Boolean Expression>:
    Statement 1
    Statement 2
    Statement 3
'''
n = 8

while n > 4:
    print(f'{n} is greater than 4')
    n -= 1

print('Done')

answer = 'y'
while True:
    answer = input('Do you want to continue the loop (y/n): ')
    print(f'Answer: {answer}')
    if answer.lower() == 'y':
        break
