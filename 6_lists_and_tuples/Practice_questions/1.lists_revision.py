'''Quick Revision of Lists and its methods with examples.'''

# Revision(basic_to_adv.):


# Create a list with integers and print its elements.
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Append a new element to the list.
my_list.append(6)

# Access and print a specific element from the list.
print(my_list[2])

# Remove a specific element from the list.
my_list.remove(3)

# Check if a given element exists in the list.
if 4 in my_list:
    print("Element 4 exists in the list.")

# Concatenate two lists and print the result.
new_list = my_list + [7, 8, 9]
print(new_list)

# Create a nested list and perform indexing.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])

# Sort a list of numbers in ascending and descending order.
my_list.sort()          # Ascending order
my_list.sort(reverse=True)  # Descending order

# Remove duplicates from a list.
my_list = list(set(my_list))

#--------------------------------------------------------------------------------------------#
