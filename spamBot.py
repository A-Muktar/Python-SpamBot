# importing modules, you may have to install the pyautogui using "pip install pyautogui"
import pyautogui, time
time.sleep(10) # number of second to wait after running the program
msg = open("file.txt", "r")  # read file and send msgs from the file one after another.
for word in msg:  # loop over the number of lines in the file
	pyautogui.typewrite(word) 
	time.sleep(10) # Delay time after each msg
	pyautogui.press('enter')
