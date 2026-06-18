menu = ["Green", "lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start = 1):
    print(f"{idx}: {item} chai")
    
#explanation: The code defines a list called `menu` that contains different types of tea. It then uses a `for` loop with the `enumerate` function to iterate over the items in the `menu` list. The `enumerate` function provides both the index (starting from 1, as specified by `start=1`) and the item itself. Inside the loop, it prints out each index and corresponding tea type in a formatted string, appending "chai" to each tea name.