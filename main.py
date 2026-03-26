__author__ = "Владимир Игонин"

import sys
from typing import List
import task1.task1 as t1
import task2.task2 as t2
import task3.task3 as t3
import task4.task4 as t4
import task5.task5 as t5
import task6.task6 as t6
import task7.task7 as t7
import task8.task8 as t8
from tests import test1, test2, test3, test4, test5, test6, test7, test8


def print_help()->None:
    """
    Вывод справочной информации для задач
    :return:
    """
    print("                      Запуск лабораторных задач                      ")
    print()
    print("Использование:")
    print("  python main.py [-h | --help]                  → показать эту справку")
    print("  python main.py                                 → запуск без аргументов")
    print("  python main.py <номер>                         → запустить задачу без аргументов")
    print("  python main.py <номер> [аргументы...]          → запустить задачу с параметрами")
    print()
    print("Доступные задачи:")
    print()

    print("  1  – Даны два действительных числа a и b. Получить их сумму, разность и произведение.")
    print("       Аргументы: <action> <a> <b>")
    print("       Пример:   python main.py 1 1 5.5 3.2")
    print("                 (1 = сложение, 2 = вычитание, иначе = умножение)")
    print()

    print("  2  – Если сумма трех попарно различных действительных чисел x, y, z меньше единицы, то наименьшее из этих трех чисел заменить полусуммой двух других; в противном случае заменить меньшее из x и y полусуммой двух оставшихся значений.")
    print("       Аргументы: <num1> <num2> <num3>")
    print("       Пример:   python main.py 2 7.1 2.5 4.8")
    print()

    print("  3  – Даны целые числа k, m, действительные числа x, y, z. При k < m^2, k = m^2, k > m^2 заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5.")
    print("       Аргументы: <k> <m> <num1> <num2> <num3>")
    print("       Пример:   python main.py 3 2 5 1.1 2.2 3.3")
    print()

    print("  4  – Вычислить: i = 1,n; сумма 1/i!")
    print("       Аргументы: <n>")
    print("       Пример:   python main.py 4 10")
    print()

    print("  5  – Даны натуральное число n, действительные числа a1,..., an. Вычислить: (sqrt(abs(a1))-a1)^2 + ... + (sqrt(abs(an))-an)^2")
    print("       Аргументы: <n> <elem1> <elem2> ... <elemN>")
    print("       Пример:   python main.py 5 4 1.5 2.7 3.9 4.1")
    print()

    print("  6  – Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an: являющихся нечетными числами")
    print("       Аргументы: <n> <elem1> <elem2> ... <elemN>")
    print("       Пример:   python main.py 6 5 10 25 7 42 18")
    print()

    print("  7  – Вычилить сумма k от 1 до 10 (k^3) * сумма l от 1 до 15 ((k-l)^2)")
    print("       Аргументы: <k> <l>")
    print("       Пример:   python main.py 7 3 4")
    print()

    print("  8  – Вставка двух массивов в матрицу после строки p и столбца q")
    print("       Аргументы: <n> [матрица n×(n+1)] [numbers_str (n+1)] [numbers_sl (n+1)] <p> <q>")
    print("       Пример (n=2):")
    print("       python main.py 8 2  1 2 3 4  5 6 7 8  9 10 11 12  0 1  100 200  1 1")
    print("       (матрица 2×3 → 8 чисел, numbers_str → 3 числа, numbers_sl → 3 числа, p и q)")
    print()

    print("Дополнительно:")
    print("  • Если аргументы не переданы — задача запускается в интерактивном режиме")
    print()
    print("Автор: Владимир Игонин")


def run_task_8(args: List[str])->None:
    """
    Обработка задачи 8 с поддержкой аргументов командной строки
    :param args: Аргументы командной строки
    :return:
    """
    print("")
    print(t8.term)

    try:
        # Если аргументов мало — переходим в режим без аргументов
        if len(args) < 1:
            n = int(input("Введите количество строк матрицы (n): "))
        else:
            n = int(args[0])
            args = args[1:]                     # остаток аргументов

        if n <= 0:
            print("Ошибка: n должно быть положительным числом")
            return

        # Количество элементов в матрице: n строк × (n+1) столбцов
        matrix_size = n * (n + 1)

        # Если передали достаточно аргументов — берём из консоли
        if len(args) >= matrix_size + 2*(n+1) + 2:
            # Матрица
            matr_flat = [float(x) for x in args[:matrix_size]]
            matr = [matr_flat[i*(n+1):(i+1)*(n+1)] for i in range(n)]

            idx = matrix_size
            numbers_str = [float(x) for x in args[idx:idx + n + 1]]
            idx += n + 1
            numbers_sl = [float(x) for x in args[idx:idx + n + 1]]
            idx += n + 1
            p = int(args[idx])
            q = int(args[idx + 1])

            print(f"Загружено из аргументов: n={n}, p={p}, q={q}")

        else:
            # без аргументов
            print(f"\nВведите матрицу {n}×{n+1} построчно:")
            matr = []
            for i in range(n):
                while True:
                    row = input(f"Строка {i+1} ({n+1} чисел через пробел): ").strip().split()
                    if len(row) == n + 1:
                        matr.append([float(x) for x in row])
                        break
                    print(f"Ошибка! Нужно ввести ровно {n+1} чисел.")

            numbers_str = [float(input(f"numbers_str[{i}]: ")) for i in range(n + 1)]
            numbers_sl = [float(input(f"numbers_sl[{i}]: ")) for i in range(n + 1)]

            p = int(input(f"Введите p (0 ≤ p ≤ {n}): "))
            while not (0 <= p <= n):
                p = int(input(f"Неверно! 0 ≤ p ≤ {n}: "))

            q = int(input(f"Введите q (0 ≤ q ≤ {n}): "))
            while not (0 <= q <= n):
                q = int(input(f"Неверно! 0 ≤ q ≤ {n}: "))

        # Выполняем задачу
        result_matrix = t8.act(matr, numbers_str, numbers_sl, p, q)

        print("\nРезультат задания:")
        for row in result_matrix:
            clean_row = []
            for x in row:
                # Преобразуем np.float64 → float и округляем
                val = float(x)
                clean_row.append(round(val, 3) if abs(val) < 1e10 else val)  # чтобы не округлять очень большие числа
            print(clean_row)

    except ValueError as e:
        print(f"Ошибка преобразования типов: {e}")
        print("Проверьте, что все аргументы — числа.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


def run_task(task_num: int, args: List[str])->None:
    """
    Запуск конкретной задачи с возможной передачей аргументов
    :param task_num: Номер задачи
    :param args: Аргументы командной строки
    :return:
    """
    print(f"\n\Задача {task_num}")
    try:
        match task_num:
            case 1:
                print(t1.term)
                if len(args) >= 3:
                    action = int(args[0])
                    a = float(args[1])
                    b = float(args[2])
                else:
                    action = int(input("Сложение-1, Вычитание-2, Умножение-остальное: "))
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                print("Результат действия:", t1.act(a, b, action))

            case 2:
                print(t2.term)
                if len(args) >= 3:
                    numbers = [float(x) for x in args[:3]]
                else:
                    numbers = [float(input(f"Введите {i + 1}-е число: ")) for i in range(3)]
                result = t2.act(numbers)
                if result == 1:
                    print("Ошибка: Введите 3 различных числа")
                else:
                    print("Результат задания:", numbers)

            case 3:
                print(t3.term)
                if len(args) >= 5:
                    k = int(args[0])
                    m = int(args[1])
                    numbers = [float(x) for x in args[2:5]]
                else:
                    k = int(input("Введите первое целое число: "))
                    m = int(input("Введите второе целое число: "))
                    numbers = [float(input(f"Введите {i + 1}-е действительное число: ")) for i in range(3)]
                result = t3.act(k, m, numbers)
                if result == 1:
                    print("Ошибка: Введите 3 числа")
                else:
                    print("Результат задания:", numbers)

            case 4:
                print(t4.term)
                if args:
                    n = int(args[0])
                else:
                    n = int(input("Введите целое число: "))
                if n < 0:
                    print("Ошибка: Введите положительное число")
                else:
                    print(f"Результат задания: {t4.act(n):.3f}")

            case 5:
                print(t5.term)
                if args:
                    n = int(args[0])
                    if len(args) > 1:
                        numbers = [float(x) for x in args[1:1 + n]]
                    else:
                        numbers = [float(input(f"Введите {i} элемент: ")) for i in range(n)]
                else:
                    n = int(input("Введите количество элементов: "))
                    numbers = [float(input(f"Введите {i} элемент: ")) for i in range(n)]
                if n <= 0:
                    print("Ошибка: Введите положительное число")
                else:
                    print(f"Результат задания: {t5.act(numbers):.3f}")

            case 6:
                print(t6.term)
                if args:
                    n = int(args[0])
                    numbers = [int(x) for x in args[1:1 + n]] if len(args) > 1 else \
                        [int(input(f"Введите {i} элемент: ")) for i in range(n)]
                else:
                    n = int(input("Введите количество элементов: "))
                    numbers = [int(input(f"Введите {i} элемент: ")) for i in range(n)]
                if n <= 0:
                    print("Ошибка: Введите положительное число")
                else:
                    print("Результат задания:", t6.act(numbers))

            case 7:
                print(t7.term)
                if len(args) >= 2:
                    k = int(args[0])
                    l = int(args[1])
                else:
                    k = int(input("Введите счетчик внешнего цикла (k): "))
                    l = int(input("Введите счетчик внутреннего цикла (l): "))
                if k < 0 or l < 0:
                    print("Ошибка: Введите положительные числа")
                else:
                    print("Результат задания:", t7.act(k, l))

            case 8:
                run_task_8(args)

            case _:
                print(f"Ошибка: Задача {task_num} не найдена. Доступны задачи 1-8.")

    except ValueError as e:
        print(f"Ошибка ввода: {e}. Проверьте корректность переданных аргументов.")
    except Exception as e:
        print(f"Ошибка в задаче {task_num}: {e}")

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()

    args = sys.argv[1:]  # все аргументы после имени

    # Обработка аргументов через match case
    match args:
        case []:  # без аргументов
            print("Запуск в интерактивном режиме (без аргументов)")
            task = int(input("Введите номер задачи (1-8): "))
            run_task(task, [])

        case ["-h"] | ["--help"] | ["help"]:
            print_help()

        case [num] if num.isdigit() and 1 <= int(num) <= 8:
            # Только номер задачи — запускаем без аргументов
            run_task(int(num), [])

        case [num, *rest] if num.isdigit() and 1 <= int(num) <= 8:
            # Номер задачи + дополнительные аргументы
            run_task(int(num), rest)

        case _:
            print("Ошибка: Некорректные аргументы.")
            print_help()
            sys.exit(1)

if __name__ == "__main__":
    main()