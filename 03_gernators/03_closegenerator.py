def breakfast():
    yield "pancakes"
    yield "eggs"
    yield "bacon"
    yield "toast"

def drink():
    yield "coffee"
    yield "tea"
    yield "juice"

def complete_meal():
    yield from breakfast()
    yield from drink()

meal = complete_meal()
for item in meal:
    print("Meal item:", item)



meal.close()  # Close the generator when done