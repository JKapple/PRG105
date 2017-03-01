# write a program that will read and write to a data file
# your main function should display a menu and allow the user to choose one of the following:
# 1. read and display the data file (or a message indicating there are no names)
# 2. allow the user to enter a first and last name to be appended to the data file
# 3. remove one or more people from the list
# 4. exit the program
import os               # import operating system function

# main function displays tht menu and processes the user choice
def main():
    # display a welcome message
    print('Friend list manager')
    # display a menu, get choice and validate it
    choice = '0'          # start with an invalid choice

    # the outer loop processes the menu
    while choice != '4':
        # data validation loop -- check for invalid menu choice
        while choice != '1' and choice != '2' and choice != 3 and choice != '4':
            print('\nPlease choose an option:')
            print('   1. Display friends list')
            print('   2. Add a friend')
            print('   3. Remove someone')
            print('   4. Exit')
            choice = input('? ').strip()                      # .strip() will strip any whitespace

        # now we have a valid choice do what is requested
        if choice == '1':
            display_friend_list()            # call a function to do this
            choice = '0'                     # reset to an invalid value
        elif choice == '2':
            add_friend()
            choice = '0'
        elif choice == '3':
            remove_person()
            choice = '0'

        # display an exit message
    print('\nYour friends list is stored in friends.txt')


# this function reaDS AND DISPLAYS THE LIST
def display_friend_list():
    try:
        # open read display close
        infile = open('friends.txt', 'r')
        # file is open, read it
        for name in infile:
            print(name.strip())           # remove the newline and all whitespace
        infile.close()
    except FileNotFoundError:
        print('Your friend does not exist yet. Please add some friends!')
    except IOError:
        print('Unable to access the file.')


# add friend function
def add_friend():
    try:
        outfile = open('friends.txt', 'a')     #open in append mode
        fn = input('Enter your friends first name:').capitalize()
        In = input('Enter your friends last name:').capitalize()
        # display and confirm
        print(fn, In)
        confirm = input('Does that look right? (y/n)').strip().lower()       # strip and lowercase
        if confirm == 'y':
            outfile.write(In + ',' + fn + '\n')
            print(fn, In, 'added to your friends list.')
        else:
            print('No changes made.')
        outfile.close()
    except IOError:
        print('Unable to access friend file.')

# remove someone
def remove_person():
    name = input('Which person do you want to remove').strip().lower()      # strip and lowercase
    if name != '':           # make sure I have something to look for
        # open the file and look for a match
        try:
            infile = open('friends.txt', 'r')            # friend file in read mode
            out_file = open('friends.tmp', 'w')          # temp file in write mode
            for line in infile:                # look at each line in the input file
                # check for a match
                # if it matches, skip, otherwise, copy to output
                if name in line.strip().lower():             # use same conversion, strip and lower
                    print(line.strip())                   # remove newline
                    confirm = input ('Remove this person? (y/n) ').strip().lower()
                    # if confirmed, skip this else, write to temp file
                    if confirm == 'y':
                         print(line.strip(), 'removed.')
                    else:
                        out_file.write(line)             # not confirmed
            else:
                out_file.write(line)                 # not a match
            infile.close()
            out_file.close()
            os.remove('friends.txt')
            os.rename('friends.tmp', 'friends.txt')
        except IOError:
            print('Error. Unable to modify the friends file.')
    else:
        print('No changes made')





main()
