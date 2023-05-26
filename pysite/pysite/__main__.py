import sys
import os

def main():
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

	if sys.argv[1] == "new":
		if len(sys.argv) < 3:
			print("Missing project name!")
			exit(1)

		proj_name = sys.argv[2]

		try:
			os.mkdir(proj_name)
			os.mkdir(f"{proj_name}/components")
			os.mkdir(f"{proj_name}/snippets")

			with open(f"{proj_name}/app.pyx", 'w') as f:
				f.write(
					'import pysite\nfrom flask import Flask\nfrom pysite.tags '
					'import *\n\napp = Flask(__name__)\n\n@app.route(\'/\')\n'
					'def index():\n\treturn (\n\t\t<pyx>\n\t\t\t<h1>'
					'Hello World!</h1>\n\t\t\t<br></br>\n\t\t\t<p '
					'style="display:inline-block;">This site was built with</p>'
					'\n\t\t\t<a href="https://github.com/User0332/pyx">PySite'
					'</a>\n\t\t</pyx>\n\t).html'
				)

			open(f"{proj_name}/components/__init__.py", 'w').close()
			open(f"{proj_name}/snippets/__init__.py", 'w').close()
		except OSError as e:
			print(f"An error occurred: {e}")

if __name__ == "__main__":
	main()