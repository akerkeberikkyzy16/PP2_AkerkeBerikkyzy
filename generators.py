#iterator created from a list
numbers = [10, 20, 30, 40]

number_iterator = iter(numbers)

print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))


#iterator used in a loop
fruits = ["apple", "banana", "orange"]

fruit_iterator = iter(fruits)

for fruit in fruit_iterator:
    print(fruit)


#custom iterator class
class CountUp:
    def __init__(self, maximum):
        self.number = 1
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.maximum:
            current_number = self.number
            self.number += 1
            return current_number
        else:
            raise StopIteration


counter = CountUp(5)

for number in counter:
    print(number)


#generator function using yield
def generate_numbers(maximum):
    number = 1

    while number <= maximum:
        yield number
        number += 1


for number in generate_numbers(5):
    print(number)


#generator expression
squares = (number ** 2 for number in range(1, 6))

for square in squares:
    print(square)