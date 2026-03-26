__author__ = "Владимир Игонин"

import pytest
import task1.task1 as t1
import task2.task2 as t2
import task3.task3 as t3
import task4.task4 as t4
import task5.task5 as t5
import task6.task6 as t6
import task7.task7 as t7
import task8.task8 as t8
from task8.task8 import *

one = pytest.approx(1)
zer = pytest.approx(0)

def test1() -> None:
    """
    Тестирование 1 задачи
    :return:
    """
    assert t1.act(1, 1, 1) == pytest.approx(2)
    assert t1.act(1,1,2) == zer
    assert t1.act(1,1,3) == one

def test2() -> None:
    """
    Тестирование 2 задачи
    :return:
    """
    numbers0: list[float] = [0.1, 0.3, 0.5]
    numbers1: list[float] = [0.2, 0.5, 0.1]
    numbers2: list[float] = [0.3, 0.1, 0.4]
    numbers3: list[float] = [1, 2, 3]
    numbers4: list[float] = [3, 1, 6]
    numbers5: list[float] = [16, 16, 16]
    numbers6: list[float] = [15, 15, 19]
    numbers7: list[float] = [13, 16, 13]
    numbers8: list[float] = [12, 15, 15]
    numbers9: list[float] = [3, 6, 1]
    assert t2.act(numbers0) == zer
    assert numbers0 == pytest.approx([0.4, 0.3, 0.5])
    assert t2.act(numbers1) == zer
    assert numbers1 == pytest.approx([0.2, 0.5, 0.35])
    assert t2.act(numbers2) == zer
    assert numbers2 == pytest.approx([0.3, 0.35, 0.4])

    assert t2.act(numbers3) == zer
    assert numbers3 == pytest.approx([2.5, 2, 3])
    assert t2.act(numbers4) == zer
    assert numbers4 == pytest.approx([3, 4.5, 6])
    assert t2.act(numbers9) == zer
    assert numbers9 == pytest.approx([3.5, 6, 1])

    assert t2.act(numbers5) == one
    assert numbers5 == pytest.approx([16, 16, 16])
    assert t2.act(numbers6) == one
    assert numbers6 == pytest.approx([15, 15, 19])
    assert t2.act(numbers7) == one
    assert numbers7 == pytest.approx([13, 16, 13])
    assert t2.act(numbers8) == one
    assert numbers8 == pytest.approx([12, 15, 15])
    assert t2.act([1, 2]) == one
    assert t2.act([1, 2, 5, 6]) == one

def test3() -> None:
    """
    Тестирование 3 задачи
    :return:
    """
    numbers0: list[float] = [-6, -4, -2]
    numbers1: list[float] = [-6, -2, -4]
    numbers2: list[float] = [-3, -5, -8]
    numbers3: list[float] = [1, 2, 3]
    numbers4: list[float] = [5, 4, 2]
    numbers5: list[float] = [16, 16, 16]
    numbers6: list[float] = [-1, -1, -1]
    numbers7: list[float] = [-4, 5, -3]
    assert t3.act(5, 5, numbers0) == zer
    assert numbers0 == pytest.approx([6, -4.5, -2.5])
    assert t3.act(4, 8, numbers3) == zer
    assert numbers3 == pytest.approx([1, 1.5, 2.5])
    assert t3.act(1, 1, numbers1) == zer
    assert numbers1 == pytest.approx([-6.5, 2, -4.5])
    assert t3.act(4, 2, numbers4) == zer
    assert numbers4 == pytest.approx([4.5, 4, 1.5])
    assert t3.act(4, 1, numbers2) == zer
    assert numbers2 == pytest.approx([-3.5, -5.5, 8])
    assert t3.act(16, 2, numbers7) == zer
    assert numbers7 == pytest.approx([-4.5, 4.5, 3])
    assert t3.act(5, 5, numbers5) == zer
    assert numbers5 == pytest.approx([16, 15.5, 15.5])
    assert t3.act(4, 4, numbers6) == zer
    assert numbers6 == pytest.approx([1, -1.5, -1.5])
    assert t3.act(1, 1, [1, 2]) == one
    assert t3.act(1, 1, [5, 4, 3, 67]) == one

def test4() -> None:
    """
    Тестирование 4 задачи
    :return:
    """
    assert t4.fact(-5) == "Факториал не существует для отрицательных чисел"
    assert t4.fact(0) == one
    assert t4.act(0) == zer
    assert t4.fact(1) == one
    assert t4.act(1) == one
    assert t4.fact(2) == pytest.approx(2)
    assert t4.act(2) == pytest.approx(1.5)
    assert t4.fact(5) == pytest.approx(120)
    assert t4.act(5) == pytest.approx(1.716, abs=0.001)

def test5() -> None:
    """
    Тестирование 5 задачи
    :return:
    """
    assert t5.act([]) == zer
    assert t5.act([0.0]) == zer
    assert t5.act([10.0]) == pytest.approx(46.754, abs=0.001)
    assert t5.act([-10.0]) == pytest.approx(173.245, abs=0.001)
    assert t5.act([-5.0, 10.0, -60.0]) == pytest.approx(4688.631, abs=0.001)
    assert t5.act([-1.0, -2.0, -3.0, -4.0]) == pytest.approx(74.049, abs=0.001)
    assert t5.act([1, 2, 3, 4]) == pytest.approx(5.950, abs=0.001)


def test6() -> None:
    """
    Тестирование 6 задачи
    :return:
    """
    assert t6.act([]) == zer
    assert t6.act([2]) == zer
    assert t6.act([9]) == one
    assert t6.act([0]) == zer
    assert t6.act([1, 2, 3, 4, 5]) == pytest.approx(3)
    assert t6.act([2, 4, 6, 8, 10]) == zer
    assert t6.act([1, 3, 5, 7, 9]) == pytest.approx(5)


def test7() -> None:
    """
    Тестирование 7 задачи
    :return:
    """
    assert t7.act(1, 1) == zer
    assert t7.act(0, 0) == zer
    assert t7.act(1, 2) == one
    assert t7.act(5, 2) == pytest.approx(4101)
    assert t7.act(3, 10) == pytest.approx(5840)
    assert t7.act(10, 15) == pytest.approx(983455)
    assert t7.act(20, 20) == pytest.approx(69713280)

def test8() -> None:
    """
    Тестирование 8 задачи
    :return:
    """
    arr = [[1, 1, 1], [1, 1, 1]]
    matr = array(arr)
    p = [2, 2, 2]
    q = [3, 3, 3]
    matr = t8.act(matr, p, q, 0, 1)
    matrt= array([[1, 1, 3, 1], [2, 2, 3, 2], [1, 1, 3, 1]])
    for i in range(0, 3):
        for j in range(0, 4):
            assert matr[i, j] == pytest.approx(matrt[i, j])

    arr1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matr1 = array(arr1)
    p = [13, 14, 15, 16]
    q = [18, 19, 20, 21]
    matr1 = t8.act(matr1, p, q, 2, 3)
    matrt1 = array([[1, 2, 3, 4, 18], [5, 6, 7, 8, 19], [9, 10, 11, 12, 20], [13, 14, 15, 16, 21]])
    for i in range(0, 4):
       for j in range(0, 5):
            assert matr1[i, j] == pytest.approx(matrt1[i, j])

    matr2 = array(arr1)
    p = [13, 14, 15, 16]
    q = [18, 19, 20, 21]
    matr2 = t8.act(matr2, p, q, 0, 0)
    matrt2 = array([[1, 18, 2, 3, 4], [13, 19, 14, 15, 16], [5, 20, 6, 7, 8], [9, 21, 10, 11, 12]])
    for i in range(0, 4):
       for j in range(0, 5):
            assert matr2[i, j] == pytest.approx(matrt2[i, j])
