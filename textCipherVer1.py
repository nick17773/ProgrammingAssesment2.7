import csv

cipher_mode = ""


# this function declares the selection for the mode of the cipher, either encryption, decryption or end
def encryptOrDecrypt(cipher_mode):
    loop_count = 0
    encrypt = ["Encrypt", "encrypt", "E", "e"]  # list of possible inputs that will be taken to use as encrypt
    decrypt = ["Decrypt", "decrypt", "D", "d"]  # list of possible inputs that will be taken to use as decrypt
    end = ["End", "end", "X", "x"]  # list of possible inputs that will be taken to end the program
    while loop_count == 0:
        step3 = "Brilliant, you're almost finished. To continue, please choose either Encrypt or Decrypt to alter the given message with the given key. \n" \
                " -  Selecting Encrypt will jumble the given message based on the given key. \n" \
                " -  Selecting Decrypt will reverse the jumbling of the given message with the given key."
        print(step3)
        cipher_mode = str(
            input("Will you Encrypt or Decrypt? "))  # input that asks the user whether they will encrypt or decrypt
        if cipher_mode in encrypt:
            loop_count = loop_count + 1
        elif cipher_mode in decrypt:
            loop_count = loop_count + 1
        elif cipher_mode in end:
            break
        else:
            print("You need to enter in a valid answer. Please try again. ")
    return cipher_mode


message_history = []
key_history = []


# cipher function
def cipher(message_history, key_history, ):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    translated_message = ''
    encrypt = ["Encrypt", "encrypt", "E", "e"]  # same as above list for encrypt
    decrypt = ["Decrypt", "decrypt", "D", "d"]  # same as above list for decrypt
    end = ["End", "end", "X", "x"]  # same as above list for end
    index = 0
    loop = True
    while loop:  # while loop that keeps the cipher running until the user chooses to end.
        step1 = "Great! You chose to use this cipher tool. To continue, please enter a message you would like to use"
        print(step1)
        message = input("Enter message text: ")
        step2 = "Awesome, you've selected a message. To continue, please input a key (number, letter or word) you would like to use to change the message"
        print(step2)
        key = input("Enter key (number, word or letter): ")
        mode1 = encryptOrDecrypt(cipher_mode)
        for character in message:  # encryption/decryption method
            if character in letters:
                number = letters.find(character)
                if mode1 in encrypt:
                    number = number + (ord(key[index]) - ord('a'))
                elif mode1 in decrypt:
                    number = number - (ord(key[index]) - ord('a'))
                elif mode1 in end:
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
        message_history.append(translated_message)  # appends the translated message to history to be used later
        key_history.append(key)  # appends the key to history to be used later
        return translated_message


startMsg = "Hi, welcome to my cipher tool, If you would like to continue, type yes. If you decide you would like to cancel, type no." \
           "\nAll information inputted/outputted will be stored in both a csv and txt file when the program ends."
yes = ["Yes", "yes", "y", "Y"]  # list for possible clauses to be used to continue the loop relating to yes
no = ["No", "no", "n", "N"]  # list for possible clauses to be used to end the loop relating to no
go = True  # variable that keeps the loop running
step4 = "Well done! The above text is the encrypted or decrypted message, based on YOUR inputs. If you would like to continue, please type yes.\n" \
        "If you would like to view the history of what was outputted, and the keys used, please type history.\n" \
        "Otherwise, please type no."
print(startMsg)
while go:  # loop that continues the cipher until the user opts out.

    start = input("Do you want to use the cipher? ")  # input that asks the user if they want to use the cipher
    if start in yes:  # if statement that allows the user to run the cipher
        print(cipher(message_history, key_history, ))  # print statement that runs the cipher function
        print(step4)
    elif start == "history":  # elif statement that allows the user to view the history of their translated inputs
        for item in message_history:  # for loop that prints everything in the history list
            print(item)
        for item in key_history:
            print(item)

    elif start in no:  # elif statement that allows the user to end the loop for the cipher
        print(
            "Thank you for using this tool, Goodbye")  # print statement that that runs a message when the user ends the loop

        go = False
    else:  # else statement that runs when the user doesn't input the correct value
        print("Please enter either Yes, No, or History to continue")

txtfile = "cipherHistory.txt"
csvfile = "cipherHistory.csv"

with open(txtfile, "a+") as output:  # with statement that outputs the history to a text file
    writer = csv.writer(output, lineterminator='\n', dialect='excel')
    for val in message_history:
        writer.writerow([val])
    for val in key_history:
        writer.writerow([val])

with open(csvfile, "a+") as output:  # with statement that outputs the history to a csv file
    writer = csv.writer(output, lineterminator='\n', dialect='excel')
    for val in message_history:
        writer.writerow([val])
    for val in key_history:
        writer.writerow([val])
