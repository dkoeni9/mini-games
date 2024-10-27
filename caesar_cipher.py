alphabet_en = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_ru = " абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

direction = input("Направление (кодирование (1)/декодирование (2): ")

language = input("Язык (en/ru): ")

if language == "en":
    alphabet = alphabet_en
elif language == "ru":
    alphabet = alphabet_ru
else:
    alphabet = ""

if direction == "2":
    alphabet = alphabet[::-1]

shift = int(input("Сдвиг: "))

text = input("Текст: ")
result = ""

for char in text:
    if char.isalpha():
        shifted_index = alphabet.find(char) + shift
        result += alphabet[shifted_index]
    else:
        result += char

print(result)
