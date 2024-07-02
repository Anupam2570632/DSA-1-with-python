fruits = ['banana', 'apple', 'orange']

fruits.append('lemon')


fruits.insert(1, 'mango')
print(fruits.index('lemon'))
fruits.reverse()
fruits.sort()

print(fruits)
fruits.remove('mango')

numbers = [1, 2, 3, 4, 3, 4, 5, 1]
numbers.sort()
numbers.extend(fruits)


print(numbers)