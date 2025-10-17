num1 = input()
operation = input()
num2 = input()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b
    
def multiply(a, b):
    return a * b

def squareRoot(a):
    if a < 0:
        return "Error: Square root of negative number"
    else:
        return a ** 0.5
    
def power(a, b):
    return a ** b

match operation:
    case "+":
        print(add(num1, num2))
    case "-":
        print(subtract(num1, num2))    
    case "/":
        print(division(num1, num2))
    case "*":
        print(multiply(num1, num2))
    case "sqrt":
        print(squareRoot(num1))
    case "^":
        print(power(num1, num2))