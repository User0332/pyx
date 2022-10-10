import pysite
from flask import Flask, render_template_string
from pysite.tags import *


app = Flask(__name__)
app.debug = True

def create_index() -> str:
	return (
		<head>
			<title>My Site!</title>
		</head>
		<body>
			<h1>Welcome to my site!</h1>
			<button onclick="alert('button clicked')">Click Me!</button>
		</body>
	).html

@app.route('/')
def index():
	return render_template_string(
		create_index()
	)
