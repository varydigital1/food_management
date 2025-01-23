import pyautogui # type: ignore
import time

a = 0
text = ""
while a<10:
    time.sleep(2)
    if a<5:
        text = "I Love You"
    else:
        text = "I Miss You"
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    a+=1