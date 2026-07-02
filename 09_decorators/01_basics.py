def my_decorator(func):
    def wrapper():
        print("before func runs")
        func()
        print("After func runs")
    return wrapper

@my_decorator
def greet():
    print("hello from decorators class")

greet()