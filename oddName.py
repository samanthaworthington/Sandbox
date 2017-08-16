"""Samantha Worthington"""

name = str(input("What is your name? "))
while len(name)<= 0:
    print("No name entered")
    name = str(input("What is your name? "))

print(name[0:len(name):2])






