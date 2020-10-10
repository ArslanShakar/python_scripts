import math

cols = ["Number", "Square", "Cube", "Square root", "Reciprocal"]
print(f"{cols[0]:20} {cols[1]:20} {cols[2]:20} {cols[3]:20} {cols[4]:20}")

for i in range(1, 11):
    square = f"{i ** 2}"
    cube = f"{i ** 3}"
    sqrt_root = f"{math.sqrt(i):.2f}"
    rec = f"{1 / i:.2f}"

    print(f"{str(i):20} {square:20} {cube:20} {sqrt_root:20} {rec:20}")
