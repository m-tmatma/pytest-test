import pytest

def dynamic_params1():
    for i in range(3):
        for j in ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]:
            yield i, j

@pytest.mark.parametrize("i, j, ", dynamic_params1())
def test_dynamic_params1(i, j):
    print(i, j)

def dynamic_params2():
    for i in range(3):
        for j in ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]:
            yield pytest.param(i, j, id=f"{i}-{j}-hogehoge")

@pytest.mark.parametrize("i, j, ", dynamic_params2())
def test_dynamic_params2(i, j):
    print(i, j)
