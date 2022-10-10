import sys
import os

if len(sys.argv) < 2: exit(1)

if sys.argv[1] == "run":
	for path, dirnames, filenames in os.walk(os.getcwd()):
		filename: str
		for filename in filenames:
			if filename.endswith(".pyx"):
				os.system(f"pyxc {os.path.join(path, filename)}")

	os.system("flask run")
