# File Handling in Python

# 1. Create and Write to a File
with open("sample.txt", "w") as file:
    file.write("Hello, this is a file handling demo in Python.\n")
    file.write("We are writing some sample text.\n")

print("File written successfully.")

# 2. Read the File
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nReading File Content:")
    print(content)

# 3. Append to the File
with open("sample.txt", "a") as file:
    file.write("This line is added using append mode.\n")

print("\nLine appended successfully.")

# 4. Read Line by Line
with open("sample.txt", "r") as file:
    print("\nReading file line by line:")
    for line in file:
        print(line.strip())
