# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3")

# print(type(x))


# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2")

# print(type(x))


# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)

# print(type(x))


# b = "Hello, World!"
# print(b[2:8])

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# a = " Hello, World!    "
# print(len(a))
# b = a.strip()
# print(len(b))


# a = "Hello"
# b = "World"
# c = a + b
# print(c)


# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# name = 'Tushar'
# age = 23
# print(f"Hello, My name is {name} and I'm {age} years old.")

# id = 8000

# print(f'my numbrr is {id} ')


# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("Hello"))
# print(bool(15))

# x = 5
# y = 3

# print(x ** y) #same as 2*2*2*2*2

# x = 7
# y = 2

# print(x // y)


# x = 5 

# x -= 3

# print(x)

# x = 5

# print(x > 6 and x < 10)

# x = 5

# print(x > 6 or x < 10)

# x = 5

# print(not(x > 3 and x < 10))




# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# y = thisdict.values()
# print(x)
# print(y)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2024

# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child2"]["name"])


# a = 200
# b = 200
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

letter = "a"
 
if letter == "B":
    print("letter is B")
 
else:
 
    if letter == "C":
        print("letter is C")
 
    else:
 
        if letter == "A":
            print("letter is A")
 
        else:
            print("letter isn't A, B and C")