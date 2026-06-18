ingredients = ["water", "milk", "black-tea"]
ingredients.append("sugar") #means to add sugar to the list of ingredients
print(f"Ingredients: {ingredients}")
ingredients.remove("milk") #means to remove milk from the list of ingredients
print(f"Ingredients after removing milk: {ingredients}")

spice_options = ["ginger", "cardamom", "cinnamon"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options) #means to add spice_options to the list of chai_ingredients
print(f"Chai Ingredients: {chai_ingredients}")

chai_ingredients.insert(2, "black-tea") #means to add black-tea at index 2 in the list of chai_ingredients
print(f"Chai Ingredients after inserting black-tea: {chai_ingredients}")