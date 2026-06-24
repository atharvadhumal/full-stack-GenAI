#one method to import
# import recipes.flavors #we imported it from recipe folder the name flavor.py

# print(recipes.flavors.elachi_chai)

#another way to import
# from recipes.flavors import elachi_chai, ginger_chai

# print(ginger_chai())

from .recipes.flavors import ginger_chai