#!/usr/bin/env python
# encoding: utf-8
"""
arduino.py

Created by Jonathan Sharer on 2008-11-16.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest

#from device import Device
import serial

class Arduino:
	serialConnection = None
	
	def __init__(self, path):
		self.serialConnection = serial.Serial(path,9600)
		pass
		
	def __del__(self):
		"""docstring for __del__"""
		self.serialConnection.close()
		pass
		
	def canAccessConnection(self):
		"""docstring for canAccessConnection"""
		if not self.serialConnection.isOpen():
			self.serialConnection.open()
		
		return True
		
		return self.serialConnection.isOpen()

	def readLine(self):
		"""docstring for readLine"""
		if self.canAccessConnection():
			return self.serialConnection.readline()
		else:
			return None
		pass
		
	def writeLine(self,line):
		"""docstring for writeLine"""
		if self.canAccessConnection():
			self.serialConnection.write(line)

class ArduinoTests(unittest.TestCase):
	def setUp(self):
		pass
		
if __name__ == '__main__':
	unittest.main()