def EncryptOrDecrypt():
    count = 0
    while count == 0:
        mode = str(input("Encrypt or Decrypt? "))
        if mode == "encrypt" or mode == "Encrypt" or mode == "E" or mode == "e":
            count = count + 1
        elif mode == "decrypt" or mode == "Decrypt" or mode == "D" or mode == "d":
            count = count + 1
        elif mode == "end" or mode == "End" or mode == "X" or mode == "x":
            break
        else:
            print("You need to enter in a valid answer. Please try again. ")
    return mode


history = []


def cipher(history):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    translated_message = ''

    index = 0
    yeet = True
    while yeet:
        message = input("Enter message text: ")

        key = input("Set shift offset ")
        mode = EncryptOrDecrypt()
        for character in message:
            if character in letters:
                number = letters.find(character)
                if mode == "encrypt" or mode == "Encrypt" or mode == "E" or mode == "e":
                    number = number + (ord(key[index]) - ord('a'))
                elif mode == "decrypt" or mode == "Decrypt" or mode == "D" or mode == "d":
                    number = number - (ord(key[index]) - ord('a'))
                elif mode == "end" or mode == "End" or mode == "X" or mode == "x":
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
        history.append(translated_message)
        return translated_message


yeet = True
while yeet:
    start = input("Do you want to use the cipher? ")
    if start == "yes":
        print(cipher(history))
    elif start == "history":

        for item in history:
            print(item)
    elif start == "no" or start == "No":
        print("Thank you for using this tool, Goodbye")

        yeet = False
    else:
        print("please enter either yes, no, or history to continue")
