import pysite
from flask import Flask, render_template_string
from pysite import Element
from components.button import MyButton

app = Flask(__name__)

def create_index() -> str:
	document = Element(
		"html",
		children=[
			Element(
				"head", 
				children=[
					Element("title", "My Site!")
				]
			),
			Element(
				"body",
				children=[
					Element(
						"h1", 
						"Welcome to my site!"
					),
					MyButton(
						"Click Me!", 
						"alert('button clicked')"
					)
				]
			)
		]
	)

	return document.html

@app.route('/')
def index():
	return render_template_string(
		create_index()
	)
