import csv

loop = True
while loop:
    fileType = input("What file type would you like to load? ")
    if fileType == 'csv':
        with open('cipherHistory.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        with open('output.csv', 'a+') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerows(data)
        print("Values appended to output.csv")
    elif fileType == 'text':
        with open('cipherHistory.txt', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        with open('output.txt', 'a+') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerows(data)
        print("Values appended to output.txt")
    elif fileType == "end":
        loop = False

    elif fileType == "clear":
        loop2 = True
        while loop2:
            toClearOrNotToClear = input("Do you want to clear the files? ")
            txtfile = "cipherHistory.txt"
            csvfile = "cipherHistory.csv"
            if toClearOrNotToClear == "yes":
                with open(txtfile, "w") as output:  # with statement that outputs the history to a text file
                    writer = csv.writer(output, lineterminator='\n', dialect='excel')
                    writer.writerows("")
                with open(csvfile, "w") as output:  # with statement that outputs the history to a text file
                    writer = csv.writer(output, lineterminator='\n', dialect='excel')
                    writer.writerows("")
                print("Files have been cleared")
            else:
                print("Data is still stored, goodbye")
                loop2 = False
    else:
        print("Please enter either text, csv, clear or end to continue")
