from functools import reduce

numbers = [1, 2, 3, 4, 5]

#len, sum, min, max
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

#map: multiply every number by 2
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

#filter: select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#reduce: calculate the product
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

#sorted: sort numbers
print("Sorted descending:", sorted(numbers, reverse=True))
