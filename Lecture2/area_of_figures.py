from math import pi
figure = str(input())

if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = pi * (r * r)
elif figure == "triangle":
    l = float(input())
    h = float(input())
    area = (l * h) / 2

print(f"{area:.3f}")
