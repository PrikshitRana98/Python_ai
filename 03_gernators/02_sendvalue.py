def chai_customer():
    print("What you tou like to have?")
    order = yield
    while True:
        print(f"Preparing your {order}. Please wait...")
        order = yield f"Your {order} is ready! What would you like next?"


stall=chai_customer()
next(stall) # Start the generator and get the first prompt

print(stall.send("Masala Chai"))  # Send order and get confirmation
print(stall.send("Ginger Chai"))  # Send another order and get confirmation