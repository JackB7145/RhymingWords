infile = open("dictionary.txt", "r")
dictionary = infile.read().split("\n")

#Asking the user for their characters at the end
end = input("Enter your ryming end: ").upper()
print("\nPossible ryming words: ")
length = len(end)
for x in dictionary:
    word = x[-length:]
    if word == end:
        print("\t", x)
        
        
