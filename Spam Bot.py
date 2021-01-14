'''
if you are useing an advanced IDE then search on the fifth line, the number '5' on the left area click that to close
the def function so you can use the test area
'''
def main():
	try:
		osss=True
		while osss:
			try:
				import os, time
				osss=False
			except KeyboardInterrupt:
				pass
		os.system('cls')
		os.system('title Spam Bot')
		print('\nCHATSPAMMER\n--------------\n\u001b[31mMADE BY KARTIK\u001b[0m \n--------------\nv2.1.0 error-less\n')

		pyautotrue=True
		while pyautotrue:
			try:
				import pyautogui
				pyautotrue=False
			except ModuleNotFoundError:
				print('\u001b[33mYou dont have pyautogui installed wait while it installs\u001b[0m')
				time.sleep(2)
				print('\n')
				os.system("python -m pip install pyautogui")
				time.sleep(2)
				os.system('cls')
				try:
					import pyautogui
					print('\n\u001b[32mpyautogui is installed, lets begain with spamming!\u001b[0m \n')
					time.sleep(2)
					os.system('cls')
					print('\nCHATSPAMMER\n--------------\n\u001b[31mMADE BY KARTIK\u001b[0m \n--------------\nv2.1.0 error-less\n')
				except ModuleNotFoundError:
					os.system("cls")
					print('\u001b[31mMake sure you are connected to internet and your internet works fine; in order to install pyautogui\u001b[0m')
					a=input('')
					pyautotrue=False
			except KeyboardInterrupt:
				pass
		try:
			import keyboard
		except ModuleNotFoundError:
			print('\u001b[33mYou dont have keyboard installed wait while it installs\u001b[0m')
			time.sleep(2)
			print('\n')
			os.system("python -m pip install keyboard")
			time.sleep(2)
			os.system('cls')
			try:
				import pyautogui
				print('\n\u001b[32mpyautogui is installed, lets begain with spamming!\u001b[0m \n')
				time.sleep(2)
				os.system('cls')
				print('\nCHATSPAMMER\n--------------\n\u001b[31mMADE BY KARTIK\u001b[0m \n--------------\nv2.1.0 error-less\n')
			except ModuleNotFoundError:
				os.system("cls")
				print('\u001b[31mMake sure you are connected to internet and your internet works fine; in order to install pyautogui\u001b[0m')
				a=input('')
				exit()
		ok='yes'
		stop='no'
		txt= input('What do you want to spam\n>>> ')
		timez=0
		dly=0
		
		dlyTrue=True
		while dlyTrue:
			try:
				dly=float(input('Enter the delay(seconds) that you want to give[MIN: 0| MAX:5](0.5 recommanded for most spamming cases)\n>>> '))
				if dly>=0 and dly<=5:
					dlyTrue=False
				else:
					print('\n**[MINIMUM: 0| MAXIMUM:5]**')
			except ValueError:
				print('\nKindly use an decimal or integer')
		timeTrue=True
		while timeTrue:
			try:
				timez=int(input('How many times do you want to spam [CONTINUE AT YOUR OWN RISK!!]\n>>> '))
				timeTrue=False
			except ValueError:
				print('\nKindly use an integer')
		try:
			sure=input('To start press enter! to cancel press ctrl+C OR esc[CONTINUE AT YOUR OWN RISK!!]\n')
			print('Starting...')
			time.sleep(.3)
		except KeyboardInterrupt:
			print('\nStopping...')
			time.sleep(.3)
			print('Stopped!')
			stop='yes'
			pass
		if stop!='yes':
			print('Starting in 5 seconds! *press ctrl+C or esc* to cancel!')
			time.sleep(5)
			#MAIN ;) all those were non-sense(things so that this becomes error-less)
			for _ in range(timez):
				time.sleep(dly)
				pyautogui.typewrite(txt)
				pyautogui.press('enter')
				if keyboard.is_pressed('esc'):
					exit()
			a=input('')
	except KeyboardInterrupt:
			print('\nStopping...')
			try:
				time.sleep(.3)
				print('Stopped!')
			except KeyboardInterrupt:
				print('Stopped!')
main()
'''
v2.1.0

MADE BY KARTIK
-------------
|test here ↓|
-------------

'''