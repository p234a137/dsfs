# generators and iterators

# create a generator with a function and the yield operator
def lazy_range(n):
    """lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1

# consume the yielded values
for i in lazy_range(10):
    print("consume yielded value: ", i)

# create generator with comprehension included in parantheses
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
print("lazy evens below 20")
for i in lazy_evens_below_20:
    print(i)
