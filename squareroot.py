def newton_method(number, number_iters = 50):
    a = float(number)
    for i in range(number_iters):
        number = 0.5 * (number + a / number)
    return number

print(newton_method(10))
