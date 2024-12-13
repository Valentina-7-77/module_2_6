# Слишком древний шифр
digit = int(input('Введите число от 3 до 20: '))  # Вводим число в первое поле
result = ' '                                       # Создаем строковую переменную
for i in range(1, digit):                           # Ищем нужные пары
    for j in range(1, digit):
        if j <= i:                                  # Проверяем уникальность пар
            continue
        summa = i + j
        if digit % summa == 0:
            result = result + str(i) +str(j)
print('Пароль', result)                             # Выводим результат