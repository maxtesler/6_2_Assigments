from typing import Callable

def catch_errors(func: Callable) -> Callable:
    def wrapper(*args):
        for a in args:
            if isinstance(a, dict) and 'key' in a:
                return func(*args)
        try:
            raise KeyError('Found 1 error during execution of your function: KeyError no such key as "key"')
        except KeyError as ke:
            print(ke)
        
    return wrapper