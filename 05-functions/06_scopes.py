# def serve_chai():
#     chai_type = "masala" #local scope
#     print(f"Inside function {chai_type}")
    
# chai_type = "Lemon"
# serve_chai()
# print(f"outside function {chai_type}")

def chai_counter():
    chai_order = "lemon" #enclosing scope
    
    def print_order():
        chai_order = "Ginger"
        print("inner: ",chai_order) #inner scope
    print_order()
    
    print("outer: ", chai_order)
    
chai_order = "tulsi" # global scope
chai_counter()
print("Global: ", chai_order)