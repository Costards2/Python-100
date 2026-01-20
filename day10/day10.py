def add(a, b):
    print(f"{a} + {b} = {a + b}\n")
    return a + b

def subtract(a, b):
    print(f"{a} - {b} = {a - b}\n")
    return a - b

def multiply(a, b):
    print(f"{a} * {b} = {a * b}\n")
    return a * b

def devide(a, b):
    print(f"{a} / {b} = {a / b}\n")
    return a / b

operations = {
    "+": add,
    "-": subtract, 
    "*": multiply,
    "/": multiply
}

print("Calculator\n")
print()

result = 0;

def calculate():
    num1 = float(input("What is the first number?\n"))
    
    while True:
        
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation:")
        
        print()

        num2 = float(input("What is the next number?\n"))
        
        result = operations[operation](num1, num2)

        answear = input("Do you want to use your result in a next operation? (y or n)\n")

        if(answear == 'n'):
            break
        else:
            num1 = result

calculate()