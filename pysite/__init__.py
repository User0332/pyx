class Element:
	def __init__(self, tag: str, data: str="", children: list=None, **attrs: str,):
		self.tag = tag
		self.data = data
		self.children = children if children else []
		self.attrs = attrs

	@property
	def html(self) -> str:
		return str(self)

	def __str__(self):
		attrs = ""
		children = '\n'.join(str(child) for child in self.children)

		for attrname, value in self.attrs.items():
			attrs+=f'{attrname}="{value}" '

		return f"<{self.tag} {attrs}>{self.data}{children}</{self.tag}>"

def read_cdf(filename: str) ->  str:
	with open(filename, 'r') as f:
		code = f.read()

	