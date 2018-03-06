year=[]
january = float(input('Please enter rainfall for January: '))
february = float(input('Please enter rainfall for february: '))
march = float(input('Please enter rainfall for March: '))
april = float(input('Please enter rainfall for April: '))
may = float(input('Please enter rainfall for May: '))
june = float(input('Please enter rainfall for June: '))
july = float(input('Please enter rainfall for July: '))
august = float(input('Please enter rainfall for August: '))
september =float(input('Please enter rainfall for September: '))
october = float(input('Please enter rainfall for October: '))
november = float(input('Please enter rainfall for November: '))
december = float(input('Please enter rainfall for December: '))
year.extend((january, february, march, april, may, june, july, august, september, october, november, december))
def lowest():
    print('Lowest rainfall:', min(year))
lowest()
def highest():
    print('Most rainfall:', max(year))
highest()
def total():
    print('Total rainfall for the year:', sum(year))
total()
def average():
    print('Average monthly rainfall:', float(sum(year))/len(year))
average()
