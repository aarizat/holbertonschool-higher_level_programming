#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    if my_list:
        w = 0
        for score, weight in my_list:
            average += score * weight
            w += weight
        average = average / w
    return average
