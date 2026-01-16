def india():
    count = 0
    def state():
        nonlocal count
        count += 1
        return count
    return state

c = india()
print(c())
print(c())
