#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i, v in enumerate(my_list):
            if i == x:
                break
            print(v, end="")
        print()
        return i
    except:
        print("Unknown error")
