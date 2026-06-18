seat_type = input("Enter seat type: (Sleeper, AC, general, luxury) ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper seat selected.")
    case "ac":
        print("AC seat selected.")
    case "general":
        print("General seat selected.")
    case "luxury":
        print("Luxury seat selected.")
    case _:
        print("Invalid seat type selected.")