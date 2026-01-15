def multiply_by(n):
    def multiply(x):
        return x*n
    return multiply

num = multiply_by(2)
num2 = multiply_by(3)

print(num(5))
print(num2(5))
