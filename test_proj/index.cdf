html(
	children=[
		head(
			children=[
				title("My Site!")
			]
		),
		body(
			children=[
				h1("Welcome to my site!"),
				button(
					"Click Me!", 
					onclick="alert('button clicked')"
				)
			]
		)
	]
)