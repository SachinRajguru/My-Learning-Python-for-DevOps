# 03-list-files-in-folders.py
# ----------------------------------------------------
# This script takes one or more folder paths as input
# and lists all the files present in each folder.
#
# Why useful for DevOps?
# - You can quickly check what files exist in config, log, or deployment folders.
# - Helps automate validation (e.g., ensure required files are present after deployment).
# ----------------------------------------------------

import os   # Importing 'os' module to interact with the operating system (folders & files)

def list_files_in_folder(folder_path):
    """
    Function to list files in a given folder.
    Returns:
      - files (list) if successful
      - error message (str) if folder not found or no permission
    """
    try:
        files = os.listdir(folder_path)   # Get list of files in the folder
        return files, None                # No error, return files
    except FileNotFoundError:
        return None, "Folder not found"   # Handle case where folder does not exist
    except PermissionError:
        return None, "Permission denied"  # Handle case where folder is not accessible

def main():
    # Step 1: Take user input (multiple folder paths separated by spaces)
    # Example input: /etc /var/log /home/user/Documents
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    # Step 2: Loop through each folder path
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        
        if files:   # If files are successfully retrieved
            print(f"\nFiles in {folder_path}:")
            # Loop through each file and print it
            for file in files:
                print(f"  - {file}")
        else:       # If there was an error (folder missing or no permission)
            print(f"\nError in {folder_path}: {error_message}")

# Step 3: Run the main function only when script is executed directly
if __name__ == "__main__":
    main()