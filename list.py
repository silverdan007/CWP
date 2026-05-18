import random
fruits = ["mango", "orange", "pineapple", "apple", "pawpaw"]
n = 1
for fruit in fruits:
    print(f"{n}.\t {fruit}")
    n += 1

#add a new fruit to the end of the list using append()
new_fruit = input("Gimme a fruit")
fruits.append(new_fruit)
for fruit in fruits:
    print(f"{n}.\t {fruit}")
    n += 1
#insert a fruit at position 2 in your list
new_fruit = input("New fruit at position 2")
fruits.insert(2, new_fruit)
for fruit in fruits:
    print(f"{n}.\t {fruit}")
    n += 1
fruits.pop()
print()
for fruit in fruits:
    print(f"\n {n}.\t {fruit}")
    n += 1

fruits.remove("mango")
print(fruits)
#sort by ascending order
fruits.sort()
print(f"\n {fruits}")

my_list = []
for num in range(10):
    num_a = random.randint(1, 12)
    my_list.append(num_a)
print(my_list, "\n\n")
my_list.reverse()
print(my_list)
count = 0
for a in range(10):
    for num in my_list:
        if num == a:
            count += 1
    print(f'{a}: appeared {count} times')
    count = 0
for num in my_list:
    a = my_list.count(num)
    print(f"{num}:\t {a} times")

choice = random.choice(my_list)
c_index = my_list.index(choice)
print(f'{choice} is at index {c_index}')
new_list = [fruits + my_list]
print(new_list)

