#!/usr/bin/env python
# encoding: utf-8
"""
arduino-shell.py

Created by Jonathan Sharer on 2008-11-16.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os

import arduino

class ArduinoShell:
	
	def __init__(self,path):
		"""constuctor"""
		self.board = arduino.Arduino(path)
		
	def getOpts(self):
		"""docstring for getOpts"""
		sys.stdout.write("1. Read\n2. Write\n3. Abort\n")

	def opIsValid(self,op):
		if op == "1":
			print "It's 1 - read"
			return True
		elif op == "2":
			print "It's 2 - write"
			return True
		elif op == "3":
			print "It's 3 - abort"
			return True
		return False

	def handleOp(self,op):
		"""docstring for handleOp"""
		print "OP: ", op
		if op == "1":
			self.handleRead()
		elif op == "2":
			self.handleWrite()
		elif op == "3":
			self.handleAbort()
			return True
		return False

	def handleRead(self):
		"""docstring for handleRead"""
		print "Reading: ", self.board.readLine()

	def handleWrite(self):
		"""docstring for handleWrite"""
		sys.stdout.write("Write: ")
		writeLine = sys.stdin.readline()
		self.board.writeLine(writeLine)

	def handleAbort(self):
		"""docstring for handleAbort"""
		return True

	def promptLoop(self):
		"""docstring for promptLoop"""
		abort = False

		while abort == False:
			self.getOpts()
			opt = sys.stdin.readline().rstrip()
			if self.opIsValid(opt) is True:
				abort = self.handleOp(opt)
			else:
				sys.stderr.write("Error: Option is invalid\n")

if __name__ == '__main__':
	arduino = ArduinoShell("/dev/tty.usbserial-A80081qe")
	arduino.promptLoop()