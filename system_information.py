#!/usr/bin/python

import os
import sys
import subprocess
import time
import datetime
import argparse

# add argument functionality
parser = argparse.ArgumentParser(description='Print system information.')
parser.add_argument('-f', '--file', help='save output to a separate log file (system_information_logs/system_information.log)', action = 'store_true')
args = parser.parse_args()

if (args.file):
	if not os.path.exists('system_information_logs'):
		os.makedirs('system_information_logs')

	# timestamp information
	ts = time.time()
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	# open the file to be written to
	file = open('system_information_logs/system_information' + timestamp + '.log', 'w')
	subprocess.Popen(['echo', '---------- Timestamp ----------'], stdout = file)
	subprocess.Popen(['echo', timestamp], stdout = file)

	# kernel information
	subprocess.Popen(['echo', '---------- Kernel Output ----------'], stdout = file)
	p1 = subprocess.Popen(['uname', '-a'], stdout = file)
	output = p1.communicate()[0]

	# facter information
	subprocess.Popen(['echo', '---------- Facter Output ----------'], stdout = file)
	p1 = subprocess.Popen(['facter', '--puppet'], stdout = file)
	output = p1.communicate()[0]

	# LSI information
	subprocess.Popen(['echo', '---------- LSIUtil Output ----------'], stdout = file)
	p1 = subprocess.Popen(['lsiutil', '-p', '1', '1'], stdout = file)
	output = p1.communicate()[0]

	# version information
	subprocess.Popen(['echo', '---------- Version Output ----------'], stdout = file)
	p1 = subprocess.Popen(['cat', '/sys/module/mpt2sas/version'], stdout = file)
	output = p1.communicate()[0]

	# Device information
	subprocess.Popen(['echo', '---------- Devices Output ----------'], stdout = file)
	p1 = subprocess.Popen(["lspci"], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(["grep", "LSI"], stdin=p1.stdout, stdout = file)
	p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
	output = p2.communicate()[0]

	file.close()

	subprocess.call(['echo File system_infomration.log created successfully.'], shell = True)
else:
	# timestamp information
	subprocess.call(['echo ---------- Timestamp ----------'], shell = True)
	ts = time.time()
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	subprocess.call(['echo ' + timestamp], shell = True)

	# kernel information
	subprocess.call(['echo ---------- Kernel Output ----------'], shell = True)
	p1 = subprocess.Popen(['uname', '-a'], stdin=subprocess.PIPE)
	output = p1.communicate()[0]

	# facter information
	subprocess.call(['echo ---------- Facter Output ----------'], shell = True)
	p1 = subprocess.Popen(['facter', '--puppet'], stdin=subprocess.PIPE)
	output = p1.communicate()[0]

	# LSI information
	subprocess.call(['echo ---------- LSIUtil Output ----------'], shell = True)
	p1 = subprocess.Popen(['lsiutil', '-p', '1', '1'], stdin=subprocess.PIPE)
	output = p1.communicate()[0]

	# version information
	subprocess.call(['echo ---------- Version Output ----------'], shell = True)
	p1 = subprocess.Popen(['cat', '/sys/module/mpt2sas/version'], stdin=subprocess.PIPE)
	output = p1.communicate()[0]

	# Device information
	subprocess.call(['echo ---------- Devices Output ----------'], shell = True)
	p1 = subprocess.Popen(["lspci"], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(["grep", "LSI"], stdin=p1.stdout, stdout=subprocess.PIPE)
	p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
	output = p2.communicate()[0]

	#subprocess.call(['echo ' + output], shell = True)
	print(output)
