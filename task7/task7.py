__author__ = "Владимир Игонин"

term = "Вычилить сумма k от 1 до 10 (k^3) * сумма l от 1 до 15 ((k-l)^2)"

def act(i: int, j: int) -> int:
    """
    Функция вычисления по формуле сумма k от 1 до 10 (k^3) * сумма l от 1 до 15 ((k-l)^2)
    :param i: Счетчик внешнего цикла
    :param j: Счетчик внутреннего цикла
    :return: Результат вычисления по формуле
    """
    ans = 0
    temp = 0
    for k in range(1, i+1):
        for l in range(1, j+1):
            temp += (k-l)**2
        ans += temp * k**3
        temp = 0
    return ans