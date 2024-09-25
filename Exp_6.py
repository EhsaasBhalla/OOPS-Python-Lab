def mean(numbers):
    total = sum(numbers)
    return total / len(numbers)

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2]
        mid2 = numbers[(n // 2) - 1]
        return (mid1 + mid2) / 2

def mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    if len(modes) == len(numbers):
        return "No unique mode"
    return modes

total_numbers = int(input("Enter the total count of numbers: "))
numbers = []
print("Enter the numbers: ")
for i in range(total_numbers):
    num = int(input())
    numbers.append(num)


print("Mode:", mode(numbers))
print("Median:", median(numbers))
print("Mean:", mean(numbers))
