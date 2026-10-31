#Exercise on looping through a list

#food
favourite_food = ['Rice', 'Achu', 'Eru', 'Equang', 'Kati-kati']
for food in favourite_food:
    print(food)
    print(f"I like {food.title()} so much")
print("I'm a foodie i love food so much.")

#animal
animals = ['Dog', 'Cat', 'Rat']
for animal in animals:
    print(animal)
    print(f"A {animal} will make a creat pet")
print("Any of the above animals will make a greate pet")

#Exersice on making numerical lists
for numbers in range(1, 21):
    print(numbers)

"""one_milion = []
for values in range(1, 1000001):
    one_milion.append(values)
    print(one_milion)"""

#odd numbers
odd_numbers = []
for numbers in range(1, 10):
    value = 2 * numbers + 1
    odd_numbers.append(value)
print(odd_numbers)

#multiple of three
multiple_of_3 = []
for numbers in range (3, 31, 3):
    multiple_of_3.append(numbers)
print(multiple_of_3)

#cubes
cubes = []
for cube in range(1, 11):
    value = cube ** 3
    cubes.append(value)
print(cubes)

#cube comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

#Exercise on slicing lists
my_fruits = ['Mango', 'Pear', 'Apple', 'Banana', 'Guava', 'Orange']
print("The first 3 items of the list are: ")
print(my_fruits[0:3])
print("Three items from the middle of the list are: ")
print(my_fruits[2:4])
print("The last 3 items on the list are: ")
print(my_fruits[-3:])
friend_friuts = my_fruits[:]
my_fruits.append("Grapes")
print(my_fruits)
friend_friuts.append("Achu")
print(friend_friuts)


#Exercise on Tuple
food_stuffs = ('Fried Rice', 'Kati Kati', 'Cornchaff', 'Gari and Eru', 'Achu')
print("The menu of today: ")
for food in food_stuffs:
    print(food)
#food_stuffs[0] = "Iris" #type Error
#print (food_stuffs)

#rewriting the tuple
food_stuffs = ('Fried Rice', 'Kati Kati', 'Ndole', 'Pork Meat', 'Achu')
print("Modified Menu: ")
for food in food_stuffs:
    print(food)


