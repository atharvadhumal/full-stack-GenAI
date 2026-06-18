flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Mint"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")
    
print(f"outside of loop")