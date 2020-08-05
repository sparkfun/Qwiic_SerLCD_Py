#-----------------------------------------------------------------------------
# qwiic_serlcd.py
#
# Python library for I2C control of the SparkFun Serial LCDs (QWIIC):
#
#   SparkFun 16x2 SerLCD - RGB Backlight (Qwiic)
#   https://www.sparkfun.com/products/16396
#
#   SparkFun 16x2 SerLCD - RGB Text (Qwiic)
#   https://www.sparkfun.com/products/16397
#
#   SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)
#   https://www.sparkfun.com/products/16398
#
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, August 2020
#
# This python library supports the SparkFun Electroncis qwiic
# qwiic sensor/board ecosystem
#
# More information on qwiic is at https:// www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#==================================================================================
# Copyright (c) 2019 SparkFun Electronics
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
#
# This is mostly a port of existing Arduino functionaly, so pylint is sad.
# The goal is to keep the public interface pthonic, but internal is internal
#
# pylint: disable=line-too-long, too-many-public-methods, invalid-name
#

"""
qwiic_serlcd
===============
Python module for the SparkFun SerLCD QWIIC products:

[SparkFun 16x2 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/products/16396)
[SparkFun 16x2 SerLCD - RGB Text (Qwiic)](https://www.sparkfun.com/products/16397)
[SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/products/16398)

This python package enables the user to control the SerLCDs via I2C.
It is intended to be used by simply plugging in a qwiic cable for power and I2C communicaiton.

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

"""
#-----------------------------------------------------------------------------
from __future__ import print_function
import struct

import qwiic_i2c

# Define the device name and I2C addresses. These are set in the class defintion
# as class variables, making them avilable without having to create a class instance.
# This allows higher level logic to rapidly create a index of qwiic devices at
# runtine
#
# The name of this device
_DEFAULT_NAME = "SparkFun Qwiic SerLCD"

# Some devices have multiple availabel addresses - this is a list of these addresses.
# NOTE: The first address in this list is considered the default I2C address for the
# device.
_AVAILABLE_I2C_ADDRESS = [0x72] # default address, note it can be changed via software commands

# Register codes for the SparkFun SerLCD

DISPLAY_ADDRESS1 = 0x72 # This is the default address of the OpenLCD
MAX_ROWS = 4
MAX_COLUMNS = 20

# OpenLCD command characters
SPECIAL_COMMAND = 254  # Magic number for sending a special command
SETTING_COMMAND = 0x7C # 124, |, the pipe character: The command to change settings: baud, lines, width, backlight, splash, etc

# OpenLCD commands
CLEAR_COMMAND = 0x2D					# 45, -, the dash character: command to clear and home the display
CONTRAST_COMMAND = 0x18				# Command to change the contrast setting
ADDRESS_COMMAND = 0x19				# Command to change the i2c address
SET_RGB_COMMAND = 0x2B				# 43, +, the plus character: command to set backlight RGB value
ENABLE_SYSTEM_MESSAGE_DISPLAY = 0x2E  # 46, ., command to enable system messages being displayed
DISABLE_SYSTEM_MESSAGE_DISPLAY = 0x2F # 47, /, command to disable system messages being displayed
ENABLE_SPLASH_DISPLAY = 0x30			# 48, 0, command to enable splash screen at power on
DISABLE_SPLASH_DISPLAY = 0x31			# 49, 1, command to disable splash screen at power on
SAVE_CURRENT_DISPLAY_AS_SPLASH = 0x0A # 10, Ctrl+j, command to save current text on display as splash

# special commands
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# define the class that encapsulates the device being created. All information associated with this
# device is encapsulated by this class. The device class should be the only value exported
# from this module.

class QwiicSerlcd(object):
    """
    QwiicSerlcd

        :param address: The I2C address to use for the device.
                        If not provided, the default address is used.
        :param i2c_driver: An existing i2c driver object. If not provided
                        a driver object is created.
        :return: The QwiicSerlcd device object.
        :rtype: Object
    """
    # Constructor
    device_name = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # Constructor
    def __init__(self, address=None, i2c_driver=None):

        # Did the user specify an I2C address?
        self.address = address if address is not None else self.available_addresses[0]

        # load the I2C driver if one isn't provided

        if i2c_driver is None:
            self._i2c = qwiic_i2c.getI2CDriver()
            if self._i2c is None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver

    # ----------------------------------
    # isConnected()
    #
    # Is an actual board connected to our system?

    def is_connected(self):
        """
            Determine if a device is conntected to the system..

            :return: True if the device is connected, otherwise False.
            :rtype: bool

        """
        return qwiic_i2c.isDeviceConnected(self.address)

    connected = property(is_connected)
    # ----------------------------------
    # begin()
    #
    # Initialize the system/validate the board.
    def begin(self):
        """
            Initialize the operation of the SerLCD module

            :return: Returns true of the initializtion was successful, otherwise False.
            :rtype: bool

        """
        # Basically return True if we are connected...
        return self.is_connected()

    # ----------------------------------
    # print()
    #
    # Print a string of characters to the LCD
    def print(self, string):
        """
            Print a string of characters to the LCD

            :param string: The string you would like to print. Aka ASCII characters. example: "Hello"
            
            :return: Returns true if the I2C writes were successful, otherwise False.
            :rtype: bool

        """
        for c in string:
                if self._i2c.writeCommand(self.address, ord(c)) == False:
                        return False
        return True

    # ----------------------------------
    # clearScreen()
    #
    # Clear the screen
    def clearScreen(self):
        """
            Sends the command to clear the screen

            :return: Returns true if the I2C write was successful, otherwise False.
            :rtype: bool

        """
        return self._i2c.writeByte(self.address, SETTING_COMMAND, CLEAR_COMMAND)

    # ----------------------------------
    # setCursor()
    #
    # Set the cursor position to a particular column and row.
    def setCursor(self, col, row):
        """
            Set the cursor position to a particular column and row.

            :param col: The column postion (0-19)
            :param row: The row postion (0-3)
            
            :return: Returns true if the I2C write was successful, otherwise False.
            :rtype: bool

        """        
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        
        # kepp variables in bounds
        row = max(0, row)            # row cannot be less than 0
        row = min(row, (MAX_ROWS - 1)) # row cannot be greater than max rows

        # construct the cursor "command"
        command = LCD_SETDDRAMADDR | (col + row_offsets[row])

        # send the complete bytes (special command + command)
        return self._i2c.writeByte(self.address, SPECIAL_COMMAND, command)


    # ----------------------------------
    # setContrast()
    #
    # Set the contrast to a new value.
    def setContrast(self, contrast):
        """
            Set the contrast of the LCD screen (0-255) 120 is default.

            :param contrast: The new contrast value (0-255)
            
            :return: Returns true if the I2C write was successful, otherwise False.
            :rtype: bool

        """
        # To set the contrast we need to send 3 bytes:
        # (1) SETTINGS_COMMAND
        # (2) CONTRAST_COMMAND
        # (3) contrast value
        #
        # To do this, we are going to use writeWord(),
        # so we need our "command" to include
        # CONTRAST_COMMAND and contrast value

        command = ( contrast<< 8) | CONTRAST_COMMAND 
        
        # send the complete bytes (address, settings command , contrast command, contrast value)
        return self._i2c.writeWord(self.address, SETTING_COMMAND, command)    
