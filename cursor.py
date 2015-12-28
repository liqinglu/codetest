"""
To try how to manipulate mouse moving on the screen
"""
from ctypes import *
import time

# for windows
x = 1
y = 1
while 1:
	windll.user32.SetCursorPos(x,y)
	time.sleep(1)
	x += 1
	y += 1
	if x > 500:
		x = 1
	if y > 500:
		y = 1
# for linux
