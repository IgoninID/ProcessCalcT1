__author__ = "Владимир Игонин"

term = "Вычислить: i = 1,n; сумма 1/i!"

def fact(n: int):
    """
    Вычисление факториала
    :param n: число
    :return: значение факториала для числа, если число отрицательное то строку с ошибкой
    """
    if n < 0:
        return "Факториал не существует для отрицательных чисел"
    elif n == 0:
        return 1
    else:
        ans = 1
        for i in range(1, n+1):
            ans *= i
        return ans

def act(n: int) -> float:
    """
    Вычисление по формуле в условии задачи
    :param n: число
    :return: результат формулы
    """
    ans: float = 0
    for i in range(1, n+1):
        ans += 1/fact(i)
    return ans
