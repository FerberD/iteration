from random import randrange
highlow = ""
feedback = raw_input("Think of number")
number = randrange(1,1000)
print(number)
(raw_input("Is this number a:HIGHER, b:LOWER, or c:EQUAL to yours"))
while(feedback != ("c")):
    randrange(1,1000)
    print(number)
    feedback = raw_input("Is this number a:HIGHER, b:LOWER, or c:EQUAL to yours")
    
