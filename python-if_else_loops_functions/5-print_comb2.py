#!/usr/bin/python3
for i in range(100):
    if i <= 98:
        print(format(i, '02d'), end=", ")
    else:
        print("{}".format(i))
