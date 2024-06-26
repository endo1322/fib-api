from fibo import fibo
import pytest

def test_fibo_1():
    assert fibo(3) == 2

def test_fibo_2():
    assert fibo(4) == 3

def test_fibo_3():
    assert fibo(5) == 5

def test_fibo_4():
    assert fibo(6) == 8

def test_fibo_5():
    assert fibo(7) == 13

def test_fibo_6():
    assert fibo(8) == 21

def test_fibo_6():
    assert fibo(9) == 34

def test_fibo_6():
    assert fibo(10) == 55

def test_fibo_6():
    assert fibo(11) == 89

def test_fibo_corner_1():
    assert fibo(1) == 1

def test_fibo_corner_2():
    assert fibo(2) == 1

def test_fibo_corner_3():
    assert fibo(99) == 218922995834555169026

# 負数の入力
def test_fibo_error_1():
    with pytest.raises(ValueError):
        fibo(-1)

# 100以上の入力
def test_fibo_error_2():
    with pytest.raises(ValueError):
        fibo(100)

# 数値以外の入力
def test_fibo_error_3():
    with pytest.raises(ValueError):
        fibo('a')

# 数値以外の入力
def test_fibo_error_4():
    with pytest.raises(ValueError):
        fibo(0)