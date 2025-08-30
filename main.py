import keyboard as k
import pyautogui
import time
import os

def web():
    print("1. Chrome\n2. Brave\n3. Edge\n4. Opera\n5. Firefox")
    Option = k.read_key(suppress=True)
    while Option not in ['1','2','3','4','5']:
        os.system("cls" if os.name == "nt" else "clear")
        print("The browser is not supported, Try among the given...")
        print("1. Chrome\n2. Brave\n3. Edge\n4. Opera\n5. Firefox")
        Option = k.read_key(suppress=True)
    if Option == 1:
        return "chrome"
    elif Option == 2:
        return "brave"
    elif Option == 3:
        return "msedge"
    elif Option == 4:
        return "opera"
    elif Option == 5:
        return "firefox"

os.system("cls" if os.name == "nt" else "clear")
print("Starting...")
time.sleep(0.75)
print("Only for educational purposes...")
time.sleep(0.75)
os.system("cls" if os.name == "nt" else "clear")
print("The code is shit but it works and is very basic...so yeah")
time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")

print("  /$$$$$$                                            /$$             ")
time.sleep(0.1)
print(" /$$__  $$                                          | $$             ")
time.sleep(0.1)
print("| $$  \ $$  /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$$ /$$$$$$   /$$$$$$$")
time.sleep(0.1)
print("| $$$$$$$$ /$$_____/ /$$__  $$|  $$ /$$/ /$$_____/|_  $$_/  /$$_____/")
time.sleep(0.1)
print("| $$__  $$|  $$$$$$ | $$  \ $$ \  $$$$/ | $$        | $$   |  $$$$$$ ")
time.sleep(0.1)
print("| $$  | $$ \____  $$| $$  | $$  >$$  $$ | $$        | $$ /$$\____  $$")
time.sleep(0.1)
print("| $$  | $$ /$$$$$$$/| $$$$$$$/ /$$/\  $$|  $$$$$$$  |  $$$$//$$$$$$$/")
time.sleep(0.1)
print("|__/  |__/|_______/ | $$____/ |__/  \__/ \_______/   \___/ |_______/ ")
time.sleep(0.1)
print("                    | $$                                             ")
time.sleep(0.1)
print("                    | $$                                             ")
time.sleep(0.1)
print("                    |__/                                             ")
time.sleep(0.1)
print("\t\t\tBasic Whatsapp spammer")
time.sleep(2)

num = input("Enter the number: ")
os.system("cls" if os.name == "nt" else "clear")
cc = input("Enter country code: ")
os.system("cls" if os.name == "nt" else "clear")
num = cc+num
Web = web()
os.system("cls" if os.name == "nt" else "clear")
time.sleep(0.5)
msg = input("Enter your message: ")
os.system("cls" if os.name == "nt" else "clear")
loop = int(input("Enter loop number: "))
os.system("cls" if os.name == "nt" else "clear")

text = "https://web.whatsapp.com/send?phone=+"
text = text + num
text = text + "&text="
text = text + msg
print("Daemon is",msg,"to +",num,loop,"times")

        
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Make sure your Whatsapp web is logged in and then press 'enter' to start the daemon...")
    time.sleep(1)
    if k.read_key() == "enter":
        for i in range(loop):
            k.press_and_release('win+r')
            time.sleep(1)
            k.write(Web)
            time.sleep(1)
            k.press_and_release('enter')
            time.sleep(1)
            k.write(text)
            time.sleep(1)
            k.press_and_release('enter')
            time.sleep(5)
            k.press_and_release('enter')
            time.sleep(1)
            print("daemon sent ",i+1," times")
            time.sleep(2)
            k.press_and_release('alt+f4')
            os.system("cls" if os.name == "nt" else "clear")
        print("Task completed, press 'enter' to exit...")
        exit_key = k.read_key()
        if exit_key == "enter":
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            continue   
    else:
        print("Another key was pressed, press again to exit...")
        time.sleep(1)
        if k.read_key() != "enter":
            os.system("cls" if os.name == "nt" else "clear")
            print("Exiting...")
            break