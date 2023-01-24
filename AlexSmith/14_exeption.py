a = int(input('Введите первое число : '))
b = int(input('Введите второе число : '))

try:
    result = int (a / b)
except ZeroDivisionError:
    result = 0
    print('Делить на ноль нельзя')
print('Деление : ' + str (result))

result_2 = a + b
print('Сложение : ' + str (result_2))