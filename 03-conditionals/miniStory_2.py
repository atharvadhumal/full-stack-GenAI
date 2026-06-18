snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa": #or is used to check multiple conditions
    print("Yum! That's a delicious choice!")
else:
    print(f"sorry, {snack} is not available. we only have cookies and samosa.")