# Variables jo AI variables/libraries se uthayega:
continuous_play_time = 260      # Maan lo video 260 mins se chal raha hai
user_interacted = False          # Kya user ne screen ko touch kiya? (False matlab nahi kiya)

# --- AAPKA LOGIC START ---

# Rule: Agar video 240 mins se zyada chal gaya HAI aur user ne koi click/movement NAHI kiya hai
if continuous_play_time > 240 and user_interacted == False:
    print("Are you still watching?")
    # Yahan screen par prompt aa jayega aur video pause ho jayega
else:
    print("Video smoothly chalta rahe...") # Kyunki user active hai ya time limit cross nahi hui