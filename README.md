Qwiic_SerLCD_Py
==============

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-serlcd/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun_qwiic_serlcd.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_SerLCD_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_SerLCD_Py.svg" /></a>
	<a href="https://qwiic-serlcd-py.readthedocs.io/en/latest/" alt="Documentation">
		<img src="https://readthedocs.org/projects/qwiic-serlcd-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_SerLCD_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>
</p>

<table class="table table-hover table-striped table-bordered">
    <tr align="center">
        <td><a href="https://www.sparkfun.com/products/16396"><img src="https://cdn.sparkfun.com//assets/parts/1/1/9/2/5/14072-SparkFun_16x2_SerLCD_-_Black_on_RGB_3.3V-04.jpg" title="SparkFun SerLCD 16x2 - RGB Backlight (QWIIC)"></a></td>
        <td><a href="https://www.sparkfun.com/products/16397"><img src="https://cdn.sparkfun.com//assets/parts/1/1/9/2/5/14072-SparkFun_16x2_SerLCD_-_Black_on_RGB_3.3V-04.jpg" title="SparkFun SerLCD 16x2 - RGB Text (QWIIC)"></a></td>
        <td><a href="https://www.sparkfun.com/products/16398"><img src="https://cdn.sparkfun.com//assets/parts/1/1/9/2/5/14072-SparkFun_16x2_SerLCD_-_Black_on_RGB_3.3V-04.jpg" title="SparkFun SerLCD 20x2 - RGB Backlight (QWIIC)"></a></td>
    </tr>
    <tr align="center">
        <td><i><a href="https://www.sparkfun.com/products/16396">SparkFun SerLCD 16x2 - RGB Backlight (QWIIC)</a></i></td>
        <td><i><a href="https://www.sparkfun.com/products/16397">SparkFun SerLCD 16x2 - RGB Text (QWIIC)</a></i></td>
        <td><i><a href="https://www.sparkfun.com/products/16398">SparkFun SerLCD 20x2 - RGB Backlight (QWIIC)</a></i></td>
    </tr>
</table>

Python module for I2C control of the SparkFun Qwiic Serial LCDs.

This package enables the user to access all of the features of these LCD products via a single Qwiic cable. This includes writing text to the screen, adjusting backlight levels (color), customizing splash screen and much much more. They come pre-programmed with the fully open-sourced [OpenLCD firmware](https://github.com/sparkfun/OpenLCD). All of the capabilities of these LCD screens are each demonstrated in the included 17 examples.

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

## Contents

* [Supported Platforms](#supported-platforms)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Supported Platforms
--------------------
The qwiic serlcd python package current supports the following platforms:
* [Raspberry Pi](https://www.sparkfun.com/search/results?term=raspberry+pi)
* [NVidia Jetson Nano](https://www.sparkfun.com/products/15297)
* [Google Coral Development Board](https://www.sparkfun.com/products/15318)

Dependencies 
---------------
This driver package depends on the qwiic I2C driver: 
[Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)

Documentation
-------------
The SparkFun qwiic serlcd documentation is hosted at [ReadTheDocs](https://qwiic-serlcd-py.readthedocs.io/en/latest/)

Installation
-------------

### PyPi Installation
This repository is hosted on PyPi as the [sparkfun-qwiic-serlcd](https://pypi.org/project/sparkfun-qwiic-serlcd/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-serlcd
```
For the current user:

```sh
pip install sparkfun-qwiic-serlcd
```

### Local Installation
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun_qwiic_serlcd-<version>.tar.gz
  
```
Example Use
 ---------------
See the examples directory for more detailed use examples.

```python
from __future__ import print_function
import qwiic_serlcd
import time
import sys

def runExample():

	print("\nSparkFun Qwiic SerLCD   Example 1\n")
	myLCD = qwiic_serlcd.QwiicSerlcd()

	if myLCD.connected == False:
		print("The Qwiic SerLCD device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myLCD.setBacklight(255, 255, 255) # Set backlight to bright white
	myLCD.setContrast(5) # set contrast. Lower to 0 for higher contrast.
	myLCD.clearScreen() # clear the screen - this moves the cursor to the home position as well

	time.sleep(1) # give a sec for system messages to complete
	
	myLCD.print("Hello World!")
	counter = 0
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
		print("\nEnding Example 1")
		sys.exit(0)
```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>
