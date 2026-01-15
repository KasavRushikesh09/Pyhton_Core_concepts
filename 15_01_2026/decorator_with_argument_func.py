def decorator(func):
    def wrapper(*args,**kwargs):
        print("Arguments",args)
        return func(*args,**kwargs)
    return wrapper
@decorator
def dec(a,b):
    return a+b
print(dec(2,3))
