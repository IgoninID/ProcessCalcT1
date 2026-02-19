__author__ = "Владимир Игонин"

term = "Даны целые числа k, m, действительные числа x, y, z. При k < m^2, k = m^2, k > m^2 заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5."

def act(k: int, m: int, numbers: list[float]) -> int:
    """
    При k < m^2, k = m^2, k > m^2 заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5.
    :param k: первое целое число
    :param m: второе целое число
    :param numbers: список с 3 действительными числами
    :return: 1 - чисел в списке не 3, 0 - функция сработала без ошибок
    """
    if len(numbers) != 3:
        return 1
    else:
        if k < m ** 2:
            numbers[0] = abs(numbers[0])
            numbers[1] -= 0.5
            numbers[2] -= 0.5
        elif k > m ** 2:
            numbers[2] = abs(numbers[2])
            numbers[0] -= 0.5
            numbers[1] -= 0.5
        else:
            numbers[1] = abs(numbers[1])
            numbers[0] -= 0.5
            numbers[2] -= 0.5
        return 0