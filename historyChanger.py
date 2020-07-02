# this file will be used to clear csv and txt files
import csv

loop = True
while loop:
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
        loop = False
