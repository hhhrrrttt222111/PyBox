import random

list1 = ["A friend asks only for your time not your money.", "A fresh start will put you on your way.",
         "A dubious friend may be an enemy in camouflage.", "You have a secret admirer.",
         "A faithful friend is a strong defense.","Good fortune will be yours.",
         "Be passionate and totally worth the chaos"]

print("Lets have a check on your luck by rolling the dice !!")
c = 'y'

while c == 'y':
    x = random.randint(1, 6)
    print("\n{0}\n".format(random.choice(list1)))
    if x == 1:
        print("-------------")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("-------------")
    if x == 2:
        print("-------------")
        print("|           |")
        print("|    0 0    |")
        print("|           |")
        print("-------------")
    if x == 3:
        print("-------------")
        print("|           |")
        print("|   0 0 0   |")
        print("|           |")
        print("-------------")
    if x == 4:
        print("-------------")
        print("|  0     0  |")
        print("|           |")
        print("|  0     0  |")
        print("-------------")
    if x == 5:
        print("-------------")
        print("|  0     0  |")
        print("|     0     |")
        print("|  0     0  |")
        print("-------------")
    if x == 6:
        print("-------------")
        print("|  0     0  |")
        print("|  0     0  |")
        print("|  0     0  |")
        print("-------------")
    c = input("Enter y to roll again: ")
