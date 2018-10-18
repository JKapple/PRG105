"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 9.1 Dictionaries
# Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14'}
birthdays ['katie'] = 'Mar16'
birthdays
birthdays
# 1.Print Meri's Birthday


# 2.Create an empty dictionary named registration
registration = []
print("registration is type", type(registration))

# 3.You will use the following dictionary for many of the remaining exercises

miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# print the keys and the values of miles_ridden using a for loop

print("\n")

# get the value for June 3 and print it, if not found display 'Entry not found', replace the ""

print("\nLooking for the values in miles_ridden")
value = ""
print(value)

# get the value for June 6 and print it, if not found display 'Entry not found' replace the ""

value2 = "June 6"
if value2 in miles_ridden:
    print(value2)
else:
    print("Entry not found")

# Use the items method to print the miles_ridden dictionary

print("\nUsing the items()method:")
for key, value3 in miles_ridden.items():
    print(key, ":", value3)

# Use the keys method to print all of the keys in miles_ridden

print("\nusing the keys() method:")
for keys in miles_ridden.keys

# Use the pop method to remove June 4 then print the contents of the dictionary

# Use the values method to print the contents of the miles_ridden dictionary

print("\nUsing the valur() method")
for values in miles_ridden.value():
    for key2 in miles_ridden:
        if miles_ridden[key2] == value4:
            print(value4,"has key", key2)

# TODO 9.2 Sets
# Create an empty set named my_set

print("\nWorking with sets")
mu_set - set()

# Create a set named days that contains the days of the week and print the set
days_of_week = ["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"]
# (You will need two sets of parentheses to avoid an error) set = (([ .... ] ))


# get the number of elements from the days set and print it
print("days_of_week has", len(days_of_week))
# Remove Saturday and Sunday from the days set, then print the set
days_of_week.discard("saturday")
days_of_week.remove("sunday")
print(days_of_week)
# Determine if 'Mon' is in the days set, print a messeage displaying the results

if 'Mon' in Days_of_week

# TODO 9.3 Serializing Objects (Pickling)

# import the pickle library at the top of the page
import pickle

print("\npickle library import at the top of the file")
# create the output file log and open it for binary writing
outfile = open("log.dat", 'wb')
# pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, outfile)

# close the log file
outfile.close
