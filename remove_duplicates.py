# Author : Lalatendu Swain
# Version: 1
# Read the content from the provided file
file_name = "YourFileName.txt"
with open(file_name, "r") as file:
    commands = file.readlines()

# Remove duplicate commands while preserving order
unique_commands = []
seen_commands = set()
for command in commands:
    if command not in seen_commands:
        unique_commands.append(command)
        seen_commands.add(command)

# Write the unique commands back to the file
with open(file_name, "w") as file:
    file.writelines(unique_commands)
