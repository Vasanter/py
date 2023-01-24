# var = input("Напиши че нить: ")
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

# a - запись новых данных в файл и помещение новых данных в конец файла
# w - запись новых данных, но с удалением старых данных

fw = open('doc/file_1.txt', 'w')
fw.write("Moustashe")
fw.close()

# чтение
fr = open('doc/file_1.txt', 'r')
text = fr.read()
fr.close()
print(text)