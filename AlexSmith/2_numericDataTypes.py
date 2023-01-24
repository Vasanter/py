# Числовые типы данных

num_1 = 5
# print(num_1)
# num_1 = 10
# print(type(num_1)) функция type позволяет оптеделять тип данных
# print(num_1) система читает код сверху вниз
num_2 = 10
result = num_1 + num_2
num_1 = 10
print(result)

# возведение в степень
num_3 = 2 ** 5
print(num_3)

# округление в результате
num_4 = 50
num_5 = 8
result_1 = num_4 / num_5  # если поставть // в результате тоже получим целостное число. int писать не надо
print(int(result_1))  # ответ 6

# остаток от деления - %
num_6 = 50
num_7 = 8
result_2 = num_6 % num_7  # т.е. 6 * 8 = 48 --2 в остатке
print(result_2)

# True/False
num_8 = 5
num_9 = 6
result_3 = num_8 % num_9
print(num_8 == num_9)  # == означенает сравнение

# округление
num_10 = 10
num_11 = 3
result_4 = num_10 / num_11
print(result_4)

print(round(10 / 3, 4))  # 4ка означает до какой цифры округлять

# разделение с помощью float
num_12 = float(10.5)
num_13 = 10
result_5 = num_12 + num_13
print(result_5)
