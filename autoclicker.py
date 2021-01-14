import win32api, win32con, keyboard, time
try:
	import keyboard
except ModuleNotFoundError:
	import os
	print('WAIT FOR MODULE TO INSTALL')
	os.system('python -m pip install keyboard')
	os.system('cls')
	import keyboard

print('T, -, esc to toggle the buttons\nR for left click F for right click\nFOR DIFFICULTIES ctrl+c to disable the program without closeing ctrl+r to RUN THE PROGRAM\nctrl+shift+c to close the program')
delay=0.05
def click(DELAY,x=False,y=False):
	if not x and not y:
		postuple=win32api.GetCursorPos()
		x=postuple[0]
		y=postuple[1]
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(DELAY)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def rclick(DELAY,x=False,y=False):
	if not x and not y:
		postuple=win32api.GetCursorPos()
		x=postuple[0]
		y=postuple[1]
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
	time.sleep(DELAY)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
toggle=True
nexte=True
try:
	while True:
		if keyboard.is_pressed('ctrl+c'):
			nexte=False
		elif keyboard.is_pressed('ctrl+r'):
			nexte=True
		elif keyboard.is_pressed('ctrl+shift+c'):
			exit()
		if nexte:
			if keyboard.is_pressed('-') == True or keyboard.is_pressed('esc') == True or keyboard.is_pressed('t') == True:
				toggle=not toggle
				time.sleep(0.5)
			if toggle:
				while keyboard.is_pressed('r') or keyboard.is_pressed('caps lock'):
					click(delay)
				while keyboard.is_pressed('f'):
					rclick(delay)
except KeyboardInterrupt:
	exit()