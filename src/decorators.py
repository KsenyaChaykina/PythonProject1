import os
from typing import Optional, Any
from config import ROOT_DIR

def log(filename: Optional[str]) -> Any:
    def decorator(func):
        if os.path.exists(filename):
            os.remove(filename)
        def wrapper(*args, **kwargs):
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    try:
                        result = func(*args, **kwargs)
                        file.write(f"{func.__name__} called with args {args} and kwargs {kwargs}: result {result} \n")
                        return result
                    except Exception as er:
                        file.write(f"{func.__name__} Error: {er} \n")
                        raise er
            else:
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} called with args {args} and kwargs {kwargs}: result {result}")
                    return result
                except Exception as er:
                    print(f"{func.__name__} Error: {er}")
                    raise er
        return wrapper
    return decorator
