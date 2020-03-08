#!/usr/bin/python

import logging
import os
import sys

#sys.path.append("lib")

import lib.log
import lib.testpmd
import lib.pktgen

def main():
	a= 100
	b = 200
	c = a + b
	print(c)

if __name__ == '__main__':
	lib.log.set_log_conf()
	logger = logging.getLogger(__name__)
	logger.info("test")
	lib.testpmd.test_testpmd()
	lib.pktgen.test_pktgen()
	
