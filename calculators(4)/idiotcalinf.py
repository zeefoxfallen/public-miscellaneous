opon = "x"

def inval():
    if opon == "x":
        global x
        x = input("input first value: ")
    opon == "y"
    try:
        x = float(x)
    except:
        print("you can only use numbers")
        cal()
    else:
        global y
        y = input("input second value: ")
    try:
        y = float(y)
    except:
        print("you can only use numbers")
        cal()

def cal():
    inval()


    print("pick a operation")
    print("1 - addition")
    print("2 - Subtraction")
    print("3 - multiplication")
    print("4 - division")
    op1 = input("pick : ")

    if op1 == "1" :
        print(x+y)
    elif op1 == "2":
        print(x-y)
    elif op1 == "3":
        print(x*y)
    elif op1 == "4":
        print(x/y)
    else:
        print("you need to pick a valid answer")
        cal()

    print("")
    print("select what to do next")
    print("1 - run again")
    print("2 - exit")
    end = input("enter what to do next: ")

    if end == "2":
        exit()
    else:
        cal()

cal()

