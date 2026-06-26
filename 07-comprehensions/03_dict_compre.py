tea_prices_inr = {
    "masala chai": 40,
    "green chai" : 50,
}

tea_prices_usd = { tea:price / 80 for tea, price in tea_prices_inr.items() }
print(tea_prices_usd)