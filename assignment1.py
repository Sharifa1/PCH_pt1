# Word Reverse Game
myInput = input("Enter a string: ")
count = len(myInput)
result = ""
while count > 0:
    result = result + myInput[count-1]
    count = count - 1
print(result)
