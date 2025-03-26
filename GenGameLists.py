#!/usr/bin/env python3
# Generate gamelist for Lutris (or any other systems if you edit tuple below):
GEN_SYSTEMS = ("PC Games - Lutris", )

import glob
import os
import sys

from GenSsystemFiles import SYSTEMS
from pathlib import Path

HOME = os.environ.get("HOME")

for sys_t in SYSTEMS:
	#print(sys_t)
	# EDIT here if you want to use another system, use same name as in GenSsystemFiles:
	if not sys_t[0] in GEN_SYSTEMS:
		continue

	print("Entering system: " + str(sys_t[0]))

	sys.stderr.write("\nEntering system: " + str(sys_t[1]) + "\n")
	print(sys_t[2]) #  paths

	if not os.path.isdir(f"{HOME}/ES-DE/gamelists/" + sys_t[0]):
		os.makedirs(f"{HOME}/ES-DE/gamelists/" + sys_t[0])

	with open(f"{HOME}/ES-DE/gamelists/" + sys_t[0] + "/" + "gamelist.xml", "w") as f:
		f.write("<?xml version=\"1.0\"?><gameList>\n")

		for ext in sys_t[3].split(" "):

			print(">> ext:" + ext)

			for filename in glob.iglob(sys_t[2] + "/**/*%s" % ext, recursive=True):
				print(filename)

				f.write("<game>\n<path>%s</path>\n<name>%s</name>\n</game>\n\n" % (
						filename,
						os.path.basename(filename.replace(ext, ""))
					)
				)
		f.write("</gameList>")
