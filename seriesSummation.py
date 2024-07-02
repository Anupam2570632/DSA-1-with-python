print('-------------------------find sum of 1 to n------------------------')

num = int(input('Enter a number : '))
sum = 0

for i in range(1, num + 1):
    sum += i

print(f'Sum of 1 to {num} is : {sum}')