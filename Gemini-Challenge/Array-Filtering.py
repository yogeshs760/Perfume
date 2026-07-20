Result_list = []
product_price = [600, 500, 200, 300]

for product in product_price:
    if product > 100:
        Result_list.append(product)

print(Result_list)  # Output: [600, 500, 200, 300]