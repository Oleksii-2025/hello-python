# Task 7: rectangle area function
def rectangle_area(width, height):
    return width * height


w = float(input("Введите ширину прямоугольника: "))
h = float(input("Введите высоту прямоугольника: "))

area = rectangle_area(w, h)

print("Площадь прямоугольника:", area)

