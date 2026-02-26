__author__ = "Владимир Игонин"

from math import sqrt

term = "Даны натуральное число n, действительные числа a1,..., an. Вычислить: (sqrt(abs(a1))-a1)^2 + ... + (sqrt(abs(an))-an)^2"

def act(a: list[float])-> float:
    """
    Функция вычисления по формуле (sqrt(abs(a1))-a1)^2 + ... + (sqrt(abs(an))-an)^2
    :param a: Массив из действительных чисел
    :return: Результат вычисления по формуле
    """
    ans = 0.0
    for elem in a:
        ans += (sqrt(abs(elem))-elem)**2
    return ans