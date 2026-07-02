def local_chai():
    yield "Masala chai"
    yield "ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)
    

def chai_stall():
    try:
        while True:
            order = yield "waiting for the chai"
    except:
        print("stall closed")
    
stall = chai_stall()
print(next(stall))
stall.close