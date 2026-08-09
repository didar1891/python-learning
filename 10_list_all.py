# Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)


# Access List Items
print(fruits[0])
print(fruits[1])
print(fruits[-1])


# Change List Items
fruits[1] = "Grapes"
print(fruits)


# Change Multiple Items
fruits[1:3] = ["Banana", "Pineapple"]
print(fruits)


# Add Items - append()
fruits.append("Watermelon")
print(fruits)


# Add Items - insert()
fruits.insert(1, "Guava")
print(fruits)


# Add Another List - extend()
more_fruits = ["Papaya", "Lemon"]
fruits.extend(more_fruits)
print(fruits)


# Remove Item - remove()
fruits.remove("Lemon")
print(fruits)


# Remove Last Item - pop()
fruits.pop()
print(fruits)


# Remove Specific Item - pop(index)
fruits.pop(1)
print(fruits)


# Delete Item - del
del fruits[0]
print(fruits)


# Clear the List
fruits.clear()
print(fruits)


# Create List Again
fruits = ["Apple", "Banana", "Mango", "Orange", "Banana"]


# Loop Through a List
for fruit in fruits:
    print(fruit)


# Check if Item Exists
if "Apple" in fruits:
    print("Apple is available")


# List Length
print(len(fruits))


# Count an Item
print(fruits.count("Banana"))


# Find Item Position - index()
print(fruits.index("Mango"))


# Sort List - sort()
fruits.sort()
print(fruits)


# Reverse Sort
fruits.sort(reverse=True)
print(fruits)


# Reverse List - reverse()
fruits.reverse()
print(fruits)


# Copy List - copy()
new_fruits = fruits.copy()
print(new_fruits)


# Copy List using list()
another_fruits = list(fruits)
print(another_fruits)


# Join Two Lists
list1 = ["Apple", "Banana"]
list2 = ["Mango", "Orange"]

list3 = list1 + list2
print(list3)


# Repeat List
numbers = [1, 2, 3]
print(numbers * 2)


# List Slicing
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])
print(fruits[-3:])


# Check Item with not in
if "Pineapple" not in fruits:
    print("Pineapple is not available")