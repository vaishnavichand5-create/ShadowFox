# ------------------ PART 1 ------------------

# List of friends
friends = ["Amit", "Neha", "Rohit", "Sneha", "Karan"]

# List of tuples (name, length)
name_length = []

for name in friends:
    name_length.append((name, len(name)))

print("1. List of tuples (Name, Length):")
print(name_length)


# ------------------ PART 2 ------------------

# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\n2. Total Expenses:")
print("Your total:", your_total)
print("Partner total:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more money")
elif partner_total > your_total:
    print("Your partner spent more money")
else:
    print("Both spent equal amount")

# Find category with maximum difference
max_diff = 0
max_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    
    if diff > max_diff:
        max_diff = diff
        max_category = category

print("\nCategory with highest difference:")
print(max_category, "-> Difference:", max_diff)