total = 0
n = int(input('Enter number: '))

for x in range(1, n + 1):
    cube = x**3
    print(f'{x}: {x}**3 = {cube}')
    total = total + cube

print('Total:', total)