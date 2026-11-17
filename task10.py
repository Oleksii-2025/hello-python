with open("notes.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        line = input(f"Введите строку {i + 1}: ")
        f.write(line + "\n")


with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("\nСодержимое файла:")
print(content)