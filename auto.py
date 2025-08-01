import mouseinfo, pyautogui, time

pyautogui.alert('Vamos começar', title='Início')

pyautogui.moveTo(1300,1055, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(1821,152, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(582,62, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.write("Casa")
pyautogui.press('enter')

pyautogui.moveTo(308,191, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(554,416, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.hotkey('ctrl', 'c')    

pyautogui.press('win')

pyautogui.moveTo(730,1058, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.write("paint")

pyautogui.press('enter')

pyautogui.moveTo(1073,478, duration=2)

pyautogui.scroll(-50)

pyautogui.hotkey('ctrl', 'v') 

mouseinfo.mouseInfo()