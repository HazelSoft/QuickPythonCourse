'''
for (<Init section>; <condition Section>; <increment section>){

}

int [] arr = {1,2,3};
for (int i = 0; i < arr.length; i++){
arr[i]
}

for (String fruit: list1){

}
'''

list1 = ['Apple', 'Orange', 'Cherry', 'Mango']

for fruit in list1:
    print(fruit)

# for access_var in iterable_obj:

for i in range(0, 100, 3):
    if (i > 50):
        break
    if (i % 2 == 0):
        continue
    print(i)

for i in range(0, len(list1), 2):
    print(list1[i])
