import pyautogui
import keyboard 
import time
x = 0
lista = 100
pyautogui.alert("o código vai começar")
pyautogui.PAUSE = 0.3
icon_sge = pyautogui.locateOnScreen('./sge.png')
pyautogui.click(icon_sge)

for x in range(3):   
    pyautogui.moveTo(538, 151)
    pyautogui.click()
    pyautogui.moveTo(745, 215)
    pyautogui.click()
    pyautogui.write('SERVIÇO SOCIAL DA INDUSTRIA - SESI')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('03.777.433/0004-99')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('cnpj')
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    #pyautogui.moveTo(695, 435)
    #pyautogui.click()
    pyautogui.write('5')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('0')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('0')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('0')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('1')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('3')
    pyautogui.press('tab')
    pyautogui.moveTo(1081, 728)
    pyautogui.click()
    time.sleep(1)
    if pyautogui.press == 'p':
        print("You pressed p")
        break


'''
time.sleep(3)
print(pyautogui.position())

'''

'''
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('youtube.com')
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(931, 102)
pyautogui.click()
pyautogui.write('Banho dos campeoes')
pyautogui.press('enter')
pyautogui.moveTo(671, 518)
time.sleep(2)
pyautogui.click()
'''