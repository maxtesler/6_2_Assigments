from typing import Callable

def is_admin(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        if len(args)>0 and args[0] == 'admin':
            print('function pass as it should be')
            return func(*args, **kwargs)
        elif kwargs.get('user_type') == 'admin':
            print('function pass as it should be')
            return func(*args, **kwargs)
        else:
            raise ValueError (f'ValueError: Permission denied')
        
    return wrapper