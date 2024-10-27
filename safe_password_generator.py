from random import *


def generate_password(length, chars):
    password = "".join(sample(chars, length))
    return password


digits = "0123456789"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""

number = int(input("Количество генераций: "))
length = int(input("Длина пароля: "))

add_digits = input("Включать ли цифры? (Y/N) ")
add_alpha_lower = input("Включать ли прописные буквы? (Y/N) ")
add_alpha_upper = input("Включать ли строчные буквы? (Y/N) ")
add_punctuation = input("Включать ли символы '!#$%&*+-=?@^_'? (Y/N) ")
remove_badsymbols = input("Исключать ли неоднозначные символы? (Y/N) ")

if add_digits.lower() == "y":
    chars += digits

if add_alpha_lower.lower() == "y":
    chars += alpha_lower

if add_alpha_upper.lower() == "y":
    chars += alpha_upper

if add_punctuation.lower() == "y":
    chars += punctuation

if remove_badsymbols.lower() == "y":
    for char in "il1Lo0O":
        chars = chars.replace(char, "")


for _ in range(number):
    print(generate_password(length, chars))
