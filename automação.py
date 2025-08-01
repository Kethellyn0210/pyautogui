import mouseinfo, pyautogui, time

pyautogui.moveTo(610,1046,duration=2)
pyautogui.click()
time.sleep(1)
pyautogui.write('carros')
pyautogui.press('enter')

mouseinfo.mouseInfo()
