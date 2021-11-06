x = input("input first value: ")
y = input("input second value: ")
try:
    x = float(x)
    y = float(y)
except:
    print("you can only use numbers")
    exit()
op1 = input("what is your first operation: ")
if op1 == "+" :
    print(x+y)
elif op1 == "-":
    print(x-y)
elif op1 == "*":
    print(x*y)
elif op1 == "/":
    print(x/y)