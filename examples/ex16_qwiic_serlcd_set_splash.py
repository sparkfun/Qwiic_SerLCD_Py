#!/usr/bin/env python
#-----------------------------------------------------------------------------
# ex16_qwiic_serlcd_set_splash.py
#
# This example demonstrates how to create your own custom splash screen.
#
# This is done by first writing the text you want as your splash to the display,
# then 'saving' it as a splash screen.
#
# You can also disable or enable the displaying of the splash screen.
#
# Note - The disableSplash() and enableSplash() commands  
# are only supported on SerLCD v1.2 and above. But you can still use the
# toggle splash command (Ctrl+i) to enable/disable the splash.
#
#------------------------------------------------------------------------
#
# Written by SparkFun Electronics, August 2020
#
# Originally written for the Arduino Library by Nathan Seidle 2/16/2019
#
# Ported to this python example by Pete Lewis 8/18/2020
#
# Ported from Arduino Library code with many contributions from
# Gaston Williams - August 29, 2018
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatable) single
# board computers. 
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2020 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
# Example 16
#

import qwiic_serlcd
import time
import sys

def runExample():

	print("\nSparkFun Qwiic SerLCD   Example 16\n")
	print("\nType CTRL+C to end.\n")
	myLCD = qwiic_serlcd.QwiicSerlcd()

	if myLCD.connected == False:
		print("The Qwiic SerLCD device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myLCD.setBacklight(255, 255, 255) # bright white
	myLCD.setContrast(5) # set contrast. Lower to 0 for higher contrast.
	myLCD.begin() # call this for default settings (no
	myLCD.leftToRight()
	myLCD.noCursor()
	time.sleep(1) # give a sec for system messages to complete

	myLCD.clearScreen()
	myLCD.print("Tea-O-Matic")
	time.sleep(1)

	myLCD.saveSplash() # save this current text as the splash screen at next power up

	myLCD.enableSplash() # This will cause the splash to be displayed at power on
	#myLCD.disableSplash() # This will supress the splash from being displayed at power on

	counter = 0

	myLCD.clearScreen()
	myLCD.print("Cups of tea: ")

	while True:				
		print("counter: %d" % counter)
		myLCD.setCursor(0,1)
		myLCD.print(str(counter))
		counter = counter + 1
		time.sleep(1)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 16")
		sys.exit(0)


