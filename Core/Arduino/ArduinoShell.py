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
		sys.stdout.write("1. Debug Mode\n2. Write\n3. Abort\n")

	def opIsValid(self,op):
		if op == "1":
			print "It's 1 - Debug Mode"
			return True
		elif op == "2":
			print "It's 2 - Write"
			return True
		elif op == "3":
			print "It's 3 - Abort"
			return True
		return False

	def handleOp(self,op):
		"""docstring for handleOp"""
		print "OP: ", op
		if op == "1":
			self.handleDebug()
		elif op == "2":
			self.handleWrite()
		elif op == "3":
			self.handleAbort()
			return True
		return False

	def handleDebug(self):
		while True:
			print "Debug Menu"
			print "----------\n"
			print "1. Read Digital Pin"
			print "2. Set Digital Pin"
			print "3. Read Analog Pin"
			print "4. Set Analog Pin"
			print "0. Leave"
			dopt = sys.stdin.readline().rstrip()
			
			if dopt == "1":
				print "Pin Number(0-13):"
				pinNo = int(sys.stdin.readline().rstrip())
				if pinNo >= 0 & pinNo <= 13:
					value = self.board.readDPin(pinNo)
					print value
			elif dopt == "2":
				print "Pin Number(0-13):"
				pinNo = int(sys.stdin.readline().rstrip())
				if pinNo >= 0 & pinNo <= 13:
					print "On or Off (1/0)?"
					value = int(sys.stdin.readline().rstrip())
					if value >=0 & value <=1:
						self.board.setDPin(pinNo, value)
					else:
						print "Value out of range."
				else:
					print "Value out of range."
			elif dopt == "3":
				print "Pin Number (0-5):"
				pinNo = int(sys.stdin.readline().rstrip())
				if pinNo >= 0 & pinNo <= 13:
					print self.board.readAPin(pinNo)
			elif dopt == "0":
				break
			else:
				print "Value out of range."
		return True
		
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

def arduinoShellPrompt():
	"""docstring for arduinoShellPrompt"""
	arduino = ArduinoShell("/dev/tty.usbserial-A80081qe")
	arduino.promptLoop()

if __name__ == '__main__':
	arduinoShellPrompt()