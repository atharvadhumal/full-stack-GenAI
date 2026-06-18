# value = 13
# remainder = value % 5

# if remainder:
#     print(f"{value} is not divisible by 5, remainder is {remainder}")

value = 13

if (remainder := value % 5):
    print(f"{value} is not divisible by 5, remainder is {remainder}")
    
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter a size: ")) in available_sizes:
    print(f"{requested_size} is available")
else:    print(f"{requested_size} is not available")