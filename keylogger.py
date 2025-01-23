import sys
import time

# Simulated Keylogger for Online Compiler
def keylogger():
    print("Keylogger Started. Type your input below (Press 'Enter key' to stop):")
    logged_keys = []
    
    try:
        while True:
            key = input()  # Take user input line by line
            if key.lower() == 'enter':
                break
            logged_keys.append(key)
            print(f"Captured: {key}")
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\nKeylogger stopped manually.")
    
    print("\nLogged Keystrokes:")
    for key in logged_keys:
        print(key)

# Start the keylogger
if _name_ == "_main_":
    keylogger() 
