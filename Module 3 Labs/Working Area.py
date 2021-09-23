my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list_without_duplicates = []
for number in my_list:  # Browse all numbers from the source list.
	if number not in list_without_duplicates:  # If the number doesn't appear within the new list...
		list_without_duplicates.append(number)  # ...append it here.
my_list = list_without_duplicates[:]  # Make a copy of new_list.
print("The list with unique elements only:")
print(my_list)