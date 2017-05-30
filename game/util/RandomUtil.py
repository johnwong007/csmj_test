# coding=utf-8
import random

COLOR_DEFINE = {0: 'club', 1: 'diamond', 2: 'heart', 3: 'spade', 4: 'little joker', 5: 'big joker'}


def get_next_card(current_gold_pool):
    little_joker_probability = int(current_gold_pool / 1000)
    big_joker_probability = int(current_gold_pool / 1000)
    weight = list([2500, 2500, 2500, 2500])
    weight.append(little_joker_probability)
    weight.append(big_joker_probability)
    index = get_index_from_weight(weight)
    return index


def get_index_from_weight(weight):
    # print "weight=", weight
    totail = reduce(lambda x, y: x + y, weight)
    # print "totail=", totail
    r = random.randint(0, totail)
    if r < 2500:
        return 0
    elif r < 5000:
        return 1
    elif r < 7500:
        return 2
    elif r < 10000:
        return 3
    else:
        big_or_little = random.randint(1, 2)
        if big_or_little == 1:
            return 4
        else:
            return 5


if __name__ == "__main__":
    count = 0
    for i in xrange(100000):
        index = get_next_card(i)
        if index > 3:
            print i, ":", index
            count += 1
    print "count = ", count
