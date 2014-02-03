#Copywrite (c) Paul Ashby 2014
#Takes a input string and outputs the position and 
#number of capital X's in the longest sub string.
#

long = 0
count = 0
longposition = 0
position = 0

string = input("Enter a string of letters.\n:>")
length = len(string)
if int(string.count("X")) == 0:
    print("There are no capital X's in your string.")
    exit()

for i in range(length):
    if string[i] != "X" or i == (length - 1):
        if count > long:
            long = count
            longposition = position
        count = 0
    if string[i] == "X":
        count += 1
    if count == 1:
        position = i
    if string[i] != "X" or i == (length - 1): #Necesary in case the longest X string is 1 and is at the end of the string.
        if count > long:
            long = count
            longposition = position
        count = 0

finalposition = longposition +1

print("The longest string of X's in your string started at \nposition", finalposition, "and the",
      "length of the string was", long, ".")

        
        
        
        
    
