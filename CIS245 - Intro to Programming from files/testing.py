import random

fruits = ['apple', 'banana', 'cherry', 'date']
selected_fruits = random.choices(
    fruits,
    weights=[10, 5, 1, 1],
    k=3

)
for fruit in selected_fruits:
    print(fruit,end=", " )
print(selected_fruits[0])