# name= input("what is your name: ")

# print("hello,",name )

"""
this is a multiple line comment in python

"""

# name=name.strip().title()

# PRINT FUNCTION 

# print("tehdi", name, end="",sep=" ")


# first, last = name.split(" ")

# print("hello", last)

# =============================================================================

"""x=float(input("enter the first num: "))
y=float(input("enter the second num: "))

print(f"{x+y:.2f}")"""

# =============================================================================

# FUNCTION IN PYTHON

# def hello(to="world"):
#     print("hello", to)

# hello()
# acceptor=input("what is your name: ")
# hello(acceptor)
# =============================================================================

# conditinals in python

# number_1=int(input("enter a number: "))
# number_2=int(input("enter another number: "))

# if number_1>number_2:
#     print("the first number is greater than the second number")
    
# elif number_1<number_2:
#     print("the second is greater than the first number ")
    
# else:
#     print("they are equal")

# =============================================================================
# the or operator

# if not number_1 > number_2 or not(number_1 < number_2):
#     print("the first number is equal to the second numbrer")


# def is_even(n):
    # if n%2==0:
    #     return True
    # else:
    #     return False
    
    
    # or
    
    # return True if n%2==0 else False
    
    # or
    
    
    # return n % 2 == 0
    
    
# even_num=int(input("enter a number that you wnat to test the eveness: "))

# print(is_even(even_num))
# =============================================================================

# match in python

# match even_num:
#     case 12:
#         print("it is twelve")
#     case 1:
#         print("this is number one")
#     case _:
#         print("not recognized")        

# =============================================================================

# loops
# num=5

# while num > 0:
#     print("meow")
#     num-=1


# we can also do this by using for loop

# for _ in range(3):
#     print("meow")
    
# for i in [1,3,5,5,7,4,343,4,343,43,]:
#     print(i)
    
# print("meow\n"*3)

# def return_posetive():
    
#     while True:
#         num=int(input("enter sth"))
    
#         if num>0:
#             print(num)
#             return num
    
#         print("enter a posetive number")
# =============================================================================

# python dictionary

# fam = {
#     "tehdi": "seid",
#     "seid": "dad",
#     "fatima": "mom",
#     "muju": "brother",
    
# }

# for family in fam:
#     print(family, fam[family], sep=", ")
    
    
# # nested for loop

# for _ in range(4):
#     for _ in range(4):
#         print("#", end="")
        
#     print()
# =============================================================================
# exeptions in python 


# try:
#     num=int(input("what is x: "))
    
# except ValueError as error:
#     print(f"x is not an intiger {error}")
    
    
# else:
    
#     print(num)

# while True:
#     try:
#         num=int(input("what is x: "))
        
#     except ValueError as error:
        
#         print(f"x is not an intiger {error}")
#     else:
#         break
# print(f"x is {num}")

        
# =============================================================================

# python liberaries

# import random 

# print(random.choice([1,2,3,4,5,1,4,4,6,3,6,3]))
# # it generates a random intiger number between 1 and 6
# print(random.randint(1,6))

# lists=["quen", "joker", "a", "1", "2"]
# random.shuffle(lists)
# print(lists)


# =============================================================================

# statistics module is python

# import statistics

# print(statistics.median([1,2,3,4,5,1,4,4,6,3,6,3]))

# print(statistics.mean([12,43,34,63,55,3,56,35,345,34]))

# print(f"{12000:,}")

# =============================================================================

# the sys liberary in python
# import cowsay  

# import sys
# print(sys.path)


# if len(sys.argv)<2:
#     sys.exit("to few argument")


# for arg in sys.argv[1:]:
#     print("name:",arg)
#     print(cowsay.trex(f"hello, {arg}"))
  

# =============================================================================

# API in python
# import requests
# import json

# data=requests.get("https://jsonplaceholder.typicode.com/todos/")

# print(json.dumps(data.json(), indent=2))
# # for datas in data.json():
# #     print(datas["userId"])

# def main():
    
#     print(square(3))


# def square(num):
#     return num * num


# if __name__=="__main__":
#     main()
# =============================================================================

# UNIT TESTINNG IN PYTHON

# =============================================================================

# file operations in python
# name = input("enter your name: ")
# file = open("name.txt", "w")

# file.write(name)
# file.close()
# =============================================================================

# with oopen in file i/o its advantage is to remove saying close all the time

# with open("name.txt", "a") as file:
    # file.write(f"{name}\n")


    
# import csv
    
# with open("name.csv", "r") as file:
#     reader = csv.reader(file)
#     lines = file.readlines()
#     lilst=[]

#     for line in sorted(lines, key=lambda line: line["name"]):
#         name, value=line.rstrip().split(",")
#         list.append({
#             "name": name,
#             "value": value
#         })
#         print("name", name, "value", value)
        
        # print(line, end="")
        

    
# =============================================================================
# regular expresions in python

import re

email = input("Enter your email: ")

if re.search(r"^\w+@[^@]+\.com$", email):
    print("Valid")
else:
    print("Invalid")


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
