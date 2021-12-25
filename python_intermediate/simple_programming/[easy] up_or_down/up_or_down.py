# Very simple up and down game.
# Can be only played once, with no score counting.
# This will be worked on intermediate / hard levels.
import random

def print_menu():
    print("Welcome to Up and Down!!")
    print("A number between 0-100 will be generated")
    print("You will get 6 chances to guess that number!")
    print("Do you want to play? 'Y' for yes, and 'N' for no~.~")
    
def play_game():
    randint = random.randint(0, 101)
    for i in range(6):
        user_answer = int(input("Give me your guess : "))
        
        # range check
        while user_answer < 0 or user_answer > 100:
            print("hey, the random int is between 0-100. Try again.")
            user_answer = int(input("Give me your guess : "))
        
        if randint == user_answer:
            print("You got it right! good job XD")
            return True
        elif randint < user_answer:
            print("The random number is smaller than that!")
        else:
            print("The random number is bigger than that!")
            
    print(f"Too bad! The random nubmer was {randint}")
    return False
    
if __name__ == "__main__":
    print_menu()
    gogo = input()
    if gogo == 'Y':
        play_game()
    else:
        print("Thanks for playing! Bye~")
