from random import randrange

secret = randrange(1,1000)
print(secret)

number = int(raw_input("Guess a number between 1 and 1000"))
print(number)


while(number != secret):
    if(number > secret):
        print("Too high")
    if(number < secret):
        print("Too low")
    if(number == secret):
        print("On target")
    if(number == secret):
        print("You Won!")
    number = int(raw_input("Guess again"))
    

