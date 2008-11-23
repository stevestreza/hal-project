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
import time

#from device import Device
import serial

class Arduino:
	serialConnection = None
	
	def __init__(self, path):
		self.serialConnection = serial.Serial(path,4800)
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
			if self.serialConnection.inWaiting() > 0:
				return self.serialConnection.readline()
			else:
				print "No data"
		else:
			return None
		pass
		
	def writeLine(self,line):
		"""docstring for writeLine"""
		if self.canAccessConnection():
			for i in range(0, len(line)):
				self.serialConnection.write(line[i])
				time.sleep(0.1)
	
	def readDPin(self,pin):
		command = "R1" + str(pin)
		self.serialConnection.flushInput()
		self.serialConnection.flushOutput()
		self.writeLine(command)
		result = self.readLine()
		result = result[result.find("Value: ")+7:result.find("Value: ")+10]
		if result[2] == '-':
			result = result[:1]
		return result
		
	def setDPin(self,pin,value):
		command = "S1" + str(pin) + str(value)
		self.writeLine(command)
		return True
	
	def readAPin(self,pin):
		command = "R0" + str(pin)
		self.serialConnection.flushInput()
		self.serialConnection.flushOutput()
		self.writeLine(command)
		result = self.readLine()
		result = result[result.find("Value: ")+7:result.find("Value: ")+10]
		if result[2] == '-':
			result = result[:1]
		return result

class ArduinoTests(unittest.TestCase):
	def setUp(self):
		pass
		
if __name__ == '__main__':
	unittest.main()