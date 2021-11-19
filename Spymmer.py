import pyautogui as pag
import time
import pyperclip
import keyboard

time.sleep(5)

def spam(text:str, amount:int):
    pyperclip.copy(text)
    for i in range(amount):
        time.sleep(0.01)
        keyboard.press_and_release('ctrl + v')
        pag.hotkey('enter')

txt = str(input("Input text: "))
am = int(input("Input amount: "))

spam(txt, am)
