import math


def objetosc_szescianu(bok):
    return bok ** 3


def pole_szescianu(bok):
    return 6 * bok ** 2


def objetosc_prostopadloscianu(a, b, c):
    return a * b * c


def pole_prostopadloscianu(a, b, c):
    return 2 * (a*b + b*c + a*c)


def objetosc_kuli(promien):
    return (4/3) * math.pi * promien ** 3


def pole_kuli(promien):
    return 4 * math.pi * promien ** 2
