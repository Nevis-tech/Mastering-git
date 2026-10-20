#Beggining

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



