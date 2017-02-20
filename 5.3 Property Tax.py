def property_value():
    x = input('What is the value of your property:')
    return x

property_value = property_value()

def property_tax():
    assessment_value = property_value * 0.6
    property_tax = assessment_value * 0.72
    print('the assessment value of your property is ', assessment_value, 'and the property will tax is ', property_tax)


