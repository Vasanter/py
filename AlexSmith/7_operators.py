# #Пример_1
# age = 26
# name = "Alex"
# if age == 25 and name == "Alex":
#     print("Мне 25 лет и зовут меня Алекс")
# elif age > 25:
#     print("Кому-то больше 25 лет")
# else:
#     print("Кому-то меньше 25 лет")

# # #Пример_2
# name = "Alex"
# if "T" in name == "Alex":
#     print("Меня зовут Алекс")
# else:
#     print("Это не Алекс")


# #Пример_3
pin = 1234
print("Введите пин-код: ")
user_pin = int(input())

if pin == user_pin:
    print("Добро пожаловать!")
else:
    print("Ошибка! Введите корректный пин-код. У Вас осталось две попытки!")
    user_pin = int(input())
    if pin == user_pin:
        print("Добро пожаловать!")
    else:
        print("Ошибка! Введите корректный пин-код. У Вас осталось одна попытка!")
        user_pin = int(input())
        if pin == user_pin:
            print("Добро пожаловать!")
        else:
            print("Ваша карта заблокирована!")