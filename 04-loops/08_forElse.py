staff = [("amit", 16), ("sachin", 18), ("rahul", 19), ("rohit", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to vote.")
        break #if someone is 18 it will break , even if there are more people in the list
else:
    print("No eligible voters found.")
    
#short explanation:
# This code iterates through a list of staff members, checking their ages. If it finds any staff member who is 18 or older, it prints that they are eligible to vote and exits the loop. If the loop completes without finding any eligible voters, it prints a message indicating that no eligible voters were found. The `else` block is executed only if the loop is not terminated by a `break` statement.