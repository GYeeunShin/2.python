import random
print("Welcome to Witches, Orges, and Robbers: ")
print("       *                  ((((")
print("*            *        *  (((")
print("       *                (((      *")
print("  *   / \\        *     *((( ")   
print("   __/___\\__  *          (((")
print("    (O)  |         *     ((((")
print("*  '<   ? |__ ... .. .             *")
print("     \\@      \\    *    ... . . . *")
print("     //__     \\")
print("    // ||\\__  \ \    |~~~~~~ . . .   *")
print("====M===M===| |=====|~~~~~~   . . .. .. .")
print("         *  \\ \\ \\   |~~~~~~    *")
print("  *         <__|_|   ~~~~~~ .   .     ... .")

print()
user=input("Choose (w)itch, (o)rge, (r)obber: ")
program=random.randint(1,3)
#1 = witch, 2= orge, 3=robber
flag=False
computer_counter=0
user_counter=0

while (not flag):
    if (user=="w"): #if the user enters Witch
        if (program== 1):
            print("Computer: witch")
            print("User: witch")
            print("Tie!")
        elif (program == 2):
            print("Computer: orge")
            print("User: witch")
            print("You Win!")
            user_counter+=1
        else:
            print("Computer: robber")
            print("User: witch")
            print("Computer Win!")
            computer_counter+=1
            
    elif (user == "o"): #if the user enters Orges
         if (program== 1):
            print("Computer: witch")
            print("User: orge")
            print("Computer Win!")
            computer_counter+=1
         elif (program == 2):
            print("Computer: orge")
            print("User: orge")
            print("Tie!")
            
         else:
            print("Computer: robber")
            print("User: orge")
            print("You Win!")
            user_counter+=1

    elif (user == "r"): #if the user enters Robbers
         if (program== 1):
            print("Computer: witch")
            print("User: robber")
            print("You win!")
            user_counter+=1
         elif (program == 2):
            print("Computer: orge")
            print("User: robber")
            print("Computer Win!")
            computer_counter+=1
         else:
            print("Computer: robber")
            print("User: robber")
            print("Tie!")

    print()
    again=input("Play again (y)es (n)o? ")
    again=again.lower()
    if (again == "y"):
        user=input("Choose (w)itch, (o)rge, (r)obber: ")
        program=random.randint(1,3)

    else:
        flag=True #exiting the game
   

print("Computer: ",computer_counter)
print("User: ",user_counter)

if (computer_counter>user_counter):
    print("ᯅ̈")
    print("Computer Wins")
elif(user_counter>computer_counter):
    print("⎝⍢⎠")
    print("User wins")
else:
    print("Tie")


        
