# Define your multiline variables
list1_text = """

"""

list2_text = """

"""

# Convert to sets of unique values (normalize: lowercase + strip whitespace)
set1 = set(line.strip().lower() for line in list1_text.splitlines() if line.strip())
set2 = set(line.strip().lower() for line in list2_text.splitlines() if line.strip())

# Compare
only_in_first = sorted(set1 - set2)
only_in_second = sorted(set2 - set1)

# Results
print(f"Unique values in first list: {len(set1)}")
print(f"Unique values in second list: {len(set2)}\n")

print(f"Values in first but not in second {len(only_in_first)}:")
for val in only_in_first:
    print(val)

print(f"\nNew values in second but not in first {len(only_in_second)}:")
for val in only_in_second:
    print(val)
