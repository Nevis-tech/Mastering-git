"""#Beggining

message = "Hello Python World"
print(message)

message = "Hello World Of Python Crash course"
print(message)
print("hope everyone is doing great")
print("And to be told we are all good thanks")

# strings

#name = "shanny rosine"
##making name to start wit capital letters & lower letters
#print(name.title())
#print(name.lower())

name = "Eic"
message = f"Hello {name}, do you want to learn some python?"
print(message )



#Using Variales in Strings

first_name = "Shanny"
last_name = "Rosine"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello {full_name.title()}!")

message = f"Hello {full_name.title()}!"
print(message)

# adding white spaces(\t) and moving to a new line(\n)

print("Languages: \n\tJavaScript \n\tC++ \n\tPython")

# striping white spaces from right using (rstrip) and from the left side using (lstrip)

favourite_language = "Python "
#print(favourite_language)
print(favourite_language.rstrip())

country =  " Cameroon"
#print(country)
print(country.lstrip())

#exercise

persons_name = "khan nevis"
print(persons_name.title())
print(persons_name.upper())
print(persons_name.lower())

quot = 'Albert Einstein once said "A person who never made a mistake, never tried something new."'
print(quot)

famous_person = f"Isac Newton"
his_message = f"first law of motion states 'A body will reamian at rest until an extenal force acts on it.' this law was stated by {famous_person} the great physicist"
print(his_message)

#Numbers

x, y, z = 2, 4, 16
sum = y + y
print(sum)
product = x * y
print(product)
division = z / x
print(division)   #answer will still be a float take note
print(5+3)

favorite_number = f"20"
my_message = f"My favourie number is {favorite_number} :)"
print(my_message)

#comments

#The Zen of Python
import this #Rules to follow and apply when writing our code
"""

#LISTS (Allows you to store information in one place)

brands = ['BMW', 'GLE', 'Toyota', 'Dodge', 'Tesla']
print(brands)

#accessing elements (by position or index, which always starts from 0 )
print(brands[0]) #BMW
print(brands[3]) #Dodge
#Negative numbers can also be used to access elements in a list from the last(beginning form -1). EG
print(brands[-1]) #Tesla
print(brands[-2]) #Dodge

#using individual values from a list
message = f"My second car was a flying {brands[-1]}" #My second car was a flying Tesla
print(message)

#Exercise

names = ["Nevis", "Khan", "Faith", "Wisdom", "Rosynie"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print(f"Hello {names[0]}! How are you doing?")
print(f"Hello {names[1]}! How are you doing?")
print(f"Hello {names[2]}! How are you doing?")
print(f"Hello {names[3]}! How are you doing?")
print(f"Hello {names[4]}! How are you doing?")

#Changing, Adding and Removing elements
motorcycles = ['Honda', 'yamaha', 'suzuki', 'Ellisam', 'Nanfang']
print(motorcycles)

#changing
motorcycles[2] = 'Lfancy'
print(motorcycles)

#adding
motorcycles.append('KEKE')
motorcycles.append('Short Gun') 
print(motorcycles)

#inserting
motorcycles.insert(0, 'High Jack') #exact position and item
print(motorcycles)

#removing(deleting)
#1) using the del method (which after item is removed, it can not be used again)
del motorcycles[0]
print(motorcycles)

#2) using the pop method (which after item is removed, it can be used after) (removes just the last item or element)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"the last motorcycle i owned was {last_owned.title()}")

#popping by position
first_owned = motorcycles.pop(0)
print(f"The first car i owned was a {first_owned.title()}")


#exercise under lists

guest = ['Fabiola', 'Rosynie', 'Bright']
first_guest = guest[0]
print(f"We Highly invite you {first_guest} to our dinner to night")
second_guest = guest[1]
print(f"We Highly invite you {second_guest} to our dinner to night")
third_guest = guest[2]
print(f"We Highly invite you {third_guest} to our dinner to night")

print(f"{second_guest} is not able to attend the dinner")

guest[1] = 'Rosine'
print(f"We Highly invite you {first_guest} to our dinner to night")
second_guest = guest[1]
print(f"We Highly invite you {second_guest} to our dinner to night")
third_guest = guest[2]
print(f"We Highly invite you {third_guest} to our dinner to night")

print("Hello guys i just found a bigger table!")

fourth_guest = guest.insert(0, 'Fabiola')
fifth_guest = guest.insert(2, 'Nevis')
sixth_guest = guest.append('Angelo')
print(guest)

#...........

print(f"We Highly invite you {first_guest} to our dinner to night")
print(f"We Highly invite you {second_guest} to our dinner to night")
print(f"We Highly invite you {third_guest} to our dinner to night")
print(f"We Highly invite you {guest[0]} to our dinner to night")
print(f"We Highly invite you {guest[2]} to our dinner to night")
print(f"We Highly invite you {guest[-1]} to our dinner to night")

print("Oh sory guys the dinner will be delaid and i can invite just 2 people :(")

guest.pop(0)
guest.pop(1)
guest.pop(2)
guest.pop(3)

print(guest)



