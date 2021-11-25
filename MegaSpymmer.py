import pyautogui as pag
import time
import pyperclip
import keyboard

def spam(text:str, amount:int):
    pyperclip.copy(text)
    for i in range(amount):
        time.sleep(0.01)
        keyboard.press_and_release('ctrl + v')
        pag.hotkey('enter')

txt = str(input("Input text: "))
am = int(input("Input amount: "))

time.sleep(5)

spam(txt, am)
