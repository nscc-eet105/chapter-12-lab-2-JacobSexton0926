#Jacob Sexton 7/8/25

import os

while True:
    filename = input("Enter the name of the file you wish to process: ")

    if os.path.isfile(filename):
        break
    else:
        print("The file", filename, "could not be found!")
        choice = input("Enter the name of the file you wish to process or type exit to quit: ")
        if choice.lower() == 'exit':
            print("Thanks for using the program!")
            exit()

unique_words = set()

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            unique_words.add(word)

print("The number of unique words in the file is:", len(unique_words))
print("Thanks for using the program!")
