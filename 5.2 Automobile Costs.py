def get_monthly_costs():
    input('Enter the monthly costs for the following: Press enter when ready:')
    a = input('Loan payment:')
    b = input('Insurance:')
    c = input('Gas:')
    d = input('oil:')
    e = input('tires:')
    f = input('Maintenance:')
    x = (a + b + c + d + e + f)
    return x
total_monthly_cost = get_monthly_costs()

def get_yearly_cost():
    z = total_monthly_cost * 12
    return z
total_yearly_cost = get_yearly_cost()

print(total_monthly_cost, total_yearly_cost)


