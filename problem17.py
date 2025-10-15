from datetime import datetime, timedelta

def estimate_delivery(distance_km, time_of_day, weather, restaurant_prep_time):
    
    
    #  Set base delivery speed
    base_speed = 30  
    
    #  Check if it's rush hour and adjust speed
    # Rush hours: 12-2 PM  and 7-9 PM 
    is_rush_hour = (12 <= time_of_day < 14) or (19 <= time_of_day < 21)
    
    if is_rush_hour:
        speed = base_speed - 10  # Reduce speed by 10 km/hour
        print(f" Rush hour detected! Speed reduced to {speed} km/hour")
    else:
        speed = base_speed
        print(f" Normal traffic. Speed: {speed} km/hour")
    
    #  Check weather conditions and adjust speed further
    if weather.lower() in ["rain", "snow"]:
        speed = speed - 5  # Reduce speed by 5 km/hour
        print(f" Bad weather ({weather})! Speed reduced to {speed} km/hour")
    
    #  Calculate travel time
    
    travel_time_hours = distance_km / speed  # Result in hours
    travel_time_minutes = travel_time_hours * 60  # Convert to minutes
    
    print(f"\n Distance: {distance_km} km")
    print(f" Travel time: {travel_time_minutes:.1f} minutes")
    
    #  Add restaurant preparation time
    print(f" Restaurant prep time: {restaurant_prep_time} minutes")
    total_time_minutes = travel_time_minutes + restaurant_prep_time
    
    print(f"\nTotal estimated time: {total_time_minutes:.1f} minutes")
    
    #  Calculate expected delivery time
    current_time = datetime.now()  
    delivery_time = current_time + timedelta(minutes=total_time_minutes)
    
    # Format the time nicely (e.g., "08:30 PM")
    delivery_time_formatted = delivery_time.strftime("%I:%M %p")
    
    print(f" Expected delivery: {delivery_time_formatted}")
    
    # Return results as a dictionary
    return {
        "estimated_minutes": round(total_time_minutes, 1),
        "expected_delivery_time": delivery_time_formatted,
        "current_time": current_time.strftime("%I:%M %p"),
        "delivery_speed_used": speed
    }


# Example Usage
print("=" * 50)
print(" FOOD DELIVERY TIME ESTIMATOR")
print("=" * 50)

#  Normal conditions
print("\n Order 1: Normal Conditions")
print("-" * 50)
result1 = estimate_delivery(
    distance_km=5,
    time_of_day=15,  # 3 PM (not rush hour)
    weather="clear",
    restaurant_prep_time=20
)

#  Rush hour
print("\n\n Order 2: Rush Hour")
print("-" * 50)
result2 = estimate_delivery(
    distance_km=8,
    time_of_day=19,  # 7 PM (rush hour)
    weather="clear",
    restaurant_prep_time=30
)

#  Rush hour + bad weather
print("\n\n Order 3: Rush Hour + Rain")
print("-" * 50)
result3 = estimate_delivery(
    distance_km=6,
    time_of_day=13,  # 1 PM (rush hour)
    weather="rain",
    restaurant_prep_time=25
)

# Display summary
print("\n" + "=" * 50)
print(" SUMMARY")
print("=" * 50)
print(f"Order 1: {result1['estimated_minutes']} minutes → {result1['expected_delivery_time']}")
print(f"Order 2: {result2['estimated_minutes']} minutes → {result2['expected_delivery_time']}")
print(f"Order 3: {result3['estimated_minutes']} minutes → {result3['expected_delivery_time']}")