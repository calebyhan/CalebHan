import sympy


def derivative(f, c):
    x = sympy.Symbol('x')
    return sympy.diff(f(x), x).evalf(c, subs={x: 2})


def linear_approx(f, c, a, step, values):
    if int(c) == a:
        print(values)
        return
    values.append(f(c) + derivative(f, a) * (c - a))
    linear_approx(f, c + step, a, step, values)


linear_approx(lambda x: x**2, 0, 1, 0.1, [])
linear_approx(lambda x: x**2, 0, 1, 0.25, [])
linear_approx(lambda x: x**2, 0, 1, 0.5, [])
