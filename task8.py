def count_words(text):
    words = text.split()
    return len(words)


sentence = input("Введите предложение: ")

result = count_words(sentence)

print("Количество слов:", result)