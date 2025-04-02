import pyautogui
import time

def open_print_dialog():
    time.sleep(2)  # This is how many seconds you will have to switch to the window to print

    pyautogui.keyDown('alt')
    time.sleep(0.1)  
                    
    pyautogui.press('f')
    time.sleep(0.1) 
                    
    pyautogui.keyUp('alt')

    pyautogui.press('p')
    time.sleep(0.3)

if __name__ == "__main__":
    open_print_dialog()
