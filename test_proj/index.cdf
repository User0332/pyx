Element(
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