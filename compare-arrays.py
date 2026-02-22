def print_unique_from_first(arr1, arr2):
    unique = [num for num in arr1 if num not in arr2]
    print("Numbers only in the first array:", unique)

# Example usage
array1 = []
array2 = []

print_unique_from_first(array1, array2)
