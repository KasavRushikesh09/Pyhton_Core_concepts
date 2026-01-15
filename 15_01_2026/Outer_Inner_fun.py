def outer_fun():
    print("outer fun()")

    def inner_fun():
        print("inner fun()")
    return inner_fun

in_ref  = outer_fun()
in_ref()