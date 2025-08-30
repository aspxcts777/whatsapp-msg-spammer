# WhatsApp Web Automation (Educational)

## 📌 Introduction
This project demonstrates how to use Python for **basic browser and keyboard automation**.  
It shows how to:
- Capture real-time keyboard input.  
- Launch different browsers.  
- Construct and open WhatsApp Web links automatically.  
- Simulate keystrokes for message automation.  

⚠️ **Disclaimer**: This project is for **educational purposes only**.  
Do not use it for spamming, harassment, or violating WhatsApp’s terms of service.

---

## 📑 Table of Contents
- [Installation](#installation)  
- [Usage](#usage)  
- [Features](#features)  
- [Dependencies](#dependencies)  
- [Examples](#examples)  
- [Troubleshooting](#troubleshooting)  
- [Contributors](#contributors)  
- [License](#license)  

---

## ⚙️ Installation
Clone the repository and install the dependencies:

```bash
git clone <your-repo-url>
cd <repo-folder>
pip install -r requirements.txt
```

---

## 🚀 Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Provide:
   - Phone number (without country code).  
   - Country code (e.g., 91 for India).  
   - Browser choice (`1`–Chrome, `2`–Brave, `3`–Edge, `4`–Opera, `5`–Firefox).  
   - Message text.  
   - Number of repetitions.  

3. Ensure you’re logged into WhatsApp Web in the selected browser.  
4. Press **Enter** to begin automation.  

---

## ✨ Features
- **Browser choice menu** (Chrome, Brave, Edge, Opera, Firefox).  
- **Real-time key capture** with `keyboard.read_key()`.  
- **ASCII art splash screen** for fun startup.  
- **Console clearing** for a cleaner experience.  
- **Simple message daemon** loop.  

---

## 📦 Dependencies
- `keyboard` – capture and simulate key presses.  
- `pyautogui` – GUI automation.  
- `time` – control execution delays.  
- `os` – clear console and run system commands.  

You can install them with:
```bash
pip install keyboard pyautogui
```

---

## 💡 Example Run
```text
Enter the number: 9876543210
Enter country code: 91
Choose browser: (press 1–5)
Enter your message: test
Enter loop number: 3
```

Output:
```
Daemon is test to +910011230012 3 times
Make sure your WhatsApp web is logged in and then press 'enter' to start the daemon...
```

---

## 🛠 Troubleshooting
- **Browser doesn’t open** → Make sure it’s installed and accessible via `win+r`.  
- **Message not sent** → Ensure you’re logged in to WhatsApp Web.  
- **Keyboard errors** → Run the script with administrator/root permissions.  

---

## 👨‍💻 Contributors
- Author: **Aspxcts**  

---

## 📜 License
This project is released under the **Modified MIT License** for educational use.


Copyright (c) 2025 **Aspxcts**


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:


1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


2. Any works created using this Software or any modified version of this Software must include attribution to the original software author(s). Attribution should include the following information:

a. The name of the software.

b. The name of the original author(s) of the software.

c. The URL or other reference to the software (Github).


**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.** 
