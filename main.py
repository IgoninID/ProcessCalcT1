__author__ = "Владимир Игонин"

import task1.task1 as t1
import task2.task2 as t2
import task3.task3 as t3
import task4.task4 as t4
import task5.task5 as t5
import task6.task6 as t6
import task7.task7 as t7
import task8.task8 as t8
from tests import test1, test2, test3, test4, test5, test6, test7, test8, test_frame

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test_frame()

def main():
    task = int(input("Введите номер задачи: "))

    if task == 1:
        print(t1.term)
        action = int(input("Сложение-1, Вычитание-2, Умножение-остальное: "))
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print("Результат действия: ", t1.act(a, b, action))

    elif task == 2:
        print(t2.term)
        numbers: list[float] = list(range(0, 3))
        numbers[0] = float(input("Введите первое число: "))
        numbers[1] = float(input("Введите второе число: "))
        numbers[2] = float(input("Введите третье число: "))
        if t2.act(numbers) == 1:
            print("Ошибка: Введите 3 различных числа")
        else:
            print("Результат задания: ", numbers)

    elif task == 3:
        print(t3.term)
        k = int(input("Введите первое целое число: "))
        m = int(input("Введите второе целое число: "))
        numbers: list[float] = list(range(0, 3))
        numbers[0] = float(input("Введите первое действительное число: "))
        numbers[1] = float(input("Введите второе действительное число: "))
        numbers[2] = float(input("Введите третье действительное число: "))
        if t3.act(k, m, numbers) == 1:
            print("Ошибка: Введите 3 числа")
        else:
            print("Результат задания: ", numbers)

    elif task == 4:
        print(t4.term)
        n = int(input("Введите целое число: "))
        if n < 0:
            print("Ошибка: Введите положительное число")
        else:
            print(f"Результат задания: {t4.act(n):.3f}")

    elif task == 5:
        print(t5.term)
        n = int(input("Введите количество элементов: "))
        numbers: list[float] = list(range(0, n))
        for i in range(0, n):
            numbers[i] = float(input(f"Введите {i} элемент: "))
        if n < 0:
            print("Ошибка: Введите положительное число")
        else:
            print(f"Результат задания: {t5.act(numbers):.3f}")

    elif task == 6:
        print(t6.term)
        n = int(input("Введите количество элементов: "))
        numbers: list[int] = list(range(0, n))
        for i in range(0, n):
            numbers[i] = int(input(f"Введите {i} элемент: "))
        if n < 0:
            print("Ошибка: Введите положительное число")
        else:
            print("Результат задания: ", t6.act(numbers))

    elif task == 7:
        print(t7.term)
        k = int(input("Введите счетчик внешнего цикла (k): "))
        l = int(input("Введите счетчик внетреннего цикла (l): "))
        if k < 0 or l < 0:
            print("Ошибка: Введите положительное число")
        else:
            print("Результат задания: ", t7.act(k, l))

    elif task == 8:
        print(t8.term)

if __name__ == "__main__":
    main()