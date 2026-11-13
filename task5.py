numbers = [4, 8, 15, 16, 23, 42]

total = 0
biggest = numbers[0]

for n in numbers:
    total = total + n
    if n > biggest:
        biggest = n

average = total / len(numbers)

print("Сумма:", total)
print("Наибольшее:", biggest)
print("Среднее:", average)
print(sum(numbers), max(numbers))