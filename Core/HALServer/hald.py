#!/usr/bin/env python
# encoding: utf-8
"""
hald.py

Created by Jonathan Sharer on 2008-11-22.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import arduino


class hald:
	switch = {'testLight': 'A113'} # address format: <Controller(char)><Digital(1/0)><Pin Number>
	analog = {'testAnalog': 'A00'}
	arduino = {}
	
	def __init__(self):
		pass
		
	def setSwitch(self,name,state):
		address = self.switch[name]
		controller = address[0:1]
		digital = address[1:2]
		pinNo = address[2:4]
		#command = "S" + str(digital) + str(pinNo) + str(state)
		#self.arduino[controller].writeLine(command)
		self.arduino[controller].setDPin(pinNo, state)
	
	def readSwitch(self,name):
		address = self.switch[name]
		controller = address[0:1]
		digital = address[1:2]
		pinNo = address[2:4]
		return self.arduino[controller].readDPin(pinNo)
	
	def getSwitches():
		return switch
		
	def readAnalog(self,name):
		address = self.analog[name]
		controller = address[0:1]
		digital = address[1:2]
		pinNo = address[2:3]
		return self.arduino[controller].readAPin(pinNo)

	def addArduino(self,name,newArduino):
		self.arduino[name] = newArduino

if __name__ == '__main__':
	main()

