print ("Welcome to SirTime's Shift Cipher Program.")
print ("----------------------------------------")
option = input("Please type '1' to encode and '2' to decode\n\n")

if (int(option) == 1): 
    encode = input("Ok, Please type in the message you want to encode\n\n")
    shift = input("Please enter the shift value from 1 to 5\n\n")
    if ((int(shift) >= 1) and (int(shift)<= 5)):
        cipher = ""
        for character in encode:
            ascvalue = (ord(character) + int(shift))
            strvalue = (chr(ascvalue))
            cipher = cipher + strvalue
        print (cipher + "\n")
        
    else:
        print("Invalid input. Please enter the shift value from 1 to 5")

elif (int(option)== 2):
    decode = input("Ok, Please type in the message you want to decode\n\n")
    shift = input("Please enter the shift value from 1 to 5\n\n")
    if ((int(shift) >= 1) and (int(shift)<= 5)):
        cipher = ""
        for character in decode:
            ascvalue = (ord(character) - int(shift))
            strvalue = (chr(ascvalue))
            cipher = cipher + strvalue
        print (cipher + "\n")
    
else :
    print ("Your input is invalid ! Please type '1' to encode and '2' to decode\n\n")
