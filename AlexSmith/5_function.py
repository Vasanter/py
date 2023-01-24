# Функции
# Пример 1:
# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)

# #  МОЖНО ЗАПИСАТЬ КАК:
# def summ (num_1, num_2):
#     result = num_1 + num_2
#     print(result)
#
# summ(10, 20)
# summ(30, 40)


# def summ (num_1, num_2):
#     result = num_1 + num_2
#     print(result)
#
# summ(num_2="Hello ", num_1="world ")

# def hi(name="Alex"):    # hi - название функции
#     print("Hello " + name)
# hi()
# # или
# name = "Владимир"
# def Hi(name):
#     print('Привет ' + name)
# Hi(name)
#
# # Модернизируем
# name = "Владимир"
# def Hi(name, age):
#     print('Меня зовут ' + name + " мне " + age + " года")
# Hi(name, age="33")
#
# # Модернизируем_1
# name = input("Как зовут? : ")
# age = input("Сколько тебе лет? : ")
# def Hi(name, age):
#     print('Вангую, тебя зовут ' + name + ", тебе " + age + " годика")
# Hi(name, age)

# # Модернизируем_2
# name = "Alex"
# age = "32"
# def hi(name, age):
#     result = name + " " + age
#     return result
#
# h = hi(name, age)
# print(h)
#
# # Правильный пример:
# var_1 = 5
# var_2 = 5
# #пустая строка
# #пустая строка
# def total():
#        result = var_1 + var_2
#        print (result)
# #пустая строка
# #пустая строка
#
# total()