import sys
import os

if len(sys.argv) < 2: exit(1)

compiled_files = []

if sys.argv[1] == "run":
	for path, dirnames, filenames in os.walk(os.getcwd()):
		filename: str
		for filename in filenames:
			if filename.endswith(".pyx"):
				compiled_files.append(
					'.'.join(
						os.path.join(path, filename)
							.split('.')[-1]
					)+".py"
				)
				os.system(f"pyxc {os.path.join(path, filename)}")

	try: os.system("flask run")
	except KeyboardInterrupt: pass