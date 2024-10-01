#!/usr/bin/python3


def best_score(a_dictionary):
    if bool(a_dictionary) is False:
        return None
    best = ""
    score = 0
    for k, v in a_dictionary.items():
        if v > score:
            score = v
            best = k
    return best
