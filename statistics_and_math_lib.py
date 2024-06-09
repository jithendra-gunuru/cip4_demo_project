import math
import statistics

def do_some_math():
    numbers = [1,2,3,4,5,6,7,8,9]

    print(statistics.mean(numbers))

    for num in numbers:
        print(math.factorial(num))

    print(math.pi)
    print(math.pi*2)

do_some_math()