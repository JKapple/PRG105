# create a lists for dog breeds
dogs = ['Collie', 'Sheepdog', 'Corgi', 'Retriever', 'Bulldog']

# print the list
print(dogs)
print('\n')

# print each item in the list on its own line
for dog in dogs:
    print(dog)
print('\n')

# add a breed to the list
print('adding a new breed to the list')
dogs.append('german shepherd')
for index in range(len(dogs)):              # use range with # of dogs in list
    print(index+1, dogs[index])             # indexes start at 0, but I want to start with 1
print('\n')

# sort the dogs a-z
print('sorting the dogs')
dogs.sort()
# this time lets use a while loop
index = 0                           #
while index < len(dogs):
    print(index+1, dogs[index])
    index += 1
print('\n')

# reverse the order
print('reversing the list')
dogs.reverse()
for index in range(len(dogs)):              # use range with # of dogs in list
    print(index+1, dogs[index])
print('\n')

# how many dogs
print('There are', len(dogs), 'dogs in the list.')

# print the 3rd item in the list
print('The third dog in the list is', dogs[2])

# slices of the list
print('the first 3 dogs are', dogs[:3])      # Default starting value is 0
print('The last three dogs are', dogs[-3:])     # start 3 from the end and end at the end
middle = len(dogs) // 2                         # find the middle of the list
print(dogs[middle], 'is in the middle of the list')
print(dogs[middle-1:middle+2], 'are in the middle')     # +2 gets the one after the middle
print('\n')

# inserting at index
print('inserting at index 3')
dogs[3] = 'Weimaraner'
dogs.insert(3, 'Boxer')
print(dogs)
print('\n')

# look for a dog and return its index
print('Corgi is at index', dogs.index('Corgi'))

# check for inclusion
if 'Boxer' in dogs:
    print('Yes Boxer was found')
print('\n')

# use repetition to initialize a list
values = [0] * 6
print(values)

list_a = ['a','b', 'c']
list_b = [1, 2, 3]
list_c = list_a + list_b
print(list_c)


# using lists inside lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[0])
print(matrix[0][0])
print('\n')

# use nest to work with nested lists
for outer in matrix:
    for inner in outer:
        print(inner)

# make a new list from inputs
user_values = []       # initialize empty list
invalue = ''       # initialize to an emoty string
while invalue != 'done':      # look for 'done' as sentinel value
    invalue = input('enter a value:')
    if invalue != 'done':
        user_values.append(invalue)

print(user_values)
