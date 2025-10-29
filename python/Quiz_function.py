def display_welcome():
    print("Welcome to the Quiz Game!")
    print("------------------------")


def ask_question(question, option1, option2, option3, option4, correct):
    print("\n" + question)
    print("1. " + option1)
    print("2. " + option2)
    print("3. " + option3)
    print("4. " + option4)
    
    answer = int(input("Enter your answer (1-4): "))
    
    match answer:
        case correct:
            print("Correct")
            return 1
        case _:
            print("Wrong!")
            return 0


def show_score(score):
    print("\n=== Quiz Over ===")
    print("You got " + str(score) + " out of 3")
    
    match score:
        case 3:
            print("Perfect! You're a genius!")
        case 2:
            print("Good job!")
        case 1:
            print("Not bad, try again!")
        case 0:
            print("Better luck next time!")
    print("=================")


def run_quiz():
    display_welcome()
    
    score = 0
    
   
    score = score + ask_question(
        "What is the capital of France?",
        "Paris", "London", "Berlin", "Rome", 1
    )
    
 
    score = score + ask_question(
        "Where is Semicolon located?",
        "Ikeja", "Sabo Yaba", "Yaba Sabo", "Ikotun", 2
    )
    
    
    score = score + ask_question(
        "What is the color of Nigeria Flag?",
        "Green,white", "White,Green", "Green,Green", "Green,White,Green", 4
    )
    
  





