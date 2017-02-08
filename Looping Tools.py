# sentinel values, accumulators and data validation tools you will use often

# **************************************************************************************************************
# a sentinel value is a special value used to trigger the end of a loop
# the sentinel values are often used when getting input form the keyboard

#  when getting data from the keyboard you need to clue the user in about the value
# you are looking for
# IMPORTANT: the sentinel value must be invalid value for the solution

in_value = int(input('\nEnter a number (0 to quit): '))     # sentinel value is zero
while in_value != 0:
    print(in_value, 'times 5 is', in_value * 5)
    in_value = in_value = int( input('\nEnter a number (0 to quit): '))      # don't forget the next value!

# **************************************************************************************************************
# an accumulator is a variable that is used to hold a running total
# before I use the accumulator I need to INITIALIZE it, set to the correct start value

total = 0                  # accumulator
count = 0                  # another accumulator to count the values
in_value = int(input('\nEnter test score(-1 to quit):'))                # -1 is my sentinel
while in_value != -1:
    total += in_value         # add the current value to my accumulator
    count += 1                # count the scores
    in_value = int(input('\nEnter test score(-1 to quit):'))

# now I have the total and the count
average = total / count              # now that I have the totals and I can figure the average
print ('\nFor', count, 'scores, the average is', average)

# ***************************************************************************************************************
# A data Validation loop tests for a valid input value and if invalid
# will repeatedly ask for a new value until a valid value is entered
choice = input ('\n\nChoose an option (A, B, C) :')   # prompt user for valid choice
choice = choice.upper()               # this will convert the input to uppercase
while choice != 'A' and choice != 'B' and choice != 'C':         # tests for BAD data
    choice = input('\nSorry, you need to enter A, B, or C: ')     # give error and ask again
    choice = choice.upper()           # prepare the data exactly the same way as before

# example with positive integer:
choice = input (' \n\nPlease enter a positive interger: ')
while not choice.isdigit():             # tests choice for all digits,does not handle + or -
    choice = input('\nSorry, I need a positive integer, PLease re-enter: ')
choice = int(choice)
print(choice * choice)

# ***************************************************************************************************************
# Create a data validation loop that requires the user to enter a single word (alphabetic characters only).
# str.isalpha() -- returns True if all characters are alphabetic
# str.strip() -- returns the same string with leading and trailing whitespace removed

value = int(input('\nEnter a single word: (alphabetic characters only):'))
while value =





