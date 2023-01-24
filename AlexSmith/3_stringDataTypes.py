# # Строчные типы данных
#
# var_1 = ('Hello ')
# str_2 = ("world ")
# result = (var_1 + str_2)
# print(result * 3)  # переменная повторится три раза
#
# str_1 = (' Hello')
# str_2 = (" world")
# result = (str_1 * 2 + str_2 * 3) #сложение строк => Конкатена́ция
# print(result)
#
# var_1 = 5
# var_2 = 10
# result = (var_2 + var_1)
# print('Результат : ' + str(result))

# str_1 = ('hello')
# str_2 = ("WORLD")
# print(str_1)
# print(dir(str_1))  # dir показывает список действий и функций которые мы можем применить к переменной
# # print(str_1.upper()) #upper выводит текст из нижнего регистра перешел в верхний
# print(str_1.title())  #title выводит первый символ в верхний регистр
# print(str_2.lower())  #lower перевод в нижний регистр
#
# name = 'Иван'
# a = 'Hello {}' #фигурные скобки означают что туда можно подставить какое либо значение
# result = a.format(name)
# print(result)


# first_name = 'Владимир'
# last_name = "Морозов"
# f = '{} {}'
# result = f.format(first_name, last_name)
# print('Меня зовут: ' + result)
# можно упростить:
# result = f'{first_name} {last_name}'
# print('Меня зовут: ' + result)