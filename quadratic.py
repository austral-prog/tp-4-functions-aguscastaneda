def roots(a, b, c):
    disc = b**2 - 4*a*c

    if disc < 0:
        return "( )"

    r1 = (-b + disc**0.5) / (2*a)
    r2 = (-b - disc**0.5) / (2*a)

    if r1 != r2:
        return f"({r1}, {r2})"
    
    return f"({r1})"


def value_y(a, b, c, x):
    y = a*x**2 + b*x + c
    return y


def to_string(a, b, c):
    if a != 0:
        if b != 0:
            return f"f(x) = {a} * X^2 + {b} * X + {c}"
        else:
            return f"f(x) = {a} * X^2 + {c}"
    elif b != 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return f"f(x) = {c}"    


def derivation(a, b, c):
    if a != 0:
        if b != 0:
            return f"f'(x) = {2*a} * X + {b}"
        else:
            return f"f'(x) = {2*a} * X"
    elif b != 0:
        return f"f'(x) = {b}"
    else:
        return "f'(x) = 0"
