print("Main Flow Services and Technoloys-Task1")

#Arithmetic operations 
print("Arthmetic operations")
a = 15
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)




#defining a list
print("\nLists")
x= [1, 7, 4, 6]
#defining a list
y= [3, 'hello', 'jitendra', 2.0,False]


#accessing elements from lists
print(x[0])
print(x[0:2])
print(y[1])
print(x[-1])
print(y[:3])

#updating a list
y[1] = "hel"
print(x)

#sorting a list
print(x.count(5))
print(x.sort())
print(x.sort(reverse=True))

#removing element from a list
x.remove(4)
print(x)
print(x.pop(1))
print(x)

#indexing method 
print(x.index(1))

#appending an element to list
x.append(3)
print(x)

#extending a list
x.extend([4,5])
print(x)
y.insert(4, [1, 2])
print(x)
print(y)



#Dictionarys
#Accessing the specific key from the dictionary
print("\n\nDictionarys")
my_dict = {'name': 'John', 'age': 30}
print(my_dict.get('name'))
print(my_dict.get('address', 'Not Found'))

#Returns a list of all the keys and values in the dictionary
my_dict = {'name': 'John', 'age': 30}
print(my_dict.keys())
print(my_dict.values())

#return a list of all key-value pairs in the dictionary
my_dict = {'name': 'John', 'age': 30}
print(my_dict.items())

#Updating the list  key-value pairs to a dictionary 
my_dict = {'name': 'John', 'age': 30}
my_dict.update({'age': 31, 'address': '123 Street'})
print(my_dict)

#Removing the list key-value pair from a dictionary
my_dict = {'name': 'John', 'age': 30, 'address': '123 Street'}
removed_value = my_dict.pop('address')
print(removed_value)
print(my_dict)

#Returns the last key-value pair added to the dictionary
my_dict = {'name': 'John', 'age': 30, 'address': '123 Street'}
removed_pair = my_dict.popitem()
print(removed_pair)
print(my_dict)



#defining a tuple
print("\nTuples")
mytuple = ("app", "website", "chrome")

#printing the tuple
print(mytuple)

#defining the length of the tuple
print(len(mytuple))

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

##combination of data types
tuple1 = ("abc", 34, True, 40, "male")

#type()
mytuple = ("lollipop", "biscuit", "chocolate")
print(type(mytuple))

#The tuple() Constructor
thistuple = tuple(("pyaar", "afroz", "ziaur"))
print(thistuple)

#accessing tuples
tupleA = ("biscuit", "chocolate", "lollipop")
print(tupleA[1])

#Negative Indexing
Atuple = ("apple", "banana", "cherry")
print(Atuple[-1])

#Range of Indexes
thistuple = ("ziaur","afroz","anees","jitendra","chinchu","manasa","gayathri")
print(thistuple[2:5])

#add tuple to tuple 
y = ("chinchu",)
thistuple += y
print(thistuple)

#loop through a tuple 
thistuple = ("papaya", "water melaon", "mango")
for x in thistuple:
  print(x)

#joining two tuples
tuple1 = ("A", "B" , "C")
tuple2 = (5, 6, 7)
tuple3 = tuple1 + tuple2
print(tuple3)




#Manipulation of strings
print("\nManipulation of Strings")

#Eliminating Unnecessary Character of a String
text = "!!!Hello, World!!!"  
clean_text = text.strip("!")  
print(clean_text) 

#Dividing a string into multiple substrings 
text = "Hello world, how are you today?"  
words = text.split()  
print(words) 

#Concatenate Strings
string1 = "Hello"  
string2 = "world"  
result = string1 + " " + string2  
print(result)  




#conditional statements 
#if statement
a=20
b=10
if a > b: 
	print("a greater than b") 
print("Program ended") 

#if-else statement
a=100
b=200
if a > b: 
	print("a greater than b")
else:
    print("b is greater than a")
print("Program ended") 

# if..else chain statement 
x= "a"
if x== "b": 
	print("letter is b") 
else: 
	if x== "c": 
		print("letter is c") 
	else: 
		if x== "a": 
			print("letter is a") 
		else: 
			print("letter isn't a,b and c") 

# if-elif statement example 
print("\nConditional Statments")
y = "b"

if y== "b": 
	print("letter is b") 

elif y== "c": 
	print("letter is C") 

elif y== "a": 
	print("letter is A") 

else: 
	print("letter isn't a,b or c") 

# Python lambda expression
a, b = 10, 20
print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")