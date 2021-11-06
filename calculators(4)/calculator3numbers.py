x = input("input first value: ")
y = input("input second value: ")
z = input("input therd value: ")
try:
    x = float(x)
    y = float(y)
    z = float(z)
except:
    print("you can only use numbers")
    exit()
op1 = input("what is your first operation: ")
op2 = input("what is your second operation: ")
if op1 == "+" and op2 == "+" :
    print(x+y+z)
elif op1 == "-" and op2 == "-":
    print(x-y-z)
elif op1 == "*" and op2 == "*":
    print(x*y-z)
elif op1 == "/" and op2 == "/":
    print(x/y/z)
elif op1 == "+" and op2 == "-":
    print(x+y-z)
elif op1 == "+" and op2 == "*":
    print(x+y*z)
elif op1 == "+" and op2 == "/":
    print(x+y/z)
elif op1 == "-" and op2 == "+":
    print(x-y+z)
elif op1 == "-" and op2 == "*":
    print(x-y*z)
elif op1 == "-" and op2 == "/":
    print(x-y/z)
elif op1 == "*" and op2 == "+":
    print(x*y+z)
elif op1 == "*" and op2 == "-":
    print(x*y-z)
elif op1 == "*" and op2 == "/":
    print(x*y/z)
elif op1 == "/" and op2 == "+":
    print(x/y+z)
elif op1 == "/" and op2 == "-":
    print(x/y-z)
elif op1 == "/" and op2 == "*":
    print(x/y*z)