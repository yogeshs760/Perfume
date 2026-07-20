# ==========================================
# STEP 1 & 2: Blueprint & Local Logic Zone
# ==========================================
def calculate_discount(cart_total, is_prime_member):
    # Local Variable (Sirf is function ke andar zinda hai)
    discount_percentage = 0 
    
    # Aapka Pure Logic Check
    if cart_total > 5000:
        discount_percentage = 20
    elif is_prime_member == True:
        discount_percentage = 10
    else:
        discount_percentage = 0
        
    # Final result ko bahar bhejna (Return)
    return discount_percentage


# ==========================================
# STEP 3: Outside World / Execution Zone
# ==========================================
# Asli data jo badal sakta hai (Global Input)
customer_cart = 6000
customer_is_prime = False

# Function ko call karna aur result variable mein store karna
final_discount = calculate_discount(customer_cart, customer_is_prime)

# Output screen par dikhana
print(f"User ko {final_discount}% ka discount mila!")