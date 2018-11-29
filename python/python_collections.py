#STRINGS
course = "Python"
print(len(course)) #prints length of string
print(course[0])   #prints character at index of string
print(course[-1])  #gets back to the end of string for negative indices
print(course[0:3]) #prints substring starting from 0 index to 2 index

first = "mehul"
last = "agrawal"
full = first + " " + last #concatinating
print(full)

"""formated strings:-"""
full = f"{first} {last}" #any valid statemet can be written inside curly braces
print(full)

"""string methods"""
print(course.upper())
print(course.lower())
print(course.title()) #makes first character of every word capital
print(course.strip()) #trims spaces from front and end ot the string
print(course.rstrip()) #strips from right
print(course.lstrip()) #from left
print(course.find("thon")) #returns index of the substring
print(course.replace("o", "-"))
b = course.split(",") #splits the string at "," and stores the seperated literals in a list
print(b)
print("thon" in course) #returns true if substring present in the string variable
print("thon" not in course)

"""
Method			Description
capitalize()	Converts the first character to upper case
casefold()		Converts string into lower case
center()		Returns a centered string
count()			Returns the number of times a specified value occurs in a string
encode()		Returns an encoded version of the string
endswith()		Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()			Searches the string for a specified value and returns the position of where it was found
format()		Formats specified values in a string
format_map()	Formats specified values in a string
index()			Searches the string for a specified value and returns the position of where it was found
isalnum()		Returns True if all characters in the string are alphanumeric
isalpha()		Returns True if all characters in the string are in the alphabet
isdecimal()		Returns True if all characters in the string are decimals
isdigit()		Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()		Returns True if all characters in the string are lower case
isnumeric()		Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()		Returns True if all characters in the string are whitespaces
istitle()		Returns True if the string follows the rules of a title
isupper()		Returns True if all characters in the string are upper case
join()			Joins the elements of an iterable to the end of the string
ljust()			Returns a left justified version of the string
lower()			Converts a string into lower case
lstrip()		Returns a left trim version of the string
maketrans()		Returns a translation table to be used in translations
partition()		Returns a tuple where the string is parted into three parts
replace()		Returns a string where a specified value is replaced with a specified value
rfind()			Searches the string for a specified value and returns the last position of where it was found
rindex()		Searches the string for a specified value and returns the last position of where it was found
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()		Splits the string at the specified separator, and returns a list
rstrip()		Returns a right trim version of the string
split()			Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
swapcase()		Swaps cases, lower case becomes upper case and vice versa
title()			Converts the first character of each word to upper case
translate()		Returns a translated string
upper()			Converts a string into upper case
zfill()			Fills the string with a specified number of 0 values at the beginning
"""

"""escape sequences:- backslash character used as an escape sequence"""

#Python Collections (Arrays)
"""There are four collection data types in the Python programming language:

~List is a collection which is ordered and changeable. Allows duplicate members.
~Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
~Set is a collection which is unordered and unindexed. No duplicate members.
~Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning, and,
it could mean an increase in efficiency or security.
"""

#list
thislist = ["apple", "banana", "cherry"] #creating a list
print(thislist)

list = [input() for i in range(5)] #scanning a list
print(list)

print(thislist[1]) #accessing items

thislist[1] = "blackcurrant" #altering items
print(thislist)

if "apple" in thislist:
	print("Yes, 'apple' is in the fruits list") #checking for an item

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry") #prints index of first occurence of the element
print(x) #prints 2

print(len(thislist)) #prints length of the list

thislist.append("orange") #to add items at last position to the list
print(thislist)

thislist.insert(1, "chiku") #to insert item at given index
print(thislist)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars) #adding another list to current list
print(fruits) #prints ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

thislist.remove("banana") #The remove() method removes the specified item
print(thislist)

thislist.pop() 	#The pop() method removes the specified index,
print(thislist) #(or the last item if index is not specified)

del thislist[0] #The del keyword removes the specified index
print(thislist)

thislist.clear() #makes the list empty
print(thislist)

thislist = list(("apple", "banana", "cherry")) #creating list with list constuctor
print(thislist)									#note the double round-brackets

x = thislist.copy() #stores a copy of the list
print(x)

fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry") #counts the number of such elements in the list
print(x) #prints 1

fruits.reverse() #reverses the list
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort() #sort in ascending order
print(cars)

cars.sort(reverse=True) #sort in descending order
print(cars)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def myFunc(e):
  return len(e) #here you can write any function
cars.sort(key=myFunc) #Sort the list by the length of the values
print(cars)

def myFunc(e):
  return len(e)
cars.sort(reverse=True, key=myFunc) #same as above but reversed
print(cars)

#tuple
"""	NOTE- A tupple is like a list, but list is something
		which can be modified but a tupple cannot be modified.
		Tupple is a read only list. It is shown is paranthesis()
		unlike list which is written in square brackets[]."""
thistuple = ("apple", "banana", "cherry") #creating a tuple
print(thistuple)

print(thistuple[1]) #accessing tuple values

"""values of tuple cannot be changed"""
"""check item same as lists"""
"""length same as lists"""

del thistuple #deleting a tuple

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)								#creating tuple usin constructor

"""count() and index() methods as in lists"""

#sets
thisset = {"apple", "banana", "cherry"} #creating a set
print(thisset)							#note the curly brackets
"""sets are unordered, so the items will appear in a random order."""

for x in thisset: #accessing set elements
 	print(x)

print("banana" in thisset) #checking an element

"""items in a set cannot be changed but you can add new items"""
thisset.add("orange") #adding an item at the last
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"]) #add multiple items
print(thisset)

"""leng(), pop(), clear(), discard(), del, remove() functions are same as in lists"""

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #removes the element
print(thisset)
"""If the item to remove does not exist, remove() will raise an error."""

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #removing an item using discard
print(thisset)
"""If the item to remove does not exist, discard() will NOT raise an error."""

thisset = set(("apple", "banana", "cherry")) #creating set using constructer
print(thisset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) #does union of both the sets
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #prints those elements of x which are not in y
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) #same above function, just itself gets updated insteaad of a third variable
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) #prints common elements present in both the sets
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) #same as above function, just x gets updated
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) #returns if both the sets are completely different
print(z) #prints true

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) #stores the union of those elements which are not common between both sets
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) #same as above, just x gets updated
print(x)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) #returns true if x is a subset of y
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) #returns true if y is a subset of x
print(z)

#dictionary
thisdict =	{
  "brand": "Ford",  #key:value
  "model": "Mustang",
  "year": 1964
} #creating a dictionary
print(thisdict)

x = thisdict["model"] #accessinng is done using key
print(x)

thisdict["year"] = 2018 #changing values
print(thisdict)

for x in thisdict:
  print(x) #prints- brand model year

for x in thisdict:
  print(thisdict[x]) #prints- Ford Mustang 2018

for x, y in thisdict.items(): #use items() to print both, key and the value
  print(x, y)

if "model" in thisdict: #to check if key is present or not
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(len(thisdict)) #no of keys/values

thisdict["color"] = "red" #adding item
print(thisdict)

thisdict.pop("model") #deleting a key and value
print(thisdict)

thisdict.clear() #clearing the dictionary
print(thisdict)

thisdict = dict(brand="Ford", model="Mustang", year=1964) #creating using constructor