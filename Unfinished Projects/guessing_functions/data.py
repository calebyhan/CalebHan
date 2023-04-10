import random
import numpy as np

TRAIN = 900
TEST = 100

def constant():
    with open("data\\train\\constant.txt", "w") as f:
        for i in range(TRAIN):
            m = random.uniform(-10, 10)
            f.write(f"y = {m}\n")
    with open("data\\test\\constant.txt", "w") as f:
        for i in range(TEST):
            m = random.uniform(-10, 10)
            f.write(f"y = {m}\n")

def linear():
    with open("data\\train\\linear.txt", "w") as f:
        for i in range(TRAIN // 3):
            m = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            f.write(f"y = {m}x + {b}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 3):
            m = random.uniform(-10, 10)
            y1 = random.uniform(-100, 100)
            x1 = random.uniform(-100, 100)
            f.write(f"y - {y1} = {m}(x - {x1})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 3):
            a = random.uniform(-100, 100)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            f.write(f"{a}x + {b}y = {c}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
    with open("data\\test\\linear.txt", "w") as f:
        for i in range(TEST // 3):
            m = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            f.write(f"y = {m}x + {b}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 3):
            m = random.uniform(-10, 10)
            y1 = random.uniform(-100, 100)
            x1 = random.uniform(-100, 100)
            f.write(f"y - {y1} = {m}(x - {x1})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 3 + 1):
            a = random.uniform(-100, 100)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            f.write(f"{a}x + {b}y = {c}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))

def quadratic():
    with open("data\\train\\quadratic.txt", "w") as f:
        for i in range(TRAIN // 3):
            a = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            f.write(f"y = {a}x^2 + {b}x + {c}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 3):
            a = random.uniform(-10, 10)
            h = random.uniform(-100, 100)
            k = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {h})^2 + {k}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 3):
            a = random.uniform(-10, 10)
            r1 = random.uniform(-100, 100)
            r2 = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {r1})(x - {r2})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
    with open("data\\test\\quadratic.txt", "w") as f:
        for i in range(TEST // 3):
            a = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            f.write(f"y = {a}x^2 + {b}x + {c}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 3):
            a = random.uniform(-10, 10)
            h = random.uniform(-100, 100)
            k = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {h})^2 + {k}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 3 + 1):
            a = random.uniform(-10, 10)
            r1 = random.uniform(-100, 100)
            r2 = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {r1})(x - {r2})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))

def cubic():
    with open("data\\train\\cubic.txt", "w") as f:
        for i in range(TRAIN // 3):
            a = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            d = random.uniform(-100, 100)
            f.write(f"y = {a}x^3 + {b}x^2 + {c}x + {d}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 3):
            a = random.uniform(-10, 10)
            h = random.uniform(-100, 100)
            k = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {h})^3 + {k}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 3):
            a = random.uniform(-10, 10)
            r1 = random.uniform(-100, 100)
            r2 = random.uniform(-100, 100)
            r3 = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {r1})(x - {r2})(x - {r3})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
    with open("data\\test\\cubic.txt", "w") as f:
        for i in range(TEST // 3):
            a = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            d = random.uniform(-100, 100)
            f.write(f"y = {a}x^3 + {b}x^2 + {c}x + {d}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 3):
            a = random.uniform(-10, 10)
            h = random.uniform(-100, 100)
            k = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {h})^3 + {k}\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 3 + 1):
            a = random.uniform(-10, 10)
            r1 = random.uniform(-100, 100)
            r2 = random.uniform(-100, 100)
            r3 = random.uniform(-100, 100)
            f.write(f"y = {a}(x - {r1})(x - {r2})(x - {r3})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))

def polynomial():
    with open("data\\train\\polynomial.txt", "w") as f:
        for i in range(TRAIN // 2):
            a = random.uniform(-10, 10)
            degree = random.randint(4, 10)
            poly = f"y = {a}x^{degree}"
            for j in range(degree - 1, -1, -1):
                poly += f" + {random.uniform(-100, 100)}x^{j}"
            poly = poly[:-3] + "\n"
            f.write(poly.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 2):
            degree = random.randint(4, 10)
            poly = f"y = "
            for j in range(1, degree):
                poly += f"(x - {random.uniform(-100, 100)})"
            poly += "\n"
            f.write(poly.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
    with open("data\\test\\polynomial.txt", "w") as f:
        for i in range(TEST // 2):
            a = random.uniform(-10, 10)
            degree = random.randint(4, 10)
            poly = f"y = {a}x^{degree}"
            for j in range(degree - 1, -1, -1):
                poly += f" + {random.uniform(-100, 100)}x^{j}"
            poly += poly[:-3] + "\n"
            f.write(poly.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 2):
            degree = random.randint(4, 10)
            poly = f"y = "
            for j in range(1, degree):
                poly += f"(x - {random.uniform(-100, 100)})"
            poly += "\n"
            f.write(poly.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))

def exponential():
    with open("data\\train\\exponential.txt", "w") as f:
        for i in range(TRAIN // 2):
            a = random.uniform(-100, 100)
            b = random.uniform(-100, 100)
            c = random.uniform(-10, 10)
            f.write(f"y = {a}*{b}^({c}x)\n")
        for i in range(TRAIN // 2):
            a = random.uniform(-100, 100)
            b = random.uniform(-10, 10)
            f.write(f"y = {a}*e^({b}x)\n")
    with open("data\\test\\exponential.txt", "w") as f:
        for i in range(TEST // 2):
            a = random.uniform(-100, 100)
            b = random.uniform(-100, 100)
            c = random.uniform(-10, 10)
            f.write(f"y = {a}*{b}^({c}x)\n")
        for i in range(TEST // 2):
            a = random.uniform(-100, 100)
            b = random.uniform(-10, 10)
            f.write(f"y = {a}*e^({b}x)\n")

def root():
    with open("data\\train\\root.txt", "w") as f:
        for i in range(TRAIN):
            a = random.uniform(-100, 100)
            b = random.uniform(-10, 10)
            root = random.randint(2, 10)
            f.write(f"y = ({a}(x + {b}))^(1/{root})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
    with open("data\\train\\root.txt", "w") as f:
        for i in range(TEST):
            a = random.uniform(-100, 100)
            b = random.uniform(-10, 10)
            root = random.randint(2, 10)
            f.write(f"y = ({a}(x + {b}))^(1/{root})\n".replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))

def rational():
    with open("data\\train\\rational.txt", "w") as f:
        for i in range(TRAIN // 2):
            a = random.uniform(-10, 10)
            degree = random.randint(4, 10)
            poly1 = f"{a}x^{degree}"
            for j in range(degree - 1, -1, -1):
                poly1 += f" + {random.uniform(-100, 100)}x^{j}"
            poly1 = poly1[:-3]
            a = random.uniform(-10, 10)
            degree = random.randint(4, 10)
            poly2 = f"{a}x^{degree}"
            for j in range(degree - 1, -1, -1):
                poly2 += f" + {random.uniform(-100, 100)}x^{j}"
            poly2 = poly2[:-3]
            rational = f"y = ({poly1}) / ({poly2})\n"
            f.write(rational.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TRAIN // 2):
            degree = random.randint(4, 10)
            poly1 = f""
            for j in range(1, degree):
                poly1 += f"(x - {random.uniform(-100, 100)})"
            degree = random.randint(4, 10)
            poly2 = f""
            for j in range(1, degree):
                poly2 += f"(x - {random.uniform(-100, 100)})"
            rational = f"y = ({poly1}) / ({poly2})\n"
            f.write(rational.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
    with open("data\\test\\rational.txt", "w") as f:
        for i in range(TEST // 2):
            a = random.uniform(-10, 10)
            degree = random.randint(4, 10)
            poly1 = f"{a}x^{degree}"
            for j in range(degree - 1, -1, -1):
                poly1 += f" + {random.uniform(-100, 100)}x^{j}"
            poly1 = poly1[:-3]
            a = random.uniform(-10, 10)
            degree = random.randint(4, 10)
            poly2 = f"{a}x^{degree}"
            for j in range(degree - 1, -1, -1):
                poly2 += f" + {random.uniform(-100, 100)}x^{j}"
            poly2 = poly2[:-3]
            rational = f"y = ({poly1}) / ({poly2})\n"
            f.write(rational.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))
        for i in range(TEST // 2):
            degree = random.randint(4, 10)
            poly1 = f""
            for j in range(1, degree):
                poly1 += f"(x - {random.uniform(-100, 100)})"
            degree = random.randint(4, 10)
            poly2 = f""
            for j in range(1, degree):
                poly2 += f"(x - {random.uniform(-100, 100)})"
            rational = f"y = ({poly1}) / ({poly2})\n"
            f.write(rational.replace("- -", "+ ").replace("+ -", "- ").replace("- +", "- "))

def power():
    with open("data\\train\\power.txt", "w") as f:
        for i in range(TRAIN):
            a = random.uniform(-100, 100)
            b = random.uniform(-10, 10)
            f.write(f"y = {a}x^{b}\n")
    with open("data\\test\\power.txt", "w") as f:
        for i in range(TEST):
            a = random.uniform(-100, 100)
            b = random.uniform(-10, 10)
            f.write(f"y = {a}x^{b}\n")

def logarithmic():
    with open("data\\train\\logarithmic.txt", "w") as f:
        for i in range(TRAIN):
            a = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            base = random.randint(2, 10)
            f.write(f"y = {a}*log_{base}({b}x + {c})\n")
    with open("data\\test\\logarithmic.txt", "w") as f:
        for i in range(TEST):
            a = random.uniform(-10, 10)
            b = random.uniform(-100, 100)
            c = random.uniform(-100, 100)
            base = random.randint(2, 10)
            f.write(f"y = {a}*log_{base}({b}x + {c})\n")

if input("CONFIRM? Y/N: ").strip().lower() == "y":
    constant()
    linear()
    quadratic()
    cubic()
    polynomial()
    exponential()
    root()
    rational()
    power()
    logarithmic()