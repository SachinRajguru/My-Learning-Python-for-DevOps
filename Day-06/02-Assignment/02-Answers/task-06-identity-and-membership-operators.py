# Task 6: Identity and Membership Operators

# Step 1: Create a list
my_list = [1, 2, 3, 4, 5]

# Identity Operators
# 'is' checks if two variables point to the same object in memory
a = my_list           # 'a' references the same list object as 'my_list'
b = [1, 2, 3, 4, 5]  # 'b' is a new list object with the same values

is_same_object = a is my_list       # True, same object
is_not_same_object = b is not my_list  # True, different objects

# Membership Operators
# 'in' checks if an element exists in a sequence
# 'not in' checks if an element does NOT exist in a sequence
element_in_list = 3 in my_list       # True, 3 is in the list
element_not_in_list = 6 not in my_list  # True, 6 is not in the list

# Step 2: Print results
print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)