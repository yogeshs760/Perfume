price = 3000

# 1. PEHLE EDGE CASE CHECK (Photo 2 wala solid logic)
if price is None or price == "Out of Stock" or price == "":
    print("Product Unavailable")

# 2. FIR PRICE DROP CHECK
elif price < 2000:
    print("Price Drop Alert! Buy Now.")

# 3. DEFAULT EXIT
else:
    print("Regular Price")