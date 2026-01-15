def my_decorator(func):
    def wrapper():
        print("Before decorator function")
        func()
        print("After decorator function")
    return wrapper

def result():
    print("Hello result")

result = my_decorator(result)
result()