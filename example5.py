def calculate_cab_fare(distance_km):
    if distance_km < 0:
        print("Distance cannot be negative.")
        return None

    base_price_per_km = 50
    fare = distance_km * base_price_per_km

    print(f"Distance Travelled: {distance_km} km")
    print(f"Total Fare: ₹{fare}")

    return fare


# TAKE INPUT FROM USER
distance = float(input("Enter distance in km: "))

# CALL FUNCTION
result = calculate_cab_fare(distance)

print("Returned Fare:", result)