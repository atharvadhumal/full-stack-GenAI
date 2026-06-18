essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black-pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}") #we get a set of all the spices without duplicates

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}") #we get a set of spices that are in both sets, which is "ginger"

only_in_essential = essential_spices - optional_spices
print(f"Spices only in essential: {only_in_essential}") #we get a set of spices that are in essential_spices but not in optional_spices

print(f"Is clove in optional? {'cloves' in optional_spices}") #we check if "cloves" is in optional_spices, which is True