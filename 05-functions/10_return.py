def make_chai():
    return "here is your order"

return_value = make_chai()

print(return_value)


def sold_cups():
    return 120

total = sold_cups
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "sorry"
    return "ready"