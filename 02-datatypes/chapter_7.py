masala_spice = ("ginger", "cinnamon", "cardamom", "cloves", "nutmeg")
(spice1, spice2, spice3, spice4, spice5) = masala_spice
print(f"Main masala spices: {spice1}, {spice2}, {spice3}, {spice4}, {spice5}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G {ginger_ratio} and C {cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio #value swap
print(f"Ratio is G {ginger_ratio} and C {cardamom_ratio}")

#membership test
print(f"Is cinnamon in the masala spice? {'cinnamon' in masala_spice}")
print(f"Is Tea in the masala spice? {'Tea' in masala_spice}")