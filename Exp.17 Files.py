fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       # list for the desired output
words=[];
for line in fh:                    # to read every line of file romeo.txt
    words += line.split()
words.sort()

# display the sorted words

print("The unique words in  alphabetical order are:")
for word in words:
    if word in lst:         # if element is repeated
            continue              # do nothing
    else:                     # else if element is not in the list
        lst.append(word)
        print(word)
#print(lst)
