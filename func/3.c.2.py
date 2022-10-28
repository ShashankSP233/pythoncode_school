def volcal(l, b, h):
    return l * b * h


def volstr():
    a = int(input('enter length:'))
    b = int(input('enter breadth:'))
    c = int(input('enter height:'))
    print(volcal(a, b, c))


volstr()
