# 1. Hamein transaction data mila
transactions = [100, 200, 150, 80000, 120]

# 2. Shuruati safe transactions se average nikala
safe_transactions = transactions[:3] # Pehle 3 numbers le liye
average_amount = sum(safe_transactions) / len(safe_transactions) # Average = 150

# 3. Baaki ke transactions par loop chala kar check kiya (Pure Logic)
for tx in transactions:
    if tx > (average_amount * 5): # Agar transaction average ke 5x se bada hai
        print(f"Alert: Suspicious Transaction Detected! Amount: {tx}")