from random import *


def is_valid(string):
    return string.isdigit() and 1 <= int(string) <= int(n)


def define_right_border():
    while True:

        global n
        n = input("Введите правую границу интервала: ")

        if is_valid(n):
            n = int(n)
            break
        else:
            print("Введите целое число, большее 0!")
            continue


def play():
    number = randint(1, n)
    counter = 0

    while True:
        user_number = input(f"Введите число от 1 до {n}: ")

        if is_valid(user_number):
            user_number = int(user_number)
            counter += 1

            if user_number < number:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                continue
            elif user_number > number:
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                print("Вы угадали, поздравляем!")
                print(f"Количество попыток: {counter}")
                break
        else:
            print(f"А может быть все-таки введем целое число от 1 до {n}?")
            continue


print("Добро пожаловать в числовую угадайку!")

while True:
    define_right_border()
    play()

    again = input("Сыграть ещё? (Y/N) ")
    if again.lower() == "y":
        continue
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся!")
        break
