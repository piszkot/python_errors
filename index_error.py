# Common ways to get an IndexError in Python

my_list = [1, 2, 3]

print()
# --- List ---
try:
    print(my_list[5])
except IndexError as e:
    print(f"{'List index out of range:':<40}{e}")

try:
    print(my_list[-10])
except IndexError as e:
    print(f"{'Negative index out of range:':<40}{e}")

# --- Empty list ---
empty = []
try:
    print(empty[0])
except IndexError as e:
    print(f"{'Empty list:':<40}{e}")

# --- Off by one (common mistake) ---
print()
for i in range(len(my_list) + 1):
    try:
        print(my_list[i])
    except IndexError as e:
        print(f"\n{'Off by one at index ' + str(i) + ':':<40}{e}\n")

# --- String ---
text = "hello"
try:
    print(text[10])
except IndexError as e:
    print(f"{'String index out of range:':<40}{e}")

# --- Tuple ---
t = (10, 20, 30)
try:
    print(t[5])
except IndexError as e:
    print(f"{'Tuple index out of range:':<40}{e}")

# --- Nested list ---
matrix = [[1, 2], [3, 4]]
try:
    print(matrix[0][5])
except IndexError as e:
    print(f"{'Nested list index out of range:':<40}{e}")
print()
