import re
email = input("Enter an email address: ").strip()

if email.count('@') != 1:
    print("Invalid: must contain exactly one '@'")
else:
    local, domain = email.split('@')
    if not local or not domain:
        print("Invalid: local or domain part is empty")
    elif '.' not in domain:
        print("Invalid: domain must contain a '.'")
    else:
        
        pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
        if pattern.fullmatch(email):
            print("Valid email address")
        else:
            print("Invalid: does not match standard email format")
