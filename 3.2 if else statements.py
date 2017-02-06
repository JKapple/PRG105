values = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII','VIII','IX','X']
errorCode = 'Please, Choose a number that is in the range of 1-10:'
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
    print (values[7])
elif x == 9:
    print (values[8])
elif x == 10:
    print (values[9])
elif x > 10:
    print (errorCode)
elif x < 1:
    print (errorCode)
