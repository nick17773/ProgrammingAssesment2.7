import json


# this function declares the selection for the mode of the cipher, either encryption, decryption or end
def EncryptOrDecrypt():
    count = 0
    encrypt = ["Encrypt", "encrypt", "E", "e"]  # list of possible inputs that will be taken to use as encrypt
    decrypt = ["Decrypt", "decrypt", "D", "d"]  # list of possible inputs that will be taken to use as decrypt
    end = ["End", "end", "X", "x"]  # list of possible inputs that will be taken to end the program
    while count == 0:
        mode = str(input("Encrypt or Decrypt? "))  # input that asks the user whether they will encrypt or decrypt
        if mode in encrypt:
            count = count + 1
        elif mode in decrypt:
            count = count + 1
        elif mode in end:
            break
        else:
            print("You need to enter in a valid answer. Please try again. ")
    return mode


history = []


# cipher function
def cipher(history):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    translated_message = ''
    encrypt = ["Encrypt", "encrypt", "E", "e"]  # same as above list for encrypt
    decrypt = ["Decrypt", "decrypt", "D", "d"]  # same as above list for decrypt
    end = ["End", "end", "X", "x"]  # same as above list for end
    index = 0
    yeet = True
    while yeet:  # while loop that keeps the cipher running until the user chooses to end.
        message = input("Enter message text: ")

        key = input("Set shift offset ")
        mode = EncryptOrDecrypt()
        for character in message:  # encryption/decryption method
            if character in letters:
                number = letters.find(character)
                if mode in encrypt:
                    number = number + (ord(key[index]) - ord('a'))
                elif mode in decrypt:
                    number = number - (ord(key[index]) - ord('a'))
                elif mode in end:
                    pass
                index = index + 1
                index = index % len(key)

                if number >= len(letters):
                    number = number - len(letters)
                elif number < 0:
                    number = number + len(letters)

                translated_message = translated_message + letters[number]



            else:
                translated_message = translated_message + character
        history.append(translated_message)  # appends the translated message to history to be used later
        return translated_message


yes = ["Yes", "yes", "y", "Y"]  # list for possible clauses to be used to continue the loop relating to yes
no = ["No", "no", "n", "N"]  # list for possible clauses to be used to end the loop relating to no
yeet = True  # variable that keeps the loop running
while yeet:  # loop that continues the cipher until the user opts out.
    start = input("Do you want to use the cipher? ")  # input that asks the user if they want to use the cipher
    if start in yes:  # if statement that allows the user to run the cipher
        print(cipher(history))  # print statement that runs the cipher function
    elif start == "history":  # elif statment that allows the user to view the history of their translated inputs
        for item in history:  # for loop that prints everything in the history list
            print(item)
    elif start in no:  # elif statment that allows the user to end the loop for the cipher
        print(
            "Thank you for using this tool, Goodbye")  # print statment that that runs a message when the user ends the loop

        yeet = False
    else:  # else statment that runs when the user doesn't input the correct value
        print("please enter either Yes, No, or History to continue")

# open output file for writing
with open('cipherHistory.txt',
          'w') as filehandle:  # with statement that outputs the history to a text file, which is overwritten everytime the loop is run
    for listitem in history:
        json.dump(history, filehandle)
