def serve_chai(flavor):
    try:
        print("Perparing your", flavor)
        if flavor=="unknown":
            raise ValueError("We don't have this flavor")
        
    except ValueError as ve:
        print("Value Error:", ve)
    else:
        print("Here is your", flavor)
    finally:
        print("Thank you for visiting Chai Point and next customer please") # this will always execute



serve_chai("masala chai")
serve_chai("unknown")