numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Sum of even numbers:", total)