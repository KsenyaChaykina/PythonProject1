import os
from fileinput import filename

import pytest
from typing import Optional, Any
from config import ROOT_DIR
from src.decorators import log

@log()
def func_1(a, b):
    return a+b

@log(os.path.join(ROOT_DIR, "logs", "log_test.txt"))
def func_2(a, b):
    return a+b


def test_func_1(capsys):
    result = func_1(1, 4)
    assert result == 5
    captured = capsys.readouterr()
    assert "func_1 called with args (1, 4) and kwargs {}: result 5" in captured.out

def test_func_1_error(capsys):
    with pytest.raises(Exception):
        result = func_1(1, "dog")
    captured = capsys.readouterr()
    assert f"func_1 Error" in captured.out

def test_func_2():
    filename = os.path.join(ROOT_DIR, "logs", "log_test.txt")
    if os.path.exists(filename):
        os.remove(filename)
    result = func_2(1, 4)
    assert result == 5
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()
    assert content[0] == "func_2 called with args (1, 4) and kwargs {}: result 5 \n"

def test_func_2_error():
    filename = os.path.join(ROOT_DIR, "logs", "log_test.txt")
    if os.path.exists(filename):
        os.remove(filename)
    with pytest.raises(Exception):
        result = func_2(1, "dog")
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()
    assert content[0] == "func_2 Error: unsupported operand type(s) for +: 'int' and 'str' \n"

