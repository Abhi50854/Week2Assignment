my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("The list is:", my_list)  # Output the list

my_list[1] = 15  # Change the second element to 15
print("The updated list is:", my_list)  # Output the updated list

my_list.append(50)  # Add another element to the list
my_list.append(60)  # Add another element to the list
my_list.append(70)  # Add another element to the list
print("The final list is:", my_list)  # Output the final list

my_list.pop()
print("After popping the last element, the list is:", my_list)  # Output after popping last element

my_list.sort()  # Sort the list
print("The sorted list is:", my_list)  # Output the sorted list

index_of_30 = my_list.index(30)  # Find the index of 30
print("The index of 30 is:", index_of_30)  # Output the index

