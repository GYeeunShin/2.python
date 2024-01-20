length=int(input("Please enter the number of inches: "))
mile1=length//63360
mile2=length%63360

yard1=mile2//36
yard2=mile2%36

feet1=yard2//12
feet2=yard2%12

print(f"{mile1}mi",f"{yard1}yd",f"{feet1}'",f"{feet2}\"")
