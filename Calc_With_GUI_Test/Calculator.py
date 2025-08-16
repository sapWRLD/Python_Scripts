import math
from tkinter import *
from tkinter import ttk


numbers = []
run = True


def add():
    for i in numbers:
        for j in numbers+1:
            return i + j
    return
def subtract():
    for i in numbers:
        for j in numbers+1:
            return i - j
    return
def multiply():
    for i in numbers:
        for j in numbers+1:
            return i * j
    return
def divide():
    for i in numbers:
        for j in numbers+1:
            return i / j
    return
operation = {   "+": add,
                "-": subtract,
                "*": multiply,
                "/": divide}



def main():
    while run is True:
        user_Input = input("geef je getallen in")
        parts = user_Input.split()
        if user_Input == "quit":
            run = False
if __name__ == "__main__":
    main()       
