sales = [1500, 2200, 800, 3100, 1900]

total_sales = 0
max_sale = 0

for sale in sales:
    # 1. Total increment karna
    total_sales += sale  # total_sales = total_sales + sale
    
    # 2. Maximum dhoondna (Condition Check)
    if sale > max_sale:
        max_sale = sale

print(f"Total Sales: {total_sales}, Max Sale: {max_sale}")