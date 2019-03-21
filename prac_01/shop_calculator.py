TOTAL_PRICE = 0
number_of_items = int(input("Enter the number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items: "))
for i in range(number_of_items):
    price = float(input("Enter the price of the item: $"))
    TOTAL_PRICE += price
if TOTAL_PRICE >= 100:
    TOTAL_PRICE = TOTAL_PRICE - TOTAL_PRICE * 0.10
print("Total price for {} item(s): ${:.2f}".format(number_of_items, TOTAL_PRICE))
