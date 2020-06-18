import csv

loop = True
while loop:
    type = input("What file type would you like to load? ")
    if type == 'csv':
        with open('cipherHistory.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        with open('output.csv', 'w') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerows(data)
        print("Values written to output.csv")
    elif type == 'text':
        with open('cipherHistory.txt', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        with open('output.txt', 'w') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerows(data)
        print("Values written to output.txt")
    elif type == "end":
        loop = False
    else:
        print("Please enter either text, csv or end to continue")
