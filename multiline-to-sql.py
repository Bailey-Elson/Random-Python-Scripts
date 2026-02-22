ids = """

"""

prices = """

"""



arr1 = [line.strip() for line in ids.splitlines() if line.strip()]
arr2 = [line.strip() for line in prices.splitlines() if line.strip()]

for id in arr1:
    print(id+',')

# Check if arrays are the same length
if len(arr1) == len(arr2):
    # Loop through both arrays together
    for a, b in zip(arr1, arr2):
        print(f"update table_name set col_name = {b} where col_name = {a};\n")
else:
    print("Arrays are not the same length.")
