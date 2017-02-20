def get_replacement_cost():
    x = input('Enter replacement cost of property: ')
    return x
replacement_cost = get_replacement_cost()

def calculate_insured_amount():
    y = replacement_cost * 0.80
    return y
insured_amount = calculate_insured_amount()

print("The amount of insurance you should purchase is:", insured_amount)
