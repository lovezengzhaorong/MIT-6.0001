def calculate_months_to_save(annual_salary, portion_saved, total_cost, semi_annual_raise):
    portion_down_payment = 0.25  # 25% down payment
    current_savings = 0
    r = 0.04  # Annual return on investment

    monthly_salary = annual_salary / 12
    down_payment_needed = portion_down_payment * total_cost

    months = 0
    while current_savings < down_payment_needed:
        if months > 0 and months % 6 == 0:
            annual_salary *= (1 + semi_annual_raise)  # Apply semi-annual raise
            monthly_salary = annual_salary / 12

        current_savings += current_savings * (r / 12)  # Investment return
        current_savings += monthly_salary * portion_saved
        months += 1

    return months

# Get user inputs
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the portion of your salary to be saved, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual salary raise, as a decimal: "))

# Calculate and print result
months_needed = calculate_months_to_save(annual_salary, portion_saved, total_cost, semi_annual_raise)
print("Number of months:", months_needed)
