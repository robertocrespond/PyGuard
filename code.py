from other_code import xyz
import random

entrypoint = lambda f: f

def sub() -> int:
    aaa = .5

    if random.random() < aaa:
        raise IOError
    
    return 10 + sub2()

def sub2() -> int:
    roberto = 100 
    if roberto > 101:
        raise AttributeError
    return roberto

@entrypoint
def abc():
    a = sub()

    try:
        b = sub()
    except (IOError):
        b = 2
    try:
        z = xyz()
    except (UnicodeError, ZeroDivisionError, ValueError):
        pass
    return a + b + z
