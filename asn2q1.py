def sub(string,substring):
    for p in range(len(string)-len(substring)+1): #starting letter
       result=True
       for q in range(len(substring)): 
           if (string[p+q]!=substring[q]):
               #if the starting letter of substring is in string
               #nested for loop will continue checking for the
               #rest of the substring letters
               result=False
               break
       if result: #if the substring is found in the string
           return True

    return False 

substring=input("enter a substring: ")
string=input("enter a string: ")
result = sub(string,substring)
if result:
    print("the substring",substring,"is in",string)
else:
    print("the substring",substring,"is not in",string)
