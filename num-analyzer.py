print("======================== NUM ANALYZER ==================================")

numbers=[]
num_of_num=0
sum_accomolator=0
smallest=0
largest = 0
even_accomolator=0
odd_accomolator=0

while num_of_num < 10:
    number = int(input(f"Enter number {num_of_num+1}: "))
    sum_accomolator+=number
    if number > largest: largest=number
    if number < smallest: smallest = number
    if number % 2 == 0:
        even_accomolator+=1
    else:
        odd_accomolator+=1
        
    num_of_num+=1
    
print("=======================================================\n")
print(f"the largest number is {largest}")
print(f"the smallest number is {smallest}")
print(f"the sum of the number is {sum_accomolator}")
print(f"the average is {round(sum_accomolator/10,2)}")
print(f"there are {even_accomolator} even numbers")
print(f"there are {odd_accomolator} odd numbers")


print("\n========================================================")