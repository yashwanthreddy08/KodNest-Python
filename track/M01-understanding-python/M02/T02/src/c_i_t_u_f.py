def display_invoice_total(price, quantity):
    total=price*quantity
    print("Total:", total)

price = int(input("Enter the price: "))
quantity= int(input("Enter the Quantity: "))
display_invoice_total(price, quantity)