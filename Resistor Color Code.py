import os # Imports a command from the operating system (used on Line 121).

def Sanitizer(x): # Runs a function to sanitize the input so there are no errors.
    if x.isdigit() and 1 <= int(x) <= 10:       #Checks if the number is equal to or between 1 and 10.
        x = int(x) - 1                          #Subtracts the input by 1.
    else:                                       #If the input was not equal to or between 1 and 10 then it runs this line.
        print ("Please enter a valid number.")  #Error message.
    return x                                    #Returns x

def BandA(): # Runs the function to
    print ("What is the color of Band 1?")
    print ("1. Black")
    print ("2. Brown")
    print ("3. Red")
    print ("4. Orange")
    print ("5. Yellow")
    print ("6. Green")
    print ("7. Blue")
    print ("8. Violet")
    print ("9. Gray")
    print ("10. White")
    Band1 = input ("> ")
    Band1 = Sanitizer(Band1)
    return Band1

def BandB():
    print ("What is the color of Band 2?")
    print ("1. Black")
    print ("2. Brown")
    print ("3. Red")
    print ("4. Orange")
    print ("5. Yellow")
    print ("6. Green")
    print ("7. Blue")
    print ("8. Violet")
    print ("9. Gray")
    print ("10. White")
    Band2 = input ("> ")
    Band2 = Sanitizer(Band2)
    return Band2

def BandC():
    print ("What is the color of Band 3?")
    print ("1. Black")
    print ("2. Brown")
    print ("3. Red")
    print ("4. Orange")
    print ("5. Yellow")
    print ("6. Green")
    print ("7. Blue")
    print ("8. Violet")
    print ("9. Gray")
    print ("10. White")
    print ("11. Gold")
    print ("12. Silver")
    Band3 = input ("> ")
    if Band3.isdigit() and 1 <= int(Band3) <= 12:
        Band3 = int(Band3) - 1
        Band3 = 10 ** Band3
    else:
        print ("Please enter a valid number.")
    if Band3 == 10:
        Band3 = 0.1
    elif Band3 == 11:
        Band3 = 0.01
    return Band3

def BandD():
    print ("What is the color of Band 4?")
    print ("1. Brown")
    print ("2. Red")
    print ("3. Yellow")
    print ("4. Green")
    print ("5. Blue")
    print ("6. Violet")
    print ("7. Gray")
    print ("8. Gold")
    print ("9. Silver")
    print ("10. None")
    Band4 = input ("> ")
    Band4 = Sanitizer(Band4) + 1
    if Band4 == 3:
        Band4 = 5
    elif Band4 == 4:
        Band4 = 0.5
    elif Band4 == 5:
        Band4 = 0.25
    elif Band4 == 6:
        Band4 = 0.1
    elif Band4 == 7:
        Band4 = 0.05
    elif Band4 == 8:
        Band4 = 5
    elif Band4 == 9:
        Band4 = 10
    elif Band4 == 10:
        Band4 = 20
    return Band4

while 1:
    print ("Resistor Color Code")
    print ("")
    Band1 = BandA()
    print ("")
    Band2 = BandB()
    Value = str(Band1) + str(Band2)
    print ("")
    Band3 = BandC()
    Value = float(Value) * Band3
    print ("")
    Band4 = BandD()
    print ("")
    print ("The resistance is: " + str(round(Value)) + " Ohms.")
    print ("The tolerance is: " + str(Band4) + "%")
    print ("")
    print ("Press <1> before <Enter> to exit program or press <Enter> to continue.")
    Key = input (">> ")
    if Key == "1":
        quit()
    else:
        os.system(['clear','cls'][os.name == 'nt'])
