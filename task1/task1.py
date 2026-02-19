__author__ = "Владимир Игонин"

term = "Даны два действительных числа a и b. Получить их сумму, разность и произведение."

def act(a: float, b: float, action: int) -> float:
    """
    Функция выполнения задания номер 1
    :param a: первое число
    :param b: второе число
    :param action: действие 1-сложение, 2-разность, остальное-умножение
    :return: результат действия с числами
    """
    if action == 1:
        return a + b
    elif action == 2:
        return a - b
    else:
        return a * b