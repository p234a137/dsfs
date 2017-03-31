#List Comprehension

import pprint

even_numbers = [x for x in range(10) if x%2 ==  0]
print("even numbers")
pprint.pprint(even_numbers)


squares = [x*x for x in range(10)]
print("squares")
pprint.pprint(squares)

even_squares = [x*x for x in even_numbers]
print("even squares")
pprint.pprint(even_squares)

square_dict = {x: x*x for x in range(10) }
print("square dict")
pprint.pprint(square_dict)

square_set = {x*x for x in range(10) }
print("square set")
pprint.pprint(square_set)

zeroes = [0 for _ in even_numbers] # use _ if you do not need the value from the list
print("zeroes")
pprint.pprint(zeroes)


# A list comprehension can include multiple for-s
# and later for-s can use the results of earlier ones
pairs = [ (x, y)
        for x in range(3)
        for y in range(3)
        ]
print("pairs")
pprint.pprint(pairs)

increasing_pairs = [(x, y)        # only pairs with x < y
        for x in range(4)        # range(lo, hi) equals
        for y in range(x+1, 4)   # [lo, lo+1, ..., hi-1]
        ]
print("increasing pairs")
pprint.pprint(increasing_pairs)
