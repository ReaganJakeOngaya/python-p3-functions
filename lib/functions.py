#!/usr/bin/env python3

def greet_programmer():
    print('Hello developer')
greet_programmer()

def greet(name):
    print(f'Hello, {name}')
greet('Reagan')

def greet_with_default(name="programmer"):
    print(f'hello , {name}')
greet_with_default()

def add(num1, num2):
    print(
        num1 + num2
    )

add( 3, 5)

def halve(number):
    print(
        int(number/2)
    )
halve(8)
