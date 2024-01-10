#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

<<<<<<< HEAD
    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight
        
        return (total_score / total_weight)
=======
    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]
>>>>>>> 334d4bcf3b58a37d33405212195fd57a676c9471

    return (num / den)
