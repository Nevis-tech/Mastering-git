#Exercise on looping through a list

"""
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

""
one_milion = []
#for values in range(1, 1000001):
    one_milion.append(values)
    print(one_milion)
""

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



#EXERCISES ON IF Statements
car = 'tesla'
print("is car == 'tesla'? maybe")
print(car == 'tesla')

print("is car == 'audi'? sure its False")
print(car == 'audi') 

#testfor equality and inequality
age_0 = 20
age_1 = 12
print(age_0 >=19 and age_1 >= 19) 
print(age_0 >= 19 or age_1 <= 19)

#Test using the lower method
food = 'ACHU'
print(food == 'achu')
print(food.lower() == 'achu')

#Testing whether an item is in a list
menu = ['achu', 'rice', 'corn', 'eru']
favourite_food = 'achu'
if favourite_food not in menu:
    print(f"{favourite_food.title()} is not in that resto dont go there")
else:
    print(f"{favourite_food.title()} is there you can go there")


alien_color = 'green'
if alien_color == 'green':
    print("you just earned 10 points!")


age = int(input("Enter your age: \n"))
if age < 2:
    print("you are still a baby")
elif age == 2 or age < 4:
    print("You are a todler")
elif age == 4 or age < 13:
    print("You are a kid")
elif age == 13 or age < 20:
    print("You are a teenager")
elif age == 20 or age < 65:
    print("you are an adult")
elif age == 65 or age >  65:
    print("You are Old!")
else:
    print("Enter a valid age")
"""

#exercises on dictionaries
#storing information about a person
"""
person = {
    'first_name' : 'khan',
    'last_name' : 'nevis',
    'age' : 22,
    'city' : 'bamenda'
}
print(person)

#storing peoples favourite numbers
favourite_numbers = {
    'khan' : 22,
    'nevis' : 40,
    'faith' : 10,
    'norbet' : 3,
    'collins' : 20
}
print(favourite_numbers)

#printing the favourite number of each persons name
#first person
favourite_1 = favourite_numbers['khan']
print(f"The favourite number of khan is {favourite_1}")
#second person
favourite_2 = favourite_numbers['nevis']
print(f"The favourite number of khan is {favourite_2}")
#third person
favourite_3 = favourite_numbers['faith']
print(f"The favourite number of khan is {favourite_3}")
#forth person 
favourite_4 = favourite_numbers['norbet']
print(f"The favourite number of khan is {favourite_4}")
#fifth person
favourite_5 = favourite_numbers['collins']
print(f"The favourite number of khan is {favourite_5}")

#words and thire meaning
glossary = {
    'list' : 'Used to make a list of things/items []',
    'tuple' : 'used to make list of things/items that can not be edited ()',
    'dictionary' : 'Acollection of key-value pairs { }',
    'loops' : 'used to loop through things',
    'if statements' : 'used for conditions',
}
#list
words_meaning = glossary['list']
print(f"List: {words_meaning}")
#tuple
words_meaning = glossary['tuple']
print(f"Tuple: {words_meaning}")
#dictionary
words_meaning = glossary['dictionary']
print(f"Dictionary: {words_meaning}")
#loops
words_meaning = glossary['loops']
print(f"Loops: {words_meaning}")
#if conditions
words_meaning = glossary['if statements']
print(f"If- statements: {words_meaning}")


#exercise 6.4   

glossary_2 = {
    'list' : 'Used to make a list of things/items []',
    'tuple' : 'used to make list of things/items that can not be edited ()',
    'dictionary' : 'Acollection of key-value pairs { }',
    'loops' : 'used to loop through things',
    'if statements' : 'used for conditions',
}
#making the above code clean
for key, value in glossary_2.items():
    print(f"{key}: {value}")

#6.5
rivers = {
    'nile' : 'egypt',
    'wouri' : 'cameroon',
    'khan' : 'nevis',
}
for river, country in rivers.items():
    print(f"The river {river.title()} passes through {country.title()}")
print("the rivers mentioned includes:")
for river in rivers.keys():
    print(river.title())
print("the countries mentioned include:")
for country in rivers.values():
    print(country.title())

#6.6 polling
favourite_languages = {
    'nevis' : 'python',
    'norbet' : 'xbet',
    'mba' : 'woman',
    'faith' : 'game'
    }
people = ['fabiola', 'rosine',   'nevis', 'mba']

for person in people:
    if person in favourite_languages:
        print(f"{person.title()}, your favourite language is  {favourite_languages[person].title()}")
    else:
        print(f"{person.title()}, you need to take a poll!")
    """

#exercises on chapter 7
#7.1
"""car = input("what is the name of the car  that you want to rent?\n")
print(f"let me see if i can find you a {car}")

#7.2
seat = input("How many people are in your dinner tabke?\n")
seat = int(seat)
if seat > 8:
    print("please you will have to wait for a table")
else:
    print("your table is ready")

#7.3
number = int(input("enter a number and i will tell if it's a multiple of 10"))
if number % 10 == 0:
    print(f"{number} is a  multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")"""

#PYTHON PRACTICE EXERCISE
#Question 1: Grade Calculator
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#list of student score
scores = [85, 42, 95, 67, 78] 
for score in scores:
    print("\nScore: ")
    print(score)
    print("Grade: ")
    print(get_grade(score))

#Question 2: Word frequency counter
"""def count_words(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[words] += 1
        else:
            word_count[words] = 1
    return word_count

sentence = input("Write a sentence:")
result = count_words(sentence)
print(result)"""

#Question 3: 
def cart_total(cart):
    total = 0

    for items, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]

        if quantity == 0:
            continue
        total += price * quantity
    return total

cart = {
    "apple" : {"price" : 0.5, "quantity" : 4},
    "bread" : {"price" : 2.5, "quantity" : 2},
    "milk" : {"price" : 1.2, "quantity" : 3}
}

result =  cart_total(cart)
print("shopping cart total:", result)

#Question 4:
"""def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#second function
def filter_primes(numbers):
    primes = []
    for number in numbers:
        if prime_number(number):
            primes.append(number)
    return primes

#test the function
numbers = [4, 7, 10, 13, 15, 17, 18, 19]

result = filter_primes(numbers)
print("prime numbers:", result)"""

#Question 5:
students = [
    {"name" : "Alice", "marks" : [85, 90, 78]},
    {"name" : "Bob", "marks" : [60, 55, 70]},
    {"name" : "Cara", "marks" : [95, 92, 89]}
]

#function to calculate students average
"""def student_averages(students):
    averages = {}

    for student in students:
        name = student["name"]
        marks = student["marks"]

        total = 0

        for mark in marks:
            total += mark

        average = round(total / len(marks), 2)
        averages[name] = average
    return averages"""