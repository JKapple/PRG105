age = int(input('Please enter a persons age.'))
if age <= 1:
    print ('The person is an infant.')
elif age > 1 and age < 13:
    print ('The person is a child.')
elif age >= 13 and age < 20:
    print ('The person is a teenager.')
elif age >= 20:
    print ('The person is an adult.')
else:
    print ('Check that your input is an integer and try again.')
