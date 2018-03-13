alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num =[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
phone = input('Please enter your phone number in the format xxx-xxx-xxxx: ').lower()
accumulator = []
index = 0
for index in range(len(phone)):
    if phone[index].isalpha():
        accumulator.append(num[alph.index(phone[index])])
    else:
        accumulator.append(phone[index])
print .join(accumulator)
