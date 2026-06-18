users = [
    {"id": 1, "total": 100, "coupon": "P10"},
    {"id": 2, "total": 200, "coupon": "F20"},
    {"id": 3, "total": 300, "coupon": "P30"},
]

discounts = {
    "P10": (0.1, 0),
    "F20": (0.5, 0),
    "P30": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discounts = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of ruppess {discounts}")