import os
from typing import Optional, Any
from config import ROOT_DIR
from src.decorators import log


@log(os.path.join(ROOT_DIR, "logs", "log.txt"))
def func_1(a, b):
    return a+b


if __name__ == '__main__':
    func_1(1, 3)
    func_1(5, 2)
    func_1(1, "dog")