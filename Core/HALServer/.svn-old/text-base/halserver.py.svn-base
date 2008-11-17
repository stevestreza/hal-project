#!/usr/bin/env python
# encoding: utf-8
"""
halserver.py

Created by Steve Streza on 2008-09-10.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest

class HALServer:
	mAbortRunLoop = False
	def __init__(self):
		pass

	def run(self):
		"""docstring for run"""
		print "Running"
		while not self.mAbortRunLoop:
			print "run"
		pass
		
	def stopServer(self):
		"""docstring for stopServer"""
		self.mAbortRunLoop = True

class HALServerTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()