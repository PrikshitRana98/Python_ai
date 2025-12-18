class Chaicup:
    size= 150#ml

    def description(self):
        return f"This chai cup is of {self.size} ml"
    


myChai=Chaicup()

print(myChai.description()) 

# print(Chaicup.description()) 

# # This will give error because description method needs an instance to be called 

# Aapko error isliye mila kyunki description ek instance method hai, lekin aap usse class (Chaicup) par bina object banaye call kar rahe hain.

# Explanation:

# def description(self): me self ka matlab hai ki yeh method sirf object (instance) ke through hi call ho sakta hai, class ke through nahi.
# Jab aap Chaicup.description() likhte hain, to Python ko self nahi milta, isliye error deta hai (usually: TypeError: description() missing 1 required positional argument: 'self').


print(Chaicup.description(myChai))  # Ab yeh sahi hai kyunki humne myChai object ko self ke roop mein pass kiya hai