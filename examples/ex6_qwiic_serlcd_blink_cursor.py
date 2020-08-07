#!/usr/bin/env python
#-----------------------------------------------------------------------------
# ex6_qwiic_serlcd_blink_cursor.py
#
# Simple example demonstrating the blinking cursor controls on the SerLCD (Qwiic).
#
# This example prints "Hello World!" to the LCD and
# uses the blink()  and noBlink() methods to turn
# on and off the blinking.
#------------------------------------------------------------------------
#
# Written by SparkFun Electronics, August 2020
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
# Example 6
#

from __future__ import print_function
import qwiic_serlcd
import time
import sys

def runExample():

	print("\nSparkFun Qwiic SerLCD   Example 6\n")
	myLCD = qwiic_serlcd.QwiicSerlcd()

	if myLCD.connected == False:
		print("The Qwiic SerLCD device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myLCD.setBacklight(255, 255, 255) # Set backlight to bright white
	myLCD.setContrast(5) # set contrast. Lower to 0 for higher contrast.
	myLCD.clearScreen()
	myLCD.cursor() # Turn on the underline cursor

	time.sleep(1) # give a sec for system messages to complete
	myLCD.print("Hello World!")
	
	while True:
		# turn off the blinking cursor
		print("Cursor blinking OFF")
		myLCD.noBlink()
		time.sleep(5)
		
		# turn on the blinking cursor
		print("Cursor blinking ON")
		myLCD.blink()
		time.sleep(5)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 6")
		sys.exit(0)


