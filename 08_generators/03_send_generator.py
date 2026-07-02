def chai_customer():
    print("welcome ! what you need")
    order = yield
    while True:
        print(f"Preparing : {order}")
        order = yield

stall = chai_customer()
next(stall)

stall.send("masala chai")