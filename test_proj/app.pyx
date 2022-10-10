import pysite
from flask import Flask, render_template_string
from pysite.tags import *
from components.button import mybutton
from snippets import mystyle

app = Flask(__name__)
app.debug = True

def create_index() -> str:
	style = "color: red"
	onclick = "alert('button clicked')"

	return (
		<pyx>
			<head>
				<title>My Site!</title>
				<mystyle></mystyle>
			</head>
			<body>
				<h1 style={style} id="heading">Welcome to my site!</h1>
				<mybutton onclickjs={onclick}>Click Me!</mybutton>
			</body>
		</pyx>
	).html

@app.route('/')
def index():
	return render_template_string(
		create_index()
	)
