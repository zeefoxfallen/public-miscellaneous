from os import X_OK


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
        exit()
    else:
        global y
        y = input("input second value: ")
    try:
        y = float(y)
    except:
        print("you can only use numbers")
        exit()


inval()


print("pick a operation")
print("1 - addition")
print("2 - Subtraction")
print("3 - multiplication")
print("4 - division")
op1 = input("enter you value: ")

if op1 == "1" :
    print(x+y)
elif op1 == "2":
    print(x-y)
elif op1 == "3":
    print(x*y)
elif op1 == "4":
    print(x/y)
else:
    print("you need to pick one")
    exit()