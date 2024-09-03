def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

def say_hello():
    print("Hello!")

decorated_say_hello = apply_decorator(say_hello)
decorated_say_hello()
