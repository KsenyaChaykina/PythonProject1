from typing import Any, Callable


def log(filename: str | None = None) -> Any:
    def decorator(func: Callable) -> Callable:
        """Очистка формируемого файла для перезаписи данных в файл"""
        # if os.path.exists(filename):
        # os.remove(filename)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Если файл существует, то записываем в файл"""
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    try:
                        result = func(*args, **kwargs)
                        """Отработка функции и результат, если функция отработала без ошибок"""
                        file.write(f"{func.__name__} called with args {args} and kwargs {kwargs}: result {result} \n")
                        return result
                    except Exception as er:
                        """Если функция отработала с ошибкой, выводит данные об ошибке"""
                        file.write(f"{func.__name__} Error: {er} \n")
                        raise er
            else:
                try:
                    result = func(*args, **kwargs)
                    """Отработка функции и результат, если функция отработала без ошибок"""
                    print(f"{func.__name__} called with args {args} and kwargs {kwargs}: result {result}")
                    return result
                except Exception as er:
                    """Если функция отработала с ошибкой, выводит данные об ошибке"""
                    print(f"{func.__name__} Error: {er}")
                    raise er

        return wrapper

    return decorator
