temp = input("Enter temperature to convert : ").strip()
try:
    value = float(temp[:-1])
    unit = temp[-1].upper()

    if unit == "C":
        converted = (value * 9/5) + 32  # F = C * 9/5 + 32 :contentReference[oaicite:0]{index=0}
        print(f"{value:.2f}°C is Converted  to {converted:.2f}°F")
    elif unit == "F":
        
        converted = (value - 32) * 5/9  # C = (F − 32) × 5/9 :contentReference[oaicite:1]{index=1}
        print(f"{value:.2f}°F is Converted  to {converted:.2f}°C")
    else:
        print("Invalid unit. Please end your input with 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid input format. Please enter a number followed by C or F.")
