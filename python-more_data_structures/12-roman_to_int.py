#!/usr/bin/python3
def str_to_list_w_dict(dictionary, string=""):
    new_list = list()
    for i, v_list in enumerate(string):
        for k, v_dict in dictionary.items():
            if v_list == k:
                new_list.append(v_dict)
    return new_list


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(reversed(str_to_list_w_dict(rom_dic, roman_string)))
    dec_number = 0
    last_v = 0

    for i, v in enumerate(roman_list):
        if i == 0:
            dec_number = v
            last_v = v
            continue
        if last_v < v or last_v == v:
            dec_number += abs(v)
            last_v = v
        else:
            dec_number -= abs(v)
            last_v = v
    return abs(dec_number)
