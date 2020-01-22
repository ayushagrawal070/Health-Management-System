def getdate():
    import datetime
    return datetime.datetime.now()


ch = "y"
while(ch=="y"):
    print("1. Load data\n", "2. Retreive data\n", end="")
    choice = int(input())

    if choice == 1 :
        print("1. harry", "2. rohan", "3. ayush")
        choice1 = int(input())
        if choice1 == 1 :
            print("1. exrecise\n", "2. diet plan\n")
            choice2 = int(input())
            if choice2 == 1:
                f = open("harryex.txt","w")
                content = input("enter the exercise")
                f.write(content)
                f.close()
                print("successfully saved !!")
            elif choice2 == 2:
                f = open("harrydiet.txt", "w")
                content = input("enter the diet plan")
                f.write(content)
                f.close()
                print("successfully saved !!")
        elif choice1 == 2 :
            print("1. exrecise\n", "2. diet plan\n")
            choice2 = int(input())
            if choice2 == 1:
                f = open("rohanex.txt", "w")
                content = input("enter the exercise")
                f.write(content)
                f.close()
                print("successfully saved !!")
            elif choice2 == 2:
                f = open("rohandiet.txt", "w")
                content = input("enter the diet plan")
                f.write(content)
                f.close()
                print("successfully saved !!")
        elif choice1 == 3 :
            print("1. exrecise\n", "2. diet plan\n")
            choice2 = int(input())
            if choice2 == 1:
                f = open("ayushex.txt", "w")
                content = input("enter the exercise")
                f.write(content)
                f.close()
                print("successfully saved !!")
            elif choice2 == 2:
                f = open("ayushdiet.txt", "w")
                content = input("enter the diet plan")
                f.write(content)
                f.close()
                print("successfully saved !!")
    else :
        print("1. harry", "2. rohan", "3. ayush")
        choice1 = int(input())
        if choice1 == 1 :
            print("1. exrecise\n", "2. diet plan\n")
            choice2 = int(input())
            print(getdate())
            if choice2 == 1:
                f = open("harryex.txt")
                print(f.read())
                f.close()
            elif choice2 == 2:
                f = open("harrydiet.txt")
                print(f.read())
                f.close()
        elif choice1 == 2 :
            print("1. exrecise\n", "2. diet plan\n")
            choice2 = int(input())
            if choice2 == 1:
                f = open("rohanex.txt")
                print(f.read())
                f.close()
            elif choice2 == 2:
                f = open("rohandiet.txt")
                print(f.read())
                f.close()
        elif choice1 == 3 :
            print("1. exrecise\n", "2. diet plan\n")
            choice2 = int(input())
            if choice2 == 1:
                f = open("ayushex.txt")
                print(f.read())
                f.close()
            elif choice2 == 2:
                f = open("ayushdiet.txt")
                print(f.read())
                f.close()

    ch = input("do you want to continue(y/n)")
