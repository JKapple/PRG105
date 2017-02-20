# the SCOPE of a variable determines what part(s) can use it
# the SCOPE of a variable can be either GLOBAL or LOCAL
john = 'John'          # variables in the main program are GLOBAL to the program

# define a function that has a local variable as the same name as the GLOBAL variable
def test_local():
    # print(john)            # john is not yet defined INSIDE the function
    john = "Johnny"          # this variable is Local to the function; shadows (hides) the GLOBAL john
    print(john)

test_local()           # call the function
print(john)            # see if it gets the same result

mary = "Mary"          # another GLOBAL variable


# define a function that changes the GLOBAL variable
def test_global():
    global mary
    print(mary)          # the global keyword gives access to the global variable
    mary = "MaryLou"
    print(mary)

test_global()            # all the function to see the value
print(mary)


# define a finction with a unique local variable
def test_accessibility():
    sue = 'Sue'                # a LOCAL variable in the function
    print(sue)

test_accessibility()
# print(sue)                  # cannot acces the functions variable
print('')

# The variable used as an argument is LOCAL to the calling function
# the parameter that receives the value is LOCAL to the called function
def main():
    value = 99
    print('the value is',value)
    change_me(value)         # value is LOCAL to this function, I am passing it as an argument
    print('Back in the main function, the value is',value)


# the parameter to the function is a LOCAL variable to the function
# it gets its initial value from the calling programs argument
def change_me(param):
    print('I am changing the value of my copy of the parameter', param)
    param = 0                # change my parameter value
    print('Now the parameter is', param)

main()        # calling the main function

