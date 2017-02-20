# In computer programs it is often useful to simulate randomness
# for example, in a game you may need to simulate the roll of a dice or shuffling of cards
#
# programs SIMULATE randomness by using complex mathematical formulas
# these provide a series of pseudo-random numbers
# in python we IMPORT a LIBRARY of functions to provide RANDOM NUMBER GENERATION
#
# the import statement tells python to access a library of code found outside of the program
# python provides several STANDARD LIBRARIES of functions like random and math
import random               # gives access to the random library

# print 3 random intergers in the range of 1-10(inclusive)
for num in range(3):
    this_guess = random.randint(1, 10)         # random.randint() gives access to randint() from random
    print(this_guess)
print('')

# to test the "accuracy" of the randomness, calculate an average
total = 0             # set an accumulator variable to 0
n_values = 3000         # how many random numbers to use
for num in range(n_values):
    total += random.randint(0, 100)            # average should be 50
# outside the loop I can calculate the average
average = total / n_values
print('The average using', n_values, 'values is',format(average, '.2f'))

# more random functions'
# randrange() parallels the range() functions
# it uses the same parameters: randrange (start, limit, step)
# return the random value from the range
print('')
for num in range(10):
    print(random.randrange(5, 101, 5))      # start=5, limit=101, step=5

# the random() returns a floating point value starting a 0.0 with a limit of 1.0
print('')
for num in range(10):
    print(random.random())

# uniform() function returns floating point numbers in a range you specify (end point included)
print('')
for num in range(10):
    print(random.uniform(5.0, 6.5))

# sometimes it is useful to be able to generate the SAME random number pattern
# to do this, we give a SEED value to the random number generator
random.seed(3)
print('')
for num in range(3):
    print(random.randint(1, 10))
random.seed(3)
print('')
for num in range(3):
    print(random.randint(1, 10))

