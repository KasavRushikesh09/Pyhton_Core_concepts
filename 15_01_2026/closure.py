def outer():
    message = "hello"
    def inner():
        print(message)
    return inner
func = outer()
print(func())