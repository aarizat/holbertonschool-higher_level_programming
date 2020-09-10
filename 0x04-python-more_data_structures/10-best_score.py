#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        dict_ord = sorted(a_dictionary.items(), key=lambda k_v: k_v[1])
        if a_dictionary.get(dict_ord[-1][0]):
            return dict_ord[-1][0]
    return
