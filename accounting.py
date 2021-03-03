# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )

# variable melon cost $1
# def a function that takes in a text file
#   create variable that opens text file
#   create variable that stores the customer name
#   create variable that stores the amount of melons purchased
#   create variable that stores the price paid for melons
#   create variable that's the evaluated result that should be   charged 
#       if amount expected is not the amount paid:
#           display customer name paid x amount, expected x amount 




MELON_COST = 1.00
def customer_payment_status(customer_payment_file_name):
    """Calculate cost of melons and determines who is underpaid"""
    
    customer_payment_data = open(customer_payment_file_name)
    
    for line in customer_payment_data:
    
        order = line.split('|')
        full_name = order[1]
        first_name = full_name.split(" ")[0]
        melon_count = float(order[2])
        amount_paid = float(order[3])
        expected_price = melon_count * MELON_COST

    print(f"{full_name} paid ${amount_paid:.2f}, expected", f"${expected_price:.2f}")

    if expected_price != amount_paid:

        if expected_price < amount_paid:
            payment_status = "underpaid"
        
        else:
            payment_status = "overpaid"

            print(f"{full_name} has {payment_status} for their melons.")

    customer_payment_data.close()

customer_payment_status("customer-orders.txt")