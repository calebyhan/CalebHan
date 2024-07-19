# problem 5 FHS

print("Currency Conversion Menu")
print("1. Convert from Euros to US Dollars (EUR to USD) ")
print("2. Convert from US Dollars to Euros (USD to EUR) ")

x = int(input("Please select a conversion option (1/2): "))
if x == 1:
    n = float(input("Enter the amount in Euros: "))
    print("The equivalent amount in Euroes (EUR) is:", f"{n * 1.18:.2f}", " EUR")
elif x == 2:
    n = float(input("Enter the amount in US Dollars: "))
    print("The equivalent amount in US Dollars (USD) is: $", f"{n / 1.18:.2f}")
