import pyautogui
import keyboard 
import time
import pyscreeze

x = 0

pyautogui.alert("o código vai começar")
pyautogui.PAUSE = 0.2
pyautogui.moveTo(771, 888)     
pyautogui.click()

for x in range(26):
    icon_pos = pyautogui.locateOnScreen('./icon.png')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')
    pyautogui.moveTo(866, 888)
    pyautogui.click()
    pyautogui.moveTo(593, 178)
    pyautogui.click()
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    pyautogui.press('enter')
    time.sleep(0.5)
    icon_pos = pyautogui.locateOnScreen('./icon.png')
    if icon_pos:
        print(icon_pos)
        print("Existe um cadeado aberto na tela")
        pyautogui.moveTo(771, 888)     
        pyautogui.click()
        pyautogui.moveTo(356, 102)     
        pyautogui.click()
        pyautogui.moveTo(407, 260)     
        pyautogui.click()
        pyautogui.press('enter')
    else: 
        pyautogui.moveTo(771, 888)     
        pyautogui.click()
        pyautogui.moveTo(356, 102)     
        pyautogui.click()
        pyautogui.moveTo(390, 257)     
        pyautogui.click()
        pyautogui.press('enter')