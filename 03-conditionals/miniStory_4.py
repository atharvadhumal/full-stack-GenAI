device_status = "offline"
temperature = 34

if device_status == "active":
    if temperature > 35:
        print(f"High temperature alert: {temperature}°C")
    else:
        print("Temperature is normal.")
else:
    print(f"Device is offline")
    
    #short explanation about nested conditionals: Nested conditionals allow you to check multiple conditions within each other. In this example, we first check if the device is active. If it is, we then check the temperature to determine if it's too high or normal. If the device is offline, we skip the temperature check and simply notify that the device is offline. This structure helps in organizing code and making decisions based on multiple criteria.