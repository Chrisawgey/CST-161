def calculate_payment_schedule(purchase_price):
    down_payment = 0.10 * purchase_price
    balance = purchase_price - down_payment
    monthly_interest_rate = 0.12 / 12
    monthly_payment = 0.05 * purchase_price  # Initialize monthly_payment here

    print(f"{'Month':<10}{'Balance':<15}{'Interest':<15}{'Principal':<15}{'Payment':<15}{'Ending balance':<15}")

    month = 1
    while balance > 0:
        monthly_interest = balance * monthly_interest_rate
        if balance < monthly_payment:
            monthly_payment = balance + monthly_interest
        monthly_principal = monthly_payment - monthly_interest
        balance -= monthly_principal
        print(f"{month:<10}{balance:<15.2f}{monthly_interest:<15.2f}{monthly_principal:<15.2f}{monthly_payment:<15.2f}{balance:<15.2f}")
        month += 1

purchase_price = float(input("Enter the purchase price: "))
calculate_payment_schedule(purchase_price)
