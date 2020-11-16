import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100,50)
pyautogui.click()
pyautogui.click(200, 220)

pyautogui.doubleClick()

pyautogui.write("Hello World", interval=0.25)
pyautogui.press("esc")
pyautogui.keyDown('shift')
pyautogui.write(['left', 'left','left','left','left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')

