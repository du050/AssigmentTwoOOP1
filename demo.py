print("       Rental System        ")
print("----------------------------")
print("Car Options: Compact/Sedan/SUV/Luxury")
# Rental rates per day (base rate)
vehicle_rates = {
    "Compact": 25,
    "Sedan": 35,
    "SUV": 50,
    "Luxury": 60
}

# Discounts based on rental duration
duration_discounts = {
    1: 0,     # 1 day: no discount
    2: 0.04,  # 2-3 days: 4% discount
    4: 0.10,  # 4-7 days: 10% discount
    8: 0.20   # 8 or more days: 20% discount
}

print("Options: (1) GPS Navigation: $5",
    "(2) Mobile Wi-Fi: $8",
    "(3) Child Seat: $2",
    "(4) Toll Pass: $4.5",
    "(5) Roadside Assistance Plus: $5")
# Additional features and their daily rates
additional_features = {
    "1": 5,
    "2": 8,
    "3": 2,
    "4": 4.50,
    "5": 5
}

vehicle_type = input("Enter vehicle type (Compact, Sedan, SUV, Luxury): ")
print()
rental_duration = int(input("Enter rental duration in days: "))
selected_features = input("Enter additional features in numbers (comma-separated): ").split(",")

initial_cost = vehicle_rates.get(vehicle_type, 0) * rental_duration
discount = duration_discounts.get(rental_duration, 0)
discount_cost = initial_cost * (1 - discount)
feature_cost = sum(additional_features.get(feature.strip(), 0) for feature in selected_features)
total_cost = discount_cost + feature_cost

print(f"The total cost is: {total_cost}")