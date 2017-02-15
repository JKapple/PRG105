# Color mixer takes two primary colors and decides which secondary color is created
# results are displayed

# define get_color() function to get data and validate


def get_color():
    color = input('Enter red, yellow or blue:')               # give them color choices
    color = color.upper()                                     # convert to uppercase

# validate input - verify RED, YELLOW or BLUE
# when we validate we look for BAD values and make them reenter

    while color != 'RED' and color != 'BLUE' and color != 'YELLOW':
        color = input('Bad Data. Please enter red, yellow or blue:')
        color = color.upper()                     #prepare data as before
# I know I have good data since I can not get out of the loop without good data
    return color                            # give this good data back to the calling program
# define the mix_colors() function to find the result


def mix_colors(first, second):
    # test the first color and then test the other two
    if first == 'BLUE':
        if second == 'RED':
            return 'PURPLE'
        else:
            return 'GREEN'       # assume second color is yellow
    elif first == 'RED':
        if second =='BLUE':
            return 'Purple'
        else:
            return 'ORANGE'      # assume second color is yellow
    else:
        if second == 'BLUE':
            return'GREEN'
        else:
            return 'ORANGE'      # assume second color is red


# one way to solve for verifying different colors is use of ELIF statements validating two entries of the same color
# will get the same color
# what are the major tasks in this program?
# Major tasks:
# 1. get colors from the user - and validate the data --> function
# 2. decide what secondary color is made --> function
# 3. display the result --> print statement
# -----Main Program-----
print('this program accepts two primary colors and tells you',
      'the result when they are combined.')

# call the get color function
first_color = get_color()        # get the first color
second_color = get_color()       # get the second color

# I have validated each color individually, but I need to test to
# make sure I have two different colors - - another data validation issue
while first_color == second_color:        # this is BAD data
    print('I need two different primary colors. I already have:', first_color)
    second_color = get_color()            # get the second color

# find result
result_color = mix_colors(first_color,second_color)        # mix the colors

#display result
print(first_color, 'and', second_color, 'makes', result_color)
