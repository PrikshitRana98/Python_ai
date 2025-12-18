class Chai:
    origin = "India"


print(Chai.origin)  # Accessing class variable without creating an instance

Chai.is_hot = True  # Adding a new class variable dynamically
print(Chai.is_hot)  # Accessing the newly added class variable

masala_tea = Chai()  # Creating an instance of the Chai class

print("masala:",masala_tea.origin)  # Accessing class variable through an instance
masala_tea.origin = "Sri Lanka"  # Creating an instance variable with the same name
print(masala_tea.origin)  # Accessing the instance variable


masala_tea.is_hot = False  # Creating an instance variable with the same name
print(masala_tea.is_hot)  # Accessing the instance variable
print(Chai.is_hot)  # Accessing the class variable to show it remains unchanged

masala_tea.flavors = ["cardamom", "ginger", "clove"]  # Adding an instance variable
print(masala_tea.flavors)  # Accessing the instance variable