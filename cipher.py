def EncryptOrDecrypt():
    count = 0
    encrypt = ["Encrypt", "encrypt", "E", "e"]
    decrypt = ["Decrypt", "decrypt", "D", "d"]
    end = ["End", "end", "X", "x"]
    while count == 0:
        mode = str(input("Encrypt or Decrypt? "))
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


def cipher(history):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    translated_message = ''
    encrypt = ["Encrypt", "encrypt", "E", "e"]
    decrypt = ["Decrypt", "decrypt", "D", "d"]
    end = ["End", "end", "X", "x"]
    index = 0
    yeet = True
    while yeet:
        message = input("Enter message text: ")

        key = input("Set shift offset ")
        mode = EncryptOrDecrypt()
        for character in message:
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
        history.append(translated_message)
        return translated_message


yes = ["Yes", "yes", "y", "Y"]
no = ["No", "no", "n", "N"]
yeet = True
while yeet:
    start = input("Do you want to use the cipher? ")
    if start in yes:
        print(cipher(history))
    elif start == "history":

        for item in history:
            print(item)
    elif start in no:
        print("Thank you for using this tool, Goodbye")

        yeet = False
    else:
        print("please enter either Yes, No, or History to continue")
