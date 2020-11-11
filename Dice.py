import random
x='Y'

print("This is Dice Stimulator Game:")
while(x=='Y'):
    number=random.randint(1,6)
    if number==1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")
    elif number==2:
        print("---------")
        print("|       |")
        print("|  o o  |")
        print("|       |")
        print("---------")
    elif number==3:
        print("---------")
        print("|       |")
        print("| o o o |")
        print("|       |")
        print("---------")
    elif number==4:
        print("---------")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print("---------")
    elif number==5:
        print("---------")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print("---------")
    else:
        print("---------")
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
        print("---------")
    
    x=input("Type Y for again Dice Rolling: ")

print("Game End!!!")        
