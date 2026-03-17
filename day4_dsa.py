# -------------------------------
# ARRAYS USING LIST (Most Common)
# -------------------------------
"""
print("----- LIST OPERATIONS -----")

# Create array
arr = [10, 20, 30, 40, 50]
print("Original array:", arr)

# Access elements
print("First element:", arr[0])
print("Third element:", arr[2])

# Modify element
arr[1] = 25
print("After modification:", arr)

# Add elements
arr.append(60)
print("After append:", arr)

arr.insert(2, 15)
print("After insert:", arr)

# Remove elements
arr.remove(30)
print("After remove:", arr)

popped = arr.pop()
print("Popped element:", popped)
print("After pop:", arr)

# Length of array
print("Length:", len(arr))

# Loop through array
print("Elements in array:")
for i in arr:
    print(i)

# Searching element
if 40 in arr:
    print("40 is present in array")

# Sorting
arr.sort()
print("Sorted array:", arr)

# Reverse
arr.reverse()
print("Reversed array:", arr)


# -------------------------------
# ARRAYS USING ARRAY MODULE
# -------------------------------

print("\n----- ARRAY MODULE OPERATIONS -----")

import array

# Create array (integer type)
arr2 = array.array('i', [1, 2, 3, 4, 5])
print("Original array:", arr2)

# Access
print("First element:", arr2[0])

# Append
arr2.append(6)
print("After append:", arr2)

# Insert
arr2.insert(1, 10)
print("After insert:", arr2)

# Remove
arr2.remove(3)
print("After remove:", arr2)

# Pop
arr2.pop()
print("After pop:", arr2)

# Index
print("Index of 4:", arr2.index(4))

# Reverse
arr2.reverse()
print("Reversed array:", arr2)

# Loop
print("Elements in array:")
for i in arr2:
    print(i)


"""
"""
sum of numbers in array

def count_sum(arr):
    total=0
    for num in arr:
        total+=num
    return total
arr = [ 1,2,3,4,5]
print("sum",count_sum(arr))

"""
#2.counting numbers in array
"""
def count_num(arr):
    count=0
    for i in arr:
        count +=1
    return count
arr=[10,20,30,40]
print("total numbers:",count_num(arr))


"""
#3.counting the even digits in arr
"""

def count_even_digits(arr):
    count = 0
    for i in arr:
        if  i % 2==0:
            count +=1
    return count
arr=[10,25,30,35,40]
print("even number count are:",count_even_digits(arr))

"""

#4.finding maximum value in array

def max_value(arr):
    max_value=arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value
arr=list(map(int,input("enter the values:").split()))
print("largest value:",max_value(arr))
