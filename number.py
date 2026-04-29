# 1. Format function
def format_example(num, char):
    return "{} {}".format(num, char)

print("Formatted Output:", format_example(145, 'o'))


# 2. Pond Area + Water Calculation
radius = 84
pi = 3.14

area = pi * radius * radius
water_per_sq_meter = 1.4
total_water = area * water_per_sq_meter

print("Area of pond:", area)
print("Total water in pond:", int(total_water))


# 3. Speed Calculation
distance = 490
time_minutes = 7

time_seconds = time_minutes * 60
speed = distance / time_seconds

print("Speed (m/s):", int(speed))