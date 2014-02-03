#Copywrite (C) Paul Ashby 2014
#Counts the number of times the number '9' appears from 1 to 'n'
#where n is integer input by the user.

count = 0

number = int(input("Enter an integer.\n:> "))

for i in range(1, number + 1):
    i = str(i)
    for j in i:
        if j == "9":
            count += 1
print("There are", count, "'9's from 1 to", number)
