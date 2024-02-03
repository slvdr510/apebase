import os

#             ╔█████████  ██╗  ██╗       ██╗ ██████╗   ███████╗   █████████    ██   ███████ 
#             ██══════╗   ██║   ██╗     ██╗  ██    ██║  ██╔══██║  ██         █ ██  ██     ██
#              ████████   ██║    ██╗   ██╗   ██    ██║  ██████╝   █████████    ██  ██     ██
#              ╚══════██  ██║     ██╗ ██╗    ██    ██║  ██╔══██╗         ██    ██  ██     ██
#             █████████╝  ███████╗  ███╝     ██████╝    ██║  ██║  ██     ██    ██  ██     ██
#             ╚═══════╝   ╚══════╝  ╚═╝      ╚════╝     ╚═╝  ╚═╝    █████      ██   ███████ 

# Get the folder path where the Python script is located
script_folder = os.path.dirname(os.path.abspath(__file__))

# Display the script folder path
print(f"Script Folder Path: {script_folder}")

# Navigate to the script folder
os.chdir(script_folder)

# Rename files without an extension to have a ".jpg" extension
for filename in os.listdir(script_folder):
    if '.' not in filename:  # Files without an extension
        new_filename = os.path.join(script_folder, f'{filename}.jpg')
        os.rename(os.path.join(script_folder, filename), new_filename)

print("Files renamed successfully.")

