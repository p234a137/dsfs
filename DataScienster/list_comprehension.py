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
