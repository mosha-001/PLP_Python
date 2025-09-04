# File Read & Write Challenge

# Read from input file
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (e.g., uppercase it)
modified_content = content.upper()

# Write to new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ Modified content has been written to output.txt")

# Error Handling Lab

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n📄 File Content:\n")
        print(content)
except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
