from grove_rgb_lcd import *

while(True):
	setText("Hello World!")
	setRGB(0,128,64)
	for c in range(0,15):
		setRGB(c,255-c,0)
		time.sleep(0.01)
	setRGB(0,255,0)
	setText("bye bye")
	time.sleep(0.5)
