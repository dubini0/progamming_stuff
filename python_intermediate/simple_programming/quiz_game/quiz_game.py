import random
import time
import sys

def print_menu():
    print("Welcome to the quiz game!!")
    print("To start input 'Y', to exit input 'N'")
    
def play_game():
    calculating_text = "......Calculating......"
    with open('questions.txt', 'r') as q, open('answers.txt', 'r') as a:
        questions = q.readlines()
        answers = a.readlines()
    question_len = len(questions)
    
    n = random.randint(0, question_len)
    print(f"Question : {questions[n]}")
    user_answer = input("Answer : ")
    for i in range(len(calculating_text)):
        sys.stdout.write(f"{calculating_text[i]}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()
        
    if user_answer == answers[n]:
        print("Congratulations!! You got it right:)")
        return True
    else:
        print(f"Too bad... The answer was : {answers[n]}")
        return False

if __name__ == "__main__":
    print_menu()
    while True:
        gogo = input()
        if gogo == 'Y':
            get_right = play_game()
            if get_right:
                print("Good job!")
            else:
                print("Too bad!")
            print("Do you want to play again?")
            print("Input 'Y' to keep playing, and 'N' for exit!")
        elif gogo == 'N':
            print("Thanks for playing!")
            exit()
        else:
            print("Please input an valid choice")
    