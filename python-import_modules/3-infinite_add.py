#!/usr/bin/python3


def add_arg(argv):
    sum_result = 0
    for arg in argv:
        if arg == "./3-infinite_add.py":
            continue
        sum_result += int(arg)
    print(f"{sum_result}")


if __name__ == "__main__":
    from sys import argv
    add_arg(argv)
