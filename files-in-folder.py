import os

folder_path = r"C:\Users\baile\OneDrive\Documents\Random-Python-Scripts"

for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)
    if os.path.isfile(full_path):
        print(filename)
