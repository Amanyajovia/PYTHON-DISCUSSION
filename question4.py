#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.


# Original list
list_of_my_favourite_foods = ['chicken', 'chips', 'matooke', 'beef', 'pork']

# Adding two new items
list_of_my_favourite_foods.append('pizza')
list_of_my_favourite_foods.append('fish')

# Removing one item
list_of_my_favourite_foods.remove('beef')

# Printing the updated list
print(list_of_my_favourite_foods)



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.

# numbers = [2,5,8,10,3,6]

# #first element
# print(numbers[0])

# #last element

# print(numbers[5])


# # Print the list in reverse order.

# numbers = [2, 5, 8, 10, 3, 6]
# print(numbers[::-1])

# # Calculate and print the sum of all the elements in the list.

# total_sum = sum(numbers)
# print(f"Sum of all elements is: {total_sum}")