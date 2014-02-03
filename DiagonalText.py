#Copywrite (c) Paul Ashby 2014
#Prints out a user inputed string diagonally by checking the x/y position
#of the 'for' loop against a variable (input by user) and prints out the element of the string that coorosponds
#to that point (all other positions print out a ".". 

string = input("Enter a word or phrase.\n:> ")
count = 0 #Used to count out positions in the string.
length = len(string) #Stores the length of the string.
a = 0
loopcount = 0 #Counts the number of times the program loops.

#Stores an integer that will determine the height of the printed string.
COUNT = int(input("Enter an integer between 1 and\
                  \nthe length of your word/phrase.\n:> "))

#This will exit the program if the entered integer is
#not within the range of 1 to the length of the string.
if COUNT < 2 or COUNT > length:
    print("Number should be between 1 and the length of",
          "the string.")
    exit()

for y in range(COUNT):
    for x in range(length):
        if x == count:
            print(string[count], end= "")
            count += COUNT
        else:
            print(".", end= "")
    loopcount += 1 #Increments loopcount by one each time the program loops.
    count = loopcount #Sets count to the value of loopcount. 
    print()
            
