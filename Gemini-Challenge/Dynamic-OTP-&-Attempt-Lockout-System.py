correct_otp = 4321
attempts_left = 3

# While loop chalega jab tak attempts 0 na ho jayein
while attempts_left > 0:
    user_entered_otp = int(input("Enter OTP: "))
    
    if user_entered_otp == correct_otp:
        print("Login successful")
        break  # Sahi OTP milte hi loop se bahar niklo!
    else:
        attempts_left -= 1  # Ek attempt kam ho gaya
        if attempts_left > 0:
            print(f"Login unsuccessful and {attempts_left} attempts remaining")

# Jab attempts khatam ho kar 0 ho jayein (Loop se bahar)
if attempts_left == 0:
    print("Your Account has been locked for 24 Hours")