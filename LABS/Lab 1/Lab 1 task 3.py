l = []
even = 0

for var in list(range(10)):
    var = int(input('Enter elements:'))
    l.append(var)

for var in list(range(10)):
    if l[var] % 2 == 0:
        even+= 1

print(even)