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

