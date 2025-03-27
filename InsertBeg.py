#this is an program in which we insert values from the begining of the array
arr = [1, 2, 3, 4, 5]
size = len(arr)
value = 99  
new_arr = [0] * (size + 1)
for i in range(size):
    new_arr[i + 1] = arr[i]
 #  Insert new value at index 0
new_arr[0] = value
print("Updated Array (After Insertion at Beginning):", new_arr)
