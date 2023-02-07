import random

num = random.randint(1,20)

while True:
    n = int(input("Enter No. : "))

    if num==n:
        print("You Guess The right number")
    elif num>n:
        print("You Guess the no less than 20")
    elif num<n:
        print("You guess the Greater no.")