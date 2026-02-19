__author__ = "Владимир Игонин"

import task1.task1 as t1
import task2.task2 as t2
import task3.task3 as t3
import task4.task4 as t4
import task5.task5 as t5
import task6.task6 as t6
import task7.task7 as t7
import task8.task8 as t8

def test1() -> None:
    assert t1.act(1, 1, 1) == 2
    assert t1.act(1,1,2) == 0
    assert t1.act(1,1,3) == 1

def test2() -> None:
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
    assert t2.act(numbers0) == 0
    assert numbers0 == [0.4, 0.3, 0.5]
    assert t2.act(numbers1) == 0
    assert numbers1 == [0.2, 0.5, 0.35]
    assert t2.act(numbers2) == 0
    assert numbers2 == [0.3, 0.35, 0.4]

    assert t2.act(numbers3) == 0
    assert numbers3 == [2.5, 2, 3]
    assert t2.act(numbers4) == 0
    assert numbers4 == [3, 4.5, 6]
    assert t2.act(numbers9) == 0
    assert numbers9 == [3.5, 6, 1]

    assert t2.act(numbers5) == 1
    assert numbers5 == [16, 16, 16]
    assert t2.act(numbers6) == 1
    assert numbers6 == [15, 15, 19]
    assert t2.act(numbers7) == 1
    assert numbers7 == [13, 16, 13]
    assert t2.act(numbers8) == 1
    assert numbers8 == [12, 15, 15]
    assert t2.act([1, 2]) == 1
    assert t2.act([1, 2, 5, 6]) == 1

def test3() -> None:
    numbers0: list[float] = [-6, -4, -2]
    numbers1: list[float] = [-6, -2, -4]
    numbers2: list[float] = [-3, -5, -8]
    numbers3: list[float] = [1, 2, 3]
    numbers4: list[float] = [5, 4, 2]
    numbers5: list[float] = [16, 16, 16]
    numbers6: list[float] = [-1, -1, -1]
    numbers7: list[float] = [-4, 5, -3]
    assert t3.act(5, 5, numbers0) == 0
    assert numbers0 == [6, -4.5, -2.5]
    assert t3.act(4, 8, numbers3) == 0
    assert numbers3 == [1, 1.5, 2.5]
    assert t3.act(1, 1, numbers1) == 0
    assert numbers1 == [-6.5, 2, -4.5]
    assert t3.act(4, 2, numbers4) == 0
    assert numbers4 == [4.5, 4, 1.5]
    assert t3.act(4, 1, numbers2) == 0
    assert numbers2 == [-3.5, -5.5, 8]
    assert t3.act(16, 2, numbers7) == 0
    assert numbers7 == [-4.5, 4.5, 3]
    assert t3.act(5, 5, numbers5) == 0
    assert numbers5 == [16, 15.5, 15.5]
    assert t3.act(4, 4, numbers6) == 0
    assert numbers6 == [1, -1.5, -1.5]
    assert t3.act(1, 1, [1, 2]) == 1
    assert t3.act(1, 1, [5, 4, 3, 67]) == 1

def test4() -> None:
    assert t4.fact(-5) == "Факториал не существует для отрицательных чисел"
    assert t4.fact(0) == 1
    assert t4.act(0) == 0
    assert t4.fact(1) == 1
    assert t4.act(1) == 1
    assert t4.fact(2) == 2
    assert t4.act(2) == 1.5
    assert t4.fact(5) == 120
    assert abs(t4.act(5) - 1.716) < 0.001

def test_frame() -> None:
    assert 1 == 1