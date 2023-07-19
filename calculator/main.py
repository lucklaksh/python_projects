from replit import clear
from art import logo
def add(a,b):
    return a+b
def subtract(a, b):
    return  a-b
def multiply(a, b):
    return a*b
def divide (a,b):
    return a/b

operation ={
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

while True:
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operation:
        print(symbol)
    cont = 'y'
    while (cont != 'n'):
        op = input("Pick an Operation: ")
        num2 = float(input("What's the Second number?: "))
        operation_function = operation[op]
        result = operation_function(num1, num2)
        print(f"{num1} {op} {num2} = {result}")
        check = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if (cont == check):
            num1 = result
        else:
            cont = 'n'
    clear()
