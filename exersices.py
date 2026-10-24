#Exercise 3.8

print("This is the orginal list")
favourite_places = ['Cameroon', 'China', 'Usa', 'UK', 'Uganda', 'Australia', 'Berlin', 'Finland', 'Libia']
print(favourite_places)

print("this is the sorted list")
print(sorted(favourite_places))

print("this is the original list again")
print(favourite_places)

print("This is the list in reverse order")
print(sorted(favourite_places, reverse = True)) #reversing it temporally

print("this is the original list")
print(favourite_places)

print("this is the list in reverse")
favourite_places.reverse()
print(favourite_places)

print('This is the reverse of the reversed list')
favourite_places.reverse()
print(favourite_places)

print("this is the sorted reversed list")
favourite_places.sort()
print(favourite_places)

print("this is the sorted reversed list revered alphabetically")
favourite_places.sort(reverse = True)
print(favourite_places)





