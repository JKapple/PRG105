# the range function returns a sequence of values
# when ONE argument is specified it represents am ending limit
#       NOT an ending value:
# 'ending limit' means up to but not including
# when a beginning value is not specified the default starts with zero
print ('Results of range (5):')
for num in range (5):
    print (num)

# when the arguments are specified, they represent a starting value and ending limit
print ('\nResults of range (6, 10:')
for num in range(6,10):
    print (num)

# when three arguments are given the last one is a step value
print('\nResults of range(2, 11, 2):')
for num in range (2, 11, 2):
    print(num)

print('\nResults of range(100, 0, -10:')
for num in range (100, 0, -10):
    print(num)

#arguments can be literals or variables
start = 75
end = 100
step = 5
#if I want the ending value to be the same as end. ineed to increase it for the limit
print ('\nResults using variables:')
for num in range(start, end+1, step):
    print(num)

# you must use a while loop if the number of interations is not clear
num = 2
end = 200
print('\nThe squares less than', end, "are:")
while num * num < end:
    print(num, 'square is',num * num)
    num += 1       # add one to the current value of num


