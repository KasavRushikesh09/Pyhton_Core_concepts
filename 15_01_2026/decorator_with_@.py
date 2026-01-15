def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("after")
    return wrapper
@my_decorator
def result():
    print("hello world")
result()

