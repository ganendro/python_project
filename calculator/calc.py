import os
from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return (n1/n2)

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}

def calculator():
    print(logo)

    num1=float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    cont =True

    while cont:
        ops_symbol = input("Pick operation: ")
        num2=float(input("what is the second number?: "))
        ops_func = operations[ops_symbol]
        answer=ops_func(num1,num2)
        print(f"{num1} {ops_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1=answer
        else:
            cont=False
            os.system('clear')
            calculator()

calculator()
        
        




