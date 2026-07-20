Balance = 700

if Balance >= 500:
    print("Sufficient Balance")
elif Balance < 500 and Balance > 100:
    print("Low Balance Warning: Top up soon!")
else:
    print("Transaction Declined: Insufficient Funds")