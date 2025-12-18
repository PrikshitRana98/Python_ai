# generatoer comprehension

# syntax: (expression for item in iterable if condition)

squares = (x * x for x in range(10))
print("Generator of squares from 0 to 9:")

daily_cups=[5,6,7,8,9,10,13,14,16,18]

above_ten=sum(x for x in daily_cups if x>10)
print("Cups above 10:", above_ten)

count_above_ten=sum(1 for x in daily_cups if x>10)
print("Count of days with cups above 10:", count_above_ten) 