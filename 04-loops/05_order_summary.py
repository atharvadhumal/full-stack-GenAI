names = ["hitesh", "suresh", "ramesh"]
bills = [100, 200, 300]

for names, bills in zip(names, bills):
    print(f"{names} has to pay {bills}")
    
#short explaination: The code uses the `zip` function to iterate over two lists, `names` and `bills`, simultaneously. For each pair of name and bill, it prints a formatted string that indicates how much each person has to pay.