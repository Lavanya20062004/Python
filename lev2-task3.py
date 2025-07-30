import re
password = input("Enter a password to evaluate: ")
if len(password) < 8:
    print("Weak: Password must be at least 8 characters long.")
else:
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    missing = []
    if not has_upper:
        missing.append("uppercase letter")
    if not has_lower:
        missing.append("lowercase letter")
    if not has_digit:
        missing.append("digit")
    if not has_special:
        missing.append("special character")

    if missing:
        print("Weak: Password is missing:", ", ".join(missing) + ".")
    elif len(password) >= 12:
        print("Strong password.")
    else:
        print("Moderately strong—consider using more than 12 characters.")
