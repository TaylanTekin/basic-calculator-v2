def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while True:
    print("Simple calculator")
    a = float(input("First number: "))
    b = float(input("Second number: "))
    op = input("Operation (+, -, *, /): ")

    if op == "+":
        print("Result:", add(a, b))
    elif op =="-":
        print("Result:", subtract(a, b))
    elif op == "*":
        print("Result:", multiply(a, b))
    elif op == "/":
        print("Result:", divide(a, b))
    else:
        print("Invalid operator")
        
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break