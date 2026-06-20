def calulate_bills(cups, price_per_cups):
    return cups * price_per_cups

my_bill = calulate_bills(3, 15)
print(my_bill)

print(f"Order is for ", calulate_bills(2, 15))