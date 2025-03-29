arr = [1, 2, 3, 4, 5]
size = len(arr)
value = 77 # Define value to insert at the end
new_arr = [0] * (size + 1)
# Copy all elements from the original array
for i in range(size):
 new_arr[i] = arr[i]
new_arr[size] = value
print("Updated Array (After Insertion at End):", new_arr)