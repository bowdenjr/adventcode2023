import os

base_directory = 'D:/repos/adventcode2023'

# Create 31 folders with leading zeros
# for i in range(32):
#     folder_name = f"day_{i:02}" 
#     folder_path = os.path.join(base_directory, folder_name)
#     os.makedirs(folder_path)
#     print(f"Folder '{folder_name}' created at '{folder_path}'")


# Iterate through existing folders and add .gitkeep file
for i in range(32):
    folder_name = f"day_{i:02}"  # Folder names with leading zeros
    folder_path = os.path.join(base_directory, folder_name)
    
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Create .gitkeep file
        gitkeep_path = os.path.join(folder_path, '.gitkeep')
        with open(gitkeep_path, 'w') as gitkeep_file:
            pass  # Creates an empty .gitkeep file
        print(f".gitkeep file added to '{folder_name}' folder")
    else:
        print(f"'{folder_name}' folder does not exist")
