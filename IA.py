import pyautogui
import keyboard 
import time
x = 0
lista = 100
pyautogui.alert("o código vai começar")
pyautogui.PAUSE = 0.1
pyautogui.moveTo(900, 879)     
pyautogui.click()
for x in range(6): 
    pyautogui.press('f2')
    pyautogui.press('left')
    pyautogui.press('left')  
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.write('/')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.write('/')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('backspace')
    pyautogui.press('enter')

