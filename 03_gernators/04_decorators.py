# decorators: functions that modify other functions

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        original_function(*args, **kwargs)
        print(f"Wrapper executed after {original_function.__name__}")
    return wrapper_function


@decorator_function
def display():
    print("Display function executed")


display()
print(display.__name__)  # Output: wrapper_function


from functools import wraps

def better_decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        original_function(*args, **kwargs)
        print(f"Wrapper executed after {original_function.__name__}")
    return wrapper_function 

@better_decorator_function
def show():
    print("Show function executed")


show()
print("this show the func name---> ",show.__name__)  # Output: show


# wraps preserves the metadata of the original function


# decorators with arguments
def repeat(num_times):
    def decorator_repeat(original_function):
        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            for _ in range(num_times):
                original_function(*args, **kwargs)
        return wrapper_function
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# chaining decorators
def uppercase_decorator(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return result.upper()
    return wrapper_function

def exclaim_decorator(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return result + "!909090"
    return wrapper_function


@exclaim_decorator
@uppercase_decorator
def say_hello(name):
    return f"Hello, {name}"


print(say_hello("Bob"))  # Output: HELLO, BOB!
# order of decorators matters