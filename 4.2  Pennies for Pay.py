daysWorked = int(input("Days worked:"))
totalPennies = 0
print("Days worked \tSalary\n-------|-------")
for currentDay in range(daysWorked):
    penniesForDay = 2 ** currentDay
    totalPennies += penniesForDay
    print(currentDay, "\t", penniesForDay)

totalPay = totalPennies * 0.01
print(totalPay)


