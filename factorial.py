print("------------------------Find factorial of a number----------------------------")
a = int(input('Enter a number : '))

fact = 1

for i in range(a+1):
    if(i != 0):
        fact *= i
    
print(f'factorial of the number {a} is {fact}')