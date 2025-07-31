for i in range(1,6):
    print('*'*i)

print('\n')

for i in range(5,91):
    print(i)
print('\n')

for i in range(2,103,4):
    print(i)
print('\n')

for i in range(29,3,-1):
    print(i)
print('\n')

for i in range(1,6):
    print(f'{i}.A')
print('\n')

for i in range(5):
    for j in range(5-i-1):
        print(' ', end = '')
    for j in range(2 * i + 1):
        if i == 2:
            print('*', end = '')
        elif j == 0 or j == 2*i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
print('\n')

total = 0
for i in range(1,1000,2):
    total += i**2
print('total = ',total)