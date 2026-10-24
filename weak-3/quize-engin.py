
print("=========================== Reusable Quiz Engine ===========================")

questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correctAnswer": "Mars"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Ag", "Fe", "Au", "Pb"],
        "correctAnswer": "Au"
    },
    {
        "question": "Which organ in the human body pumps blood?",
        "options": ["Lungs", "Brain", "Heart", "Liver"],
        "correctAnswer": "Heart"
    },
    {
        "question": "What does HTTP stand for?",
        "options": [
            "HyperText Transfer Protocol",
            "High-Level Task Tracking Program",
            "Hyperlink Text Technology Protocol",
            "Home Tool Transfer Package"
        ],
        "correctAnswer": "HyperText Transfer Protocol"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "correctAnswer": "7"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correctAnswer": "Carbon Dioxide"
    },
    {
        "question": "What is the capital city of Japan?",
        "options": ["Kyoto", "Osaka", "Tokyo", "Hiroshima"],
        "correctAnswer": "Tokyo"
    },
    {
        "question": "Which is an immutable data type in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "correctAnswer": "Tuple"
    }
]


# Display a question
def display_question(question, number):
    print(f"\nQuestion {number}: {question['question']}")

    print("A.", question["options"][0])
    print("B.", question["options"][1])
    print("C.", question["options"][2])
    print("D.", question["options"][3])


# Validate the answer
def validate_answer(answer):
    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
        return True
    else:
        return False


# Check whether the answer is correct
def check_answer(answer, question):
    if answer == "a":
        selected_answer = question["options"][0]
    elif answer == "b":
        selected_answer = question["options"][1]
    elif answer == "c":
        selected_answer = question["options"][2]
    else:
        selected_answer = question["options"][3]

    if selected_answer.lower() == question["correctAnswer"].lower():
        return True
    else:
        return False


# Update the score
def update_score(score, is_correct):
    if is_correct:
        score["correct"] += 1
    else:
        score["incorrect"] += 1


# Display the final results
def display_results(score):
    total = score["correct"] + score["incorrect"]

    percentage = score["correct"] / total * 100

    print("\n========== FINAL RESULTS ==========")
    print("Total questions:", total)
    print("Correct answers:", score["correct"])
    print("Incorrect answers:", score["incorrect"])
    print("Final score:", str(score["correct"]) + "/" + str(total))
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Category: Excellent!")
    elif percentage >= 60:
        print("Category: Good job!")
    elif percentage >= 40:
        print("Category: Keep practicing!")
    else:
        print("Category: More practice needed!")


# Run the quiz
def run_quiz():
    score = {
        "correct": 0,
        "incorrect": 0
    }

    for number in range(len(questions)):
        question = questions[number]

        display_question(question, number + 1)

        while True:
            answer = input("Your answer (A/B/C/D): ").lower().strip()

            if validate_answer(answer):
                break
            else:
                print("Invalid option! Enter A, B, C, or D.")

        if check_answer(answer, question):
            print("Correct!")
            update_score(score, True)
        else:
            print("Incorrect!")
            print("Correct answer:", question["correctAnswer"])
            update_score(score, False)

    display_results(score)


def controller():
    while True:
        run_quiz()

        replay = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if replay == "no" or replay == "n":
            print("Thank you for playing!")
            break
        elif replay == "yes" or replay == "y":
            print("\nStarting a new quiz...")
        else:
            print("Invalid choice. The quiz will end.")
            break


controller()
