#program to print duplicate values from list
list=[1,2,3,2,3,4,5,6,6,7,3,8,9,6,2] #list of integers
unique_values=[]
duplicate_values=[]

for i in list:
    if i not in unique_values:
        unique_values.append(i)
    elif i not in duplicate_values:
        duplicate_values.append(i)

print("list of integers:",list)
print("unique values in the list: ")
print(unique_values)
print("duplicates values in the list: ")
print(duplicate_values)