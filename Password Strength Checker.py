import  re
password = input("Enter your password :")
score = 0

if len(password) >= 10:
    score += 1
else:
    print("Password must be at least 10 characters long.")

if re.search("[A-Z]", password):
    score += 1
else:
    print("Password must contain at least one uppercase letter.")

if re.search("[a-z]", password):
    score += 1
else:
    print("Password must contain at least one lowercase letter.")

if re.search("[0-9]", password):
    score += 1
else:
    print("Password must contain at least one number.")

if re.search("[@#$%^&+=!?]", password):
    score += 1
else:
    print("Password must contain at least one special character (@#$%^&+=!?).")

if score == 5:
    print("Password is strong.")
elif score >= 3:
    print("Password is moderate.")
else:
    print("Password is weak.")


