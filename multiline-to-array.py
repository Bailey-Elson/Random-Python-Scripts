multiline = """
"""

lines = multiline.strip().split('\n')

print(len(lines))

for line in lines:
    print("'"+line+"',")

print("\n\n\n")

for line in lines:
    print(line+",")
