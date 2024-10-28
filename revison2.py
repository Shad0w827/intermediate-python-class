#conditionals and conditionals

#conditionals: youte given choices where you need to decide to with the one.

#conditionals: the keyword that defines conditions. Like: if, else, elif, etc.

number = 30

if number < 30:
    print("number less than 30")
elif number > 30:
    print("number greater than 30")
    
else:
    print ("number is 30")

print("before use of function")
a = 9
b = 10
c = a + b
print(c)
a = 8
b = 5
c = a + b
print(c)
a = 7
b = 9
c = a + b
print(c)
print("after use of function")
def add(a,b):
    c = a + b
    print(c)
    add(9,10)
    add(8,5)
    add(7,9)