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

