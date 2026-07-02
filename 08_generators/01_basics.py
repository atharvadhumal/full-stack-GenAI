def serve_chai():
    yield "cup 1: masala chai"
    yield "cup 2 ginger chai"
    
stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return["cup 1", "cup 2", "cup 3"]

#same can we written using the generator

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"

chai = get_chai_gen()
print(next(chai)) #gives only cup 1 as value but stores cup 2 also
print(next(chai)) #this will print cup 2
# print(next(chai))#throws error