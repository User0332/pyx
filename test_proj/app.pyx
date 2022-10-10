import pysite
from flask import Flask, render_template_string
from pysite.tags import *
from components.button import mybutton
from snippets import mystyle

app = Flask(__name__)
app.debug = True

def create_index() -> str:
	h1style = "color: red"
	onclick = "alert('button clicked')"
	pstyle = "display: inline-block;"

	return (
		<pyx>
			<head>
				<title>My Site!</title>
				<mystyle></mystyle>
			</head>
			<body>
				<h1 style={h1style} id="heading">Welcome to my site!</h1>
				<mybutton onclickjs={onclick}>Click Me!</mybutton>
				<br></br>
				<p style={pstyle}>Built using</p>
				<a href="https://github.com/User0332/pyx">PySite</a>
			</body>
		</pyx>
	).html

@app.route('/home')
def home():
	return create_index()

@app.route('/')
def index():
	return (
		<pyx>
			<script>
				window.alert('Redirecting you to /home...')
				window.location.href = '/home'
			</script>
		</pyx>
	).html
