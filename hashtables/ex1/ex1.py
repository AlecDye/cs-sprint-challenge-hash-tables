"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21

output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

hint: What if we store each weight in the input list as keys? What would be
  a useful thing to store as the value for each key? 

hint: If we store each weight's list index as its value, we can then check
  to see if the hash table contains an entry for `limit - weight`. If it
  does, then we've found the two items whose weights sum up to the
  `limit`!
"""


# 1/4 pass
# TypeError: 'NoneType' object is not subscriptable
# 3/4 pass
# [12, 6, 7, 14, 19, 3, 0, 25, 40] func(weights_4, 9, 7)
# expect: [6, 2]


def get_indices_of_item_weights(weights, length, limit):
    # IMPORTANT cache needs to be in scope of func or test data persists
    cache = {}
    # loop through length of index
    for i in range(length):
        item_weight = weights[i]
        load = limit - item_weight
        if load in cache:
            u = cache[load]
            return [i, u]
        else:
            cache[item_weight] = i
    return None


weights_1 = [9]
print(get_indices_of_item_weights(weights_1, 1, 9))
# expect: None
# output: None

weights_2 = [4, 4]
print(get_indices_of_item_weights(weights_2, 2, 8))
# expect: [1, 0]
# output: [1, 0]

weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))
# expect: [3,1]
# output: [3,1]

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))
# expect: [6, 2]
# when run by itself:
# output: [6, 2] ????
# when run with other tests
# output: [5, 0] ????
