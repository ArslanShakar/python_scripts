import math

width = 20
cols = ["Number", "Square", "Cube", "Square root", "Reciprocal"]
print("{0:<{1}} {2:<{1}} {3:<{1}} {4:<{1}} {5:<{1}}".format(cols[0][:width], width,
                                                            cols[1][:width],
                                                            cols[2][:width],
                                                            cols[3][:width],
                                                            cols[4][:width]))

for i in range(1, 11):
    square = "{}".format(i ** 2)
    cube = "{}".format(i ** 3)
    sqrt = "{0:.2f}".format(math.sqrt(i))
    rec = "{0:.2f}".format(1 / i)

    print("{0:<{1}} {2:<{1}} {3:<{1}} {4:<{1}} {5:<{1}}".format(str(i)[:width], width,
                                                                square[:width],
                                                                cube[:width],
                                                                sqrt[:width],
                                                                rec[:width]))
