# chai = "ginger chai"

# def prepare_chai(order):
#     print("Preapring ", order)
    
# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]

def edit_chai(cup): #parameter
    cup[1] = 42
edit_chai(chai) #arguments
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)
    
make_chai("Darjeeling", "Yess", "Low") #postionals
make_chai(tea="green", sugar="medium", milk="no") #keywords

def special_chai(*ingredients, **extras): #(*args, **kwargs)
    print("Ingredients", ingredients)
    print("Extras", extras)
    
special_chai("Cinnamon", "cardamom", sweetner="honey", foam="yes")

# def chai_order(order=[]):
#     order.append("masala")
#     print(order)
    
def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()

