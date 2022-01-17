﻿# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Сумма чисел кратных 3 и 5
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, 
# то получим 3, 5, 6 и 9. Сумма этих чисел - 23.
# Найдите сумму всех чисел меньше 1000 кратных 3 или 5.
# Примечание: попробуйте записать решение при помощи генератора
# и встроенной фукнции sum
def multiples():
    return sum((i for i in xrange(1000) if (i % 3 == 0 or i % 5 == 0)))


# B. Сумма четных чисел ряда Фибоначчи
# Каждый следующий элемент ряда Фибоначчи получается при сложении 
# двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех элементов ряда Фибоначчи, каждый их которых
# является четным числом и не превышает четырех миллионов.
def fibonacci():
    a = 1
    b = 2
    result = 0
    while (a < 4000000 and b < 4000000):
        if (not(a & 1)):
            result += a
        if (not(b & 1)):
            result += b
        a += b
        b += a
    if (a < 4000000):
        result += a
    return result


# С. Самый большой палиндром
# Число-палиндром с обеих сторон (справа и слева) читается одинаково. 
# Самое большое число-палиндром, полученное произведением двух двухзначных чисел – 9009 = 91 * 99.
# Найдите самый большой палиндром, полученный произведением двух трёхзначных чисел.
def palindrome():
    return max(((i * j) for i in xrange(100, 1000) for j in xrange(100, 1000) if (str(i * j) == str(i * j)[::-1])))


# D. Генератор-преобразователь
# Напишите функцию transform, которая принимает на вход 2 функции, seq_gen и func,
# возвращает функцию-генератор, которая берет следующее значение из seq_gen и пропускает его через функцию func.
def transform(seq_gen, func):
    def generator():
        for i in seq_gen():
            yield func(i)
    return generator


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Сумма чисел кратных 3 и 5')
    test(multiples(), 233168)

    print()
    print('Сумма четных чисел ряда Фибоначчи')
    test(fibonacci(), 4613732)

    print()
    print('Самый большой палиндром')
    test(palindrome(), 906609)

    print()
    print('Генератор-преобразователь')
    test(list(transform(lambda: xrange(5), lambda x: x**2)()), [0, 1, 4, 9, 16])

if __name__ == '__main__':
    main()