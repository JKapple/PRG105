

# simple void function
# a void function does not return a value
def display_currency(num):                   # num is my parameter
    print('$' + format(num, ',.2f'))         # format with commas and 2 decimal places

n = 7772.45
display_currency(n)                 # call the function with n as an argument

# rewrite this function so that it returns a value
def make_currency(num):
    return '$' + format(num, ',.2f')

dollars = make_currency (n)                   # call this function and store the value
print('***', dollars, '***')                  # use print() to display the results
print('***', make_currency (n), '***')        # I can use the function directly


# this function has multiple parameters and multiple return statements
# when you call it the arguments are matched to the parameters in order
def bigger(a, b, c):
    if a >= b and a >= c:
        return a          # a is bigger
    elif b >= a and b >= c:
        return b          # b is bigger
    else:
        return c          # c is the only other choice

print(bigger(50, 50, 50))
