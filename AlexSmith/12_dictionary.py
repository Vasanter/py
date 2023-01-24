#список
family_1 = ["Alex", "Olga", "Anton", "Nasty", "Alex"]
print(family_1)

#множества
family_2 = {"Alex", "Olga", "Anton", "Nasty", "Alex"} #система выведет уникальные значения
print(family_2)

#словарь (ключ:значение)
family_3 = {"Папа":"Alex", "Мама":"Olga", "Сын":"Semen", "Дочь":"Nasty"}
#print(family_3["Папа"])
for k, v in family_3.items():
    print(k)