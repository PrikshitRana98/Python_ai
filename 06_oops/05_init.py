class Chaiorder:

    def __init__(self,name_, type_,quantity_):
        self.name= name_
        self.type= type_
        self.quantity= quantity_

    def order_summary(self):
        return f"Order Summary: {self.quantity} cup(s) of {self.type} chai for {self.name}."
    


myOrder= Chaiorder("Amit", "Masala", 2)

print(myOrder.order_summary())