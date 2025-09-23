# 01-convert-string-to-list.py
# ---------------------------------
# Topic: Convert String to List in Python
# DevOps Use-Case:
#   - Parsing multiple folder paths or server names given as input.
#   - Useful for automation scripts that take space-separated or comma-separated values.

# Prompt user to enter folder paths separated by spaces
folder_paths = input("Enter a list of folder paths separated by spaces: ").split()

# Print the converted list
print("Converted List of Folder Paths:", folder_paths)

# Example:
# Input:  /etc /var/log /usr/local/bin
# Output: ['etc', '/var/log', '/usr/local/bin']