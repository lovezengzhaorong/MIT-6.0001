annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

def calculate_months_to_save(annual_salary, portion_saved, total_cost):
    portion_down_payment = 0.25  # 25% down payment
    current_savings = 0
    r = 0.04  # Annual return on investment

    monthly_salary = annual_salary / 12
    down_payment_needed = portion_down_payment * total_cost

    months = 0
    while current_savings < down_payment_needed:
        current_savings += current_savings * (r / 12)  # Investment return
        current_savings += monthly_salary * portion_saved
        months += 1

    return months

# Calculate and print result
months_needed = calculate_months_to_save(annual_salary, portion_saved, total_cost)
print("Number of months: ", months_needed)
