class Chaiorder:

    def __init__(self, tea_type):
        self.tea_type = tea_type
       
    def prepare_tea(self):
        print(f"Preparing a cup of {self.tea_type} tea.")
    

#normal class syntax: class Class_Name:
# Inheritance class syntax: class Derived_ClassName(BaseClassName): in this case Chaiorder is base class and MasalaChai is derived class

class MasalaChai(Chaiorder):

    def addingSpices(self):
        print("Adding spices to the chai. cardamom, ginger, clove.")


# composition is a design principle where a class is composed of one or more objects of other classes in order to achieve reusability and modularity.
class ChaiShop:
    
    chai_cls= Chaiorder  # here Chaiorder class is being used inside ChaiShop class and why we not put () because we are not creating an object of Chaiorder class here, we are just referencing it meanse reference the whole class.

    def __init__(self):
        self.chai= self.chai_cls("Regular ")  # here we are creating an object of Chaiorder class inside ChaiShop class

    def serve_tea(self):

        print(f"Serving the {self.chai.tea_type} tea to the customer.")
        self.chai.prepare_tea()

class FancyChaiShop(ChaiShop):  # inheriting ChaiShop class

    chai_cls= MasalaChai  # overriding the chai_cls attribute to use MasalaChai class instead of Chaiorder class

    def serve_fancy_tea(self):
        print("Serving fancy tea with extra toppings.")
        self.chai.prepare_tea()

shop= ChaiShop()
shop.serve_tea()


FancyChaiShop= FancyChaiShop()
FancyChaiShop.serve_fancy_tea()
FancyChaiShop.chai.addingSpices()

FancyChaiShop.chai_cls.tea_type= "adrak"  # changing the tea_type attribute of MasalaChai class
FancyChaiShop.serve_fancy_tea()