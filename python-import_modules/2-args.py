#!/usr/bin/python3


def dynamic(argv):
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    if argc == 1:
        print("1 argument:")
    if argc > 1:
        print(f"{argc} arguments:")
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print(f"{i}: {arg}")


if __name__ == "__main__":
    import sys
    dynamic(sys.argv)
