arr = [1, 2, 3, 4, 5]
size = len(arr) 
pos = 2 # Index or position where we insert
value = 10 
# Check for valid position
if pos < 0 or pos > size:
 print("Invalid position!")
else:
 new_arr = [0] * (size + 1)
 # Copy and shift elements
 for i in range(size + 1):
    if i < pos:
        new_arr[i] = arr[i] # Copy before insertion position
    elif i == pos:
        new_arr[i] = value # Insert new value
    else:
         new_arr[i] = arr[i - 1] # Shift right
 print("Updated Array:", new_arr)