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
    else:
        print("Please enter either text, csv or end to continue")
