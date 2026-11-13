first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

print("Сумма:", first_number + second_number)
print("Разность:", first_number - second_number)
print("Произведение:", first_number * second_number)

if second_number == 0:
    print("Частное: на ноль делить нельзя")
else:
    print("Частное:", first_number / second_number)