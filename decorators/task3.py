from typing import Callable

def check_types(func: Callable) -> Callable:
    def wrapper(*args):
        for a in args:
            if isinstance(a, int):
                return func(*args)
        try:
            raise TypeError('TypeError: Argument a must be int, not str')
        except TypeError as ke:
            print(ke)
        
    return wrapper