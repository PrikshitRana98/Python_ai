class Chai:
    temperature = "Hot"  # Class attribute
    strength = "Strong"  # Class attribute
    value = 10  # Class attribute

obj = Chai()
print(obj.value)  # Outputs: 10 (from class)

obj.value = 20    # Instance attribute shadows class attribute
print(obj.value)  # Outputs: 20 (from instance)

del obj.value
print(obj.value)  # Outputs: 10 (class attribute visible again)


massala=Chai()
print(massala.temperature)  # Accessing class attribute

massala.cup="Large"  # Creating instance attribute
print(massala.cup)  # Accessing instance attribute

massala.temperature="Warm"  # Creating instance attribute that shadows class attribute
print("tempature of massala",massala.temperature)  # Accessing instance attribute
del massala.temperature  # Deleting instance attribute
print("tempature of massala after deleting instance attribute:",massala.temperature)  # Access

del massala.cup  # Deleting instance attribute

print("cup of massala:",massala.cup)  # Accessing class attribute and shows error because instance attribute is deleted