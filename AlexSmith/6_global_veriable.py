# Глобальные и локальные переменные

var_1 = 10 # Глобальная переменная
var_2 = 20 # Глобальная переменная
# print(var_1, var_2)
def summ():
    var_1 = 30 # Локальная переменная
    var_2 = 40 # Локальная переменная
    result = var_1 + var_2
    print(result)
print(var_1, var_2)
summ()



var_1 = 100 # Глобальная переменная
var_2 = 20 # Глобальная переменная
# print(var_1, var_2)
def summ():
    result = var_1 + var_2
    print(result)

def sub():
    result = var_1 - var_2
    print(result)

summ()
sub()