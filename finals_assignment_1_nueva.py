# Ruzzel Nueva
# List Operations
# Creating a basic list of items
items = ["pencil", "notebook", "eraser"]

# Add 1 new item
items.append("bag")

# Remove 1 item
items.remove("notebook")

# Sort the list
items.sort()

print("List Results")
print(items)


# Tuple Operations
# Creating a tuple (fixed data)
my_tuple = (20, 30, 40)

print("\nTuple Modification")
print("Trying to change the first element to 10...")

try:
    my_tuple[0] = 10
except TypeError:
    print("Result: An error occurred! You cannot change a tuple.")

# EXPLANATION:
# In Python, tuples are immutable. This means that once they are 
# created, you cannot change, add, or remove their elements.


# Set Operations
# Creating a set of numbers
my_set = {1, 2, 3, 4, 5}

# 1. Add a value
my_set.add(6)

# 2. Remove a value
my_set.remove(2)

# 3. Print the updated set
print("\nSet Results")
print(my_set)


# Dictionary Operations
# Creating a dictionary for a student profile
student = {
    "name": "Ruzzel",
    "age": 19,
    "course": "BSIT"
}

# 1. Add a new key "grade"
student["grade"] = "1.25"

# 2. Update your "age"
student["age"] = 20

# 3. Print all keys
print("\nDictionary Results")
print("These are the keys in the dictionary:")
print(student.keys())
