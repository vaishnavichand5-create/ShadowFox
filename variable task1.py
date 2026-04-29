pi = 22/7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

print("\n----------------------\n")

try:
    exec("for = 4")
except SyntaxError as e:
    print("Error when using 'for' as variable:", e)

print("\n----------------------\n")

P = 1000
R = 5
T = 3

SI = (P * R * T) / 100
print("Simple Interest:", SI)