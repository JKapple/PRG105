values = [ 'A', 'B', 'C']

x = int(input('Current Package: 0=A, 1=B, 2=C:'))
if x == 0:
    min = int(input('minutes used:'))
    if min > 450:
        extra_min = min - 450
        extra_coin = extra_min * 0.45
        total = extra_coin + 39.99
    else:
        total = 39.99

if x == 1:
    min = int(input('minutes used:'))
    if min > 900:
        extra_min = min - 900
        extra_coin = extra_min * 0.40
        total = extra_coin + 59.99
    else:
        total = 59.99

if x == 2:
    total = 69.99

print (total)
