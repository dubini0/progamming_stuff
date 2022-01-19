from math import ceil

def is_palindrome(input_string):
    while True:
        flag = 1
        strlen = len(input_string)
        
        for i in range(ceil(strlen/2), strlen, 1):
            #print(i, strlen-i-1)
            if input_string[i] != input_string[strlen-i-1]:
                flag = 0
                break
        
        return flag

if __name__ == "__main__":
    print("A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward.")
    print("For example, madam or racecar.")
    print("This is a program that determines whether a string is a palindrome or not.")
    print("This program can manage English, Korean, and numbers")
    print("Enter what you want to check : ", end='')
    input_string = input()
    is_pal = is_palindrome(input_string)
    if is_pal:
        print("Yes, it is a palindrome.")
    else:
        print("Nope. It's not a palindrome.")
