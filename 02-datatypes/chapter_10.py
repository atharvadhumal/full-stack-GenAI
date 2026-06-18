chai_order = dict(type="chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe ={} 
chai_recipe["base"] = "black tea" # Add the base to the recipe
chai_recipe["liquid"] = "milk" # Add the liquid to the recipe

print(f"recipe base: {chai_recipe['base']}")
print(f"Recipe : {chai_recipe}")
del chai_recipe["liquid"] # Remove the liquid from the recipe
print(f"recipe after removing liquid: {chai_recipe}")

#membership test
print(f"Does the recipe have a base? {'base' in chai_recipe}")
print(f"Does the recipe have a sugar? {'sugar' in chai_order}")


chai_order = {"type": "chai", "size": "Large", "sugar": 2}
print(f"Order details(keys):  {chai_order.keys()}")
print(f"Order details(values):  {chai_order.values()}")
print(f"Order details(items):  {chai_order.items()}")
