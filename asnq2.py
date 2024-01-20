import random
word_list = ['apple','alias','alloy','banana','bongo','bogey','category','chains']

def get_secret(): #importing random word and storing it in a variable 'secret'
    secret=random.choice(word_list)
    return secret

def display_guess(display_string,missed):
    print("Missed: ",missed,"times",end="      ")
    print("Word:",display_string)
    
    while True: 
        guess=input("Guess a letter: ")
        print()
        if len(guess)!=1:#checking if the user's guess is one letter long
            print("Enter a single letter")
        else:
            return guess

def new_display_string(secret,display_string,guess):
    new="" #empty string to store the user's status
    for i in range(len(secret)):
         if secret[i]==guess:
             new+=guess.upper()
             new+=" " 
         else:
            new+=display_string[2*i] #printing the '_'(considering the space between each '_')
            new+=" "                 

    return new

def main():
    print("Welcome to Guessing Game!!")
    print("   _______________                        |* \\_/*|________")
    print("  |  ___________  |                       ||_/-\\_|______  |")
    print("  | |           | |                       | |           | |")
    print("  | |   0   0   | |                       | |   0   0   | |")
    print("  | |     -     | |                       | |     -     | |")
    print("  | |   \\___/   | |                       | |   \\___/   | |")
    print("  | |___     ___| |                       | |___________| |")
    print("  |_____|\\_/|____|                        |_______________|")
    print("    _|__|/ \\|_|_.......Getting Word........._|________|_")
    print("   / ********** \\                          / ********** \\")
    print()
    
    secret=get_secret()
    display_string="_ "*len(secret)
    missed=0
    total=0

    
    while True:
        total+=1
        guess= display_guess(display_string,missed)
        
        if guess in secret:
            display_string=new_display_string(secret,display_string,guess)
        else:
            missed+=1

        if "_" not in display_string:
            print("Correct! The word was",secret.upper())
            print("Solved using",total,"guesses")
            break



main()
         
    
    
