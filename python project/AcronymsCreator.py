#User Input
input_string = str(input("Enter your Phrase: "))

#Using the splitting function
txt = input_string.split()

#Using indexing via for loop
n = " "
for i in txt:
    n = n+str(i[0]).upper()
print(n)