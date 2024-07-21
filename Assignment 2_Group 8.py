#Assignment 2: Best Cars Inc. Rental System Part 1 & 2
#Group 8: Grace Zilun, Maria Xavier, Armaandeep Singh

#Initiate constants
GST = 0.05
DURATION_2DAY = 2
DURATION_4DAY = 4
DURATION_8DAY = 8
DISC_ZERO = 0
DISC_4PERCENT = 0.04
DISC_10PERCENT = 0.1
DISC_20PERCENT = 0.2

#Define dictionary of vehicle types and base rate
VEHICLE_RENTAL_RATES = {
    1: ("Compact", 25.0),
    2: ("Sedan", 35.0),
    3: ("SUV", 50.0),
    4: ("Luxury", 60.0)
}

#Define dictionary of feature options and rate
ADDITIONAL_FEATURES = {
    1: ("GPS Navigation", 5.00),
    2: ("Mobile Wi-Fi", 8.00),
    3: ("Child Seat", 2.00),
    4: ("Toll Pass", 4.50),
    5: ("Roadside Assistance Plus", 5.00)
}

#Initiate global variables 
rent_another = "Y"
total_vehicles_rented = 0
amount_due_before_GST = 0

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~ Welcome to Best Cars Inc. ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while rent_another.upper() == "Y":

    total_vehicles_rented += 1 

    # Step 1. Choose the type of vehcile
    print("\nStep 1. Choose the type of vehicle you wish to rent.")

    print(f'{'Vehicle Type': <16} {'Daily Rate': >10}')
    for index, (vehicle_type, vehicle_rate) in VEHICLE_RENTAL_RATES.items():
        print(f' {index}. {vehicle_type: <16}{vehicle_rate: >7}')

    selection = int(input("Your selection: "))

    while selection not in VEHICLE_RENTAL_RATES:
        print("Error: Invalid selection. Please enter a number between 1 and 4.")
        selection = int(input("Your selection: "))
        
    vehicle_type, vehicle_rate = VEHICLE_RENTAL_RATES[selection]
    print(f'You have chosen a {vehicle_type}. The base rental rate is {vehicle_rate} per day')

    # Step 2. Ask user to input the number of days and conduct base price with discount
    print("\nStep 2. Specify the duration of this vehicle rental.")

    rental_days = int(input("Enter the number of days needed: "))

    while rental_days <= 0:
        print("Error: Value cannot be less than 1.")
        rental_days = int(input("Enter the number of days needed: "))

    if rental_days >= DURATION_8DAY:
        discount = DISC_20PERCENT
    elif rental_days >= DURATION_4DAY:
        discount = DISC_10PERCENT
    elif rental_days >= DURATION_2DAY:
        discount = DISC_4PERCENT
    else:
        discount = DISC_ZERO

    base_rental_per_day = vehicle_rate * (1 - discount)

    print(f'Discount to be applied is {discount * 100:.0f}% ')
    print(f'Your discounted rental rate is ${base_rental_per_day:.2f} per day')

    # Step 3. Let user add multiple features, when user input "0", produce the summary of rental
    print("\nStep 3. Choose your desired additional features or services.")

    print(f'{"Option":<25}{"Daily Rate":>12}')
    for index, (feature, feature_rate) in ADDITIONAL_FEATURES.items():
        print(f' {index}. {feature:<25}{feature_rate:>8.2f}')

    selected_features = []
    total_feature_price = 0

    while True:
    
        option = int(input("Enter option # or 0 to end: "))
        
        if option == 0:
            break

        if option not in ADDITIONAL_FEATURES:
            print("Error: Invalid selection. Please enter number between 1 and 5.")
            continue
        else:
            feature, feature_rate = ADDITIONAL_FEATURES[option]

        if feature in selected_features:
            print("Error: You've selected this feature. Please enter agian. ")
            continue
        else:
            selected_features.append(feature)
            total_feature_price += feature_rate

        print(f'Feature: {feature} added for {feature_rate:.2f} per day.')

        print(f'{"Option":<25}{"Daily Rate":>12}')
        for index, (feature, feature_rate) in ADDITIONAL_FEATURES.items():
            if feature in selected_features:
                print(f' {index}. {feature:<25}{feature_rate:>8.2f} ✓')
            else:
                print(f' {index}. {feature:<25}{feature_rate:>8.2f}')

    #When user enter '0', break the while loop, calculate the total price and display the summary. Prompt user for the next rent.
    total_price_per_day = base_rental_per_day + total_feature_price 

    total_price = total_price_per_day * rental_days

    amount_due_before_GST += total_price
    
    print(f'\nSuccess! Your reservation for a {rental_days} day {vehicle_type} rental is complete. The price (not including GST) is ${total_price_per_day:.2f} per day or ${total_price:.2f} for the rental')

    rent_another = input("Do you want to rent another vehicle? (Y/N): ").upper()

# When user enter "n" to end renting, calculate the GST and total amount due
total_GST = amount_due_before_GST * GST
total_amount_due = amount_due_before_GST + total_GST

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~    RENTAL BILLING SUMMARY    ~~~")
print(f'Number of vehicles rented: {total_vehicles_rented:>9} ')
print(f'Amount due before tax: {amount_due_before_GST:>13.2f}')
print(f'GST: {total_GST:>31.2f}')
print(f'Total amount due: {total_amount_due:>18.2f} ')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")