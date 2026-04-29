# Predefined city-country mapping
india = ["Mumbai", "Delhi", "Chennai", "Kolkata"]
usa = ["New York", "Los Angeles", "Chicago"]
australia = ["Sydney", "Melbourne"]
uae = ["Dubai", "Abu Dhabi"]

# User input
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check condition
if city1 in india and city2 in india:
    print("Both cities are in India")

elif city1 in usa and city2 in usa:
    print("Both cities are in USA")

elif city1 in australia and city2 in australia:
    print("Both cities are in Australia")

elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")

else:
    print("They don't belong to the same country")