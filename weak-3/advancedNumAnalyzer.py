print("=====================Advanced Number Analyzer ===========================")

def is_prime(number):
    if number == 1 and number > 0:
        return "not prime"
    counter = 0
    
    for i in range(2, number):
        if number % i == 0:
            
            counter += 1
            
    if counter > 0:
        return "not prime"
    else:
        return "prime"

def sum_of_digits(number):
    sum=0
    for i in str(number):
        sum+=int(i)
    return sum

def get_divisor(number):
    devisors = []
    for i in range(number):
        i+=1
        if number%i==0:
            devisors.append(i)
    return devisors
    

def reverse_number(number):
        
    return str(number)[::-1]
        
       
       
def analyze_num():
    number = 123
    
    print("the number is ",is_prime(number))
    print("the sum of the digit is",sum_of_digits(number))
    print("when the number reversed", reverse_number(number))
    print("its devisors are", get_divisor(number))
    

analyze_num()
        
print("/----------------------------------------------------------------------/")
    
#     print(str(number))
   
# print(reverse_number(123))
# print(sum_of_digits(4543))
    
# print(get_divisor(9))
# print(is_prime(9))