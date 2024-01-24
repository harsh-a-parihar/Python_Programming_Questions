'''Revision of Tuples and there methods with examples.'''

# Revision(basic_to_advance):


# Create a tuple with strings and print its elements.
my_tuple = ('apple', 'banana', 'orange')
print(my_tuple)

# Try to modify an element in the tuple (explain the result).
# Tuples are immutable, so this will raise an error:
# my_tuple[0] = 'grape'

# Access and print a specific element from the tuple.
print(my_tuple[1])

# Convert a tuple to a list and append a new element.
my_list = list(my_tuple)
my_list.append('grape')

# Check if a given element exists in the tuple.
if 'banana' in my_tuple:
    print("Element 'banana' exists in the tuple.")

# Concatenate two tuples and print the result.
new_tuple = my_tuple + ('kiwi', 'melon')
print(new_tuple)

# Create a tuple with heterogeneous data types.
mixed_tuple = (1, 'apple', 3.14, True)

# Use the zip function to combine two tuples into a list of tuples.
combined_list = list(zip(my_tuple, ('kiwi', 'melon')))

# Unpack elements from a tuple into individual variables.
fruit1, fruit2, fruit3 = my_tuple

#----------------------------------------------------------------------------------------------#
