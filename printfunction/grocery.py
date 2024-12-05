prices={
    "apple":0.50,
    "banana":0.39,
    "Milk":1.23,
    "Cake":2.34,
    "Cheese":4.33
}

item1_name = input("Enter the name of the first item").lower()
item1_qty = int(input(f"Enter the quantity of {item1_name}"))

item2_name =input("Enter the name of the second item").lower()
item2_qty =int(input("Enter the quantity of {item2_name}"))

item3_name = input("Enter the name of the third item").lower()
item3_qty = int(input(f"Enter the quantity of {item3_name}"))


item1_price =prices.get(item1_name,0)
item2_price =prices.get(item2_name,0)
item3_price =prices.get(item3_name,0)

item1_total=item1_price *item1_qty
item2_total=item2_price *item2_qty
item3_total=item3_price *item3_qty

subtotal=item1_total+item2_total+item3_total
tax =subtotal * 0.085
total_amount = subtotal +tax

print("\n---Receipt----")
print("f{item1_name.captilization()}:{item1_qty} @ ${item1_price:.2f} each= ${item1_total:.2f}")
print("f{item2_name.captilization()}:{item2_qty} @ ${item2_price:.2f} each= ${item2_total:.2f}")
print("f{item3_name.captilization()}:{item3_qty} @ ${item3_price:.2f} each= ${item3_total:.2f}")

print(f"Subtotal:${subtotal:.2f}")
print(f"Tax(8.5%): ${tax:.2f}")
print(f"Total Amount : {total_amount:.2f}")