userInput = int(input('Enter a number between 1 and 100:'))
if userInput >= 100:
    userInput = int(input('Enter a number between 1 and 100:'))
obj = {}
for i in range(1, 100):
    obj[str(i)] = []
print(obj)


