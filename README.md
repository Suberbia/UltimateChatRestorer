# UltimateChatRestorer

**UltimateChatRestorer** is a Python project that provides a script to convert Telegram chat exports (in JSON format) into a text file that resembles WhatsApp’s chat format. You can then import the converted chat back into Telegram.


## Prerequisites

### 1. Install Python

You’ll need to have Python installed on your computer. Python is available for free and can be downloaded from [python.org](https://www.python.org/downloads/).

- **Windows**: 
  1. Download and install Python from the [official site](https://www.python.org/downloads/).
  2. During installation, make sure to check the box that says "Add Python to PATH."
- **Mac**:
  1. Python 3.x is usually pre-installed on MacOS. You can verify it by opening Terminal and typing `python3 --version`.
  2. If not installed, download it from [python.org](https://www.python.org/downloads/mac-osx/).
- **Linux**:
  1. Most Linux distributions come with Python pre-installed. You can check by running `python3 --version` in your terminal.

### 2. Prepare Your Telegram Export

Export your Telegram chat as a JSON file by following Telegram’s export instructions. Name the file `result.json`.

## Step-by-Step Guide

### 1. Download the Script

Save the Python script (`The Ultimate Chat restorer.py`) to a directory on your computer where your `result.json` file is also located.

### 2. Run the Script

#### On Windows:

1. Open the folder where you saved the script and `result.json`.
2. Hold `Shift` and right-click in the folder, then select "Open PowerShell window here" or "Open Command window here."
3. Type the following command and press Enter:

   ```bash
   python "The Ultimate Chat restorer.py"
   ```

#### On Mac:

1. Open Terminal (you can find it in Applications > Utilities).
2. Navigate to the folder where your script and `result.json` are stored using the `cd` command. For example:

   ```bash
   cd /path/to/your/folder
   ```

3. Run the script with:

   ```bash
   python3 "The Ultimate Chat restorer.py"
   ```

#### On Linux:

1. Open your terminal.
2. Navigate to the directory where the script and `result.json` are located:

   ```bash
   cd /path/to/your/folder
   ```

3. Run the script:

   ```bash
   python3 "The Ultimate Chat restorer.py"
   ```

### 3. Check the Output

After running the script, you’ll find a new file named `_chat.txt` in the same folder. This file contains your converted Telegram chat in WhatsApp format.

## Importing the `_chat.txt` into Telegram

1. **Right-click on `_chat.txt`** and choose "Add to archive" (Windows) or "Compress" (Mac/Linux).
2. **Name the archive**: Set the file name as `Whatsapp Chat - xxxx.zip`, replacing `xxxx` with the name of the user whose chat you’re importing.
3. **Transfer the file to your phone**: Use a USB cable, email, or any other method to move the `Whatsapp Chat - xxxx.zip` file to your mobile device.
4. **Open the file on your phone**: Navigate to where you saved the file, and tap on it. Choose the "Share" option.
5. **Share to Telegram**: In the sharing menu, select the Telegram app.
6. **Select the contact**: Choose the contact you want to import the chat to, and send the file.

Telegram will automatically recognize the file as a chat history and import it accordingly.

## Troubleshooting

If you encounter any issues, please make sure:
- You have Python installed and properly configured.
- Your Telegram export file is correctly named `result.json`.
- The script and the JSON file are in the same directory.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.
