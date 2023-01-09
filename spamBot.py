import pyautogui, time
time.sleep(10)
msg = open("file.txt", "r") 
for word in msg: 
	pyautogui.typewrite(word) 
	time.sleep(10)
	pyautogui.press('enter')