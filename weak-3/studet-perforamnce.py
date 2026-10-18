student_list = []
def add_student():

    name = input("Enter your name: ")
    
    while True:
        
        no_of_subjects = int(input("Enter number of subjects: "))
        if no_of_subjects <= 0 or no_of_subjects > 10:
            print("Number of subjects must be a positive integer between 1 and 10. Please try again.")
            continue
        
        if type(no_of_subjects) != int:
            print("Number of subjects must be an integer. Please try again.")
            continue
        break
    no_iterations = no_of_subjects
    total_score = 0

    
    while no_iterations > 0:
        score=float(input("Enter your score: "))
        if score < 0 or score > 100:
            print("Score must be between 0 and 100. Please try again.")
            continue
        
        if type(score) != float and type(score) != int:
            print("Score must be a number. Please try again.")
            continue
        
        total_score += score
        no_iterations -= 1
        average = calculate_average_score(total_score, no_of_subjects)
    student_list.append({'name': name, "sum": total_score, 'average_score': average, 'grade': generate_grade(average)})


def calculate_average_score(total_score, number_of_subjects):
    if number_of_subjects == 0:
        return 0    
    return total_score / number_of_subjects

def generate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

def highest_lowest():
    highest = student_list[0]["average_score"]
    lowest = student_list[0]["average_score"]
    for student in student_list:
        if student["average_score"] > highest:
            highest = student["average_score"]
        if student["average_score"] < lowest:
            lowest = student["average_score"]
            
    return highest, lowest
    

def count_pass_fail():
    pass_count = 0
    fail_count = 0
    for student in student_list:
        if student["average_score"] > 60:
            pass_count += 1
        else:
            fail_count += 1
    return pass_count, fail_count

def generate_report():
    print("=====================Students Performance Report=======================")
    print("Name\t\tTotal Score\tAverage Score\tGrade")
    print("-----------------------------------------------------------------------")
    for student in student_list:
        print(f"{student['name']}\t\t{student['sum']}\t\t{student['average_score']}\t\t{student['grade']}")
        
  
def generate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'
    
    
print("===================Students Performance analyzer=======================")
while True:
    
    choice = input("\nEnter \n1. To add student \n2. To view students report \n3. To exit \nYour choice: ")

    match choice:
        case "1":
            add_student()
            
        case "2":
            generate_report()
            
        case "3":
            print("Exiting the program...")
            break
        
        case _:
            print("Invalid choice. Please try again.")
            continue