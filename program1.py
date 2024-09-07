print("Hello TA's grading my Assaignment 1")

def my_decorator(func):
    def wrapper(*args):
        print("Before calling the function")
        result = func(*args)
        print("After the function")
        return result
    return wrapper

@my_decorator
def greet(name):
    print("Hello," + name + "!")

greet("Marcus")
