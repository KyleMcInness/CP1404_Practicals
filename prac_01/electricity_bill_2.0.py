TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Please enter the tariff's number that you use: "))
if tariff == 11:
    price = TARIFF_11
elif tariff == 31:
    price = TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

bill = price*daily_use*billing_days

print("Estimated bill: ${:.2f}".format(bill))
