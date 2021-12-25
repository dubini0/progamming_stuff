import random

user_wins = 0
computer_wins = 0
options = ['R', 'P', 'S']

def print_menu():
    print("Welcome to Rock-Paper-Scissors.")
    print("Do I really have to tell you what this is?")

def who_wins(user_input, com_pick):
    if user_input == 'R':
        if com_pick == 'S':
            return 1
        elif com_pick == 'P':
            return 0
        else:   return -1
    elif user_input == 'S':
        if com_pick == 'P':
            return 1
        elif com_pick == 'R':
            return 0
        else:   return -1
    else:
        if com_pick == 'R':
            return 1
        elif com_pick == 'S':
            return 0
        else:   return -1
        
    
if __name__ == "__main__":
    print_menu()
    while True:
        print(f"Current Score (You vs. Computer) = {user_wins} : {computer_wins}")
        print("Type 'R', 'P', 'S' for Rock/Paper/Scissors or Q to quit.")
        user_input = input("Your input : ").upper()
        if user_input in options:
            #rock: 0, paper: 1, scissors: 2
            com_pick = options[random.randint(0, 2)]
            print(f"computer picked : {com_pick}, you picked : {user_input}")
            #result; 0-> computer wins, 1-> user wins, -1-> draw
            result = who_wins(user_input, com_pick)
            if result == 0:
                print("Too bad:(")
                computer_wins += 1
            elif result == 1:
                print("Congrats!")
                user_wins += 1
            else:
                print("It's a draw. Nobody gets a point.")
                
        elif user_input == 'Q':
            print('Thanks for playing!')
            exit()
        else:
            print("type something valid please")