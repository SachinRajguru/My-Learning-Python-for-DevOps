# 02-main-construct.py
# ---------------------------------
# Topic: Using the main() construct in Python
# DevOps Use-Case:
#   - Ensures code runs only when executed directly (not when imported as a module).
#   - Useful for building modular automation scripts.

def main():
    # Prompt user for folder paths separated by spaces
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()

    # Print the full list
    print("Converted List of Folder Paths:", folder_paths)

    # Uncomment this block if you want to print each folder path separately
    # for folder_path in folder_paths:
    #     print(folder_path)


# The main() construct
if __name__ == "__main__":
    main()