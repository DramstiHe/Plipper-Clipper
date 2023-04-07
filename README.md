<div align="center">
  
  # Plipper 👀💰
  
  ### *The Crypto Clipboard Guard*
  
</div>

---

## 🔍 Overview

Plipper is a simple yet powerful Python script that automatically replaces Bitcoin and Ethereum addresses in your clipboard with pre-defined addresses of your choice. This is useful for preventing accidental copying and pasting of incorrect addresses, or for quickly switching between multiple addresses when dealing with cryptocurrencies.

---

## 🛠️ Installation

1. **Install Python:** Plipper requires Python 3.9 or later to run. You can download the latest version of Python from the official website: https://www.python.org/downloads/

2. **Download Plipper:** Clone the repository or download the `plipper.pyw` file from the [latest release](https://github.com/myusername/plipper/releases/latest).

3. **Run Plipper:** Run `plipper.pyw` from the command line or by double-clicking on the file. Plipper will run in the background and silently replace any Bitcoin or Ethereum addresses in the clipboard.

---

## ⚙️ Configuration

You can customize the Bitcoin and Ethereum addresses by editing the `btc_addresses` and `eth_addresses` variables in the `plipper.pyw` file. The `btc_addresses` variable should be a dictionary mapping address prefixes (e.g., "1", "bc1", "3") to corresponding addresses. The `eth_addresses` variable should be a list of Ethereum addresses.

---

## 📝 Usage

Plipper is designed to run in the background and silently monitor your clipboard for Bitcoin or Ethereum addresses. If it detects a Bitcoin or Ethereum address in the clipboard, it will replace it with a pre-defined address of your choice. To use Plipper:

1. Copy a Bitcoin or Ethereum address to your clipboard.
2. Plipper will automatically detect the address and replace it with the corresponding address from your configuration file.
3. Paste the new address wherever you need to use it.

---

## 📜 License

Plipper is licensed under the [MIT License](https://github.com/myusername/plipper/blob/main/LICENSE).

---

## 📧 Contact

For bug reports, feature requests, or other inquiries, please contact the author
