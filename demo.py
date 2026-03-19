from math import sin
from time import sleep
row = 0


def get_char(n: float):
    gradient = ".:-=+*%#@"
    return gradient[int(n * (len(gradient) - 1))]

while True:
    row += 1
    maxDepth = 25
    frequency = 0.2
    n = sin(row * frequency) * 0.5 + 0.5
    depth = 1 + int(n * maxDepth)
    maxi = depth - 1.0;
    for i in range(depth + 1):
        normalizedDepth = i / (depth)
        darknessChar = get_char(normalizedDepth)
        print(darknessChar, end=" ")

    d = maxDepth - depth
    for i in range(d + 1):
        normalizedDepth = (d - i) / (d + 1)
        darknessChar = get_char(normalizedDepth)
        print(darknessChar, end=" ")

    print()
    
    sleep(0.1)
