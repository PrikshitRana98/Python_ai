def regular_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


print(regular_numbers(5))


# ✔ Stores the entire list in memory
# ❌ Uses more RAM
# ❌ Slow for large data


def generator_numbers(n):
    for i in range(n):
        yield i


gen = generator_numbers(5)
print("Generator numbers:", gen)
print ("Values from generator:",next (gen))
for num in gen:
    print(num)

def print_value():
    yield "me"
    yield "you"
    yield "us"

val=print_value()
print("Values from print_value generator:",next(val))


# ✔ Doesn’t store anything in memory
# ✔ Values are produced on-demand
# ✔ Can handle millions of items without RAM issues
# ✔ Much faster for large data




# infinite generator
def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

infinite_gen = infinite_numbers()
for _ in range(5):
    print("Infinite generator number:", next(infinite_gen))


#     ✔ Infinite generator = generator that runs forever
# ✔ Useful for:

# streaming data

# simulation

# mathematical sequences

# real-time logs

# lazy loading large inputs

# generating unique IDs

# ✔ Works because values are produced one-by-one instead of storing everything.