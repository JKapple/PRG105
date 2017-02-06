values = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
errorCode = 'Please, Choose a number that is in the range of 1-7'
x = int(input('provide a number from 1-7:'))

if x == 1:
    print (values [0])
elif x == 2:
    print (values [1])
elif x == 3:
    print (values [2])
elif x == 4:
    print (values[3])
elif x == 5:
    print (values[4])
elif x == 6:
    print (values[5])
elif x == 7:
    print (values[6])
elif x == 8:
    print (errorCode)
elif x == 9:
    print (errorCode)
elif x == 10:
    print (errorCode)
