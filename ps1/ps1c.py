def calculate_months_to_save(annual_salary, portion_saved):
    total_cost = 1000000  # Cost of the house
    portion_down_payment = 0.25  # 25% down payment
    current_savings = 0
    r = 0.04  # Annual return on investment

    monthly_salary = annual_salary / 12
    down_payment_needed = portion_down_payment * total_cost

    months = 0
    while months < 36:
        if months > 0 and months % 6 == 0:
            annual_salary *= 1.07  # Semi-annual raise
            monthly_salary = annual_salary / 12

        current_savings += current_savings * (r / 12)  # Investment return
        current_savings += monthly_salary * portion_saved
        months += 1

    return current_savings - down_payment_needed

def find_savings_rate(annual_salary):
    epsilon = 100  # Tolerance for down payment
    low = 0
    high = 10000  # Representing 100.00%
    steps = 0

    while low <= high:
        steps += 1
        portion_saved = (low + high) // 2 / 10000  # Convert to decimal percentage
        savings_diff = calculate_months_to_save(annual_salary, portion_saved)

        if abs(savings_diff) <= epsilon:
            return portion_saved, steps
        elif savings_diff < 0:
            low = (low + high) // 2 + 1
        else:
            high = (low + high) // 2 - 1

    return None, steps

# Main program
annual_salary = float(input("Enter your starting annual salary: "))
best_savings_rate, steps = find_savings_rate(annual_salary)

if best_savings_rate is None:
    print("It is not possible to save for the down payment in 36 months.")
else:
    print("Best savings rate:", round(best_savings_rate, 4))
    print("Steps in bisection search:", steps)
