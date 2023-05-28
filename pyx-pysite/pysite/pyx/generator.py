from ..tags import Element

class PyCodeGenerator():
	def __init__(self, document: Element):
		self.document = document

	def generate(self, element: Element=None) -> str:
		element = element if element else self.document

		children = [self.generate(elem) for elem in element.children]
		attrs = (
			'{'+(
				','.join(
					f"{repr(name)}: {value}" 
					for name, value in element.attrs.items()
				)
			)+'}'
		)

		data = f"data={element.data}"

		return \
			f"{element.tag}({data+',' if element.data else ''} " \
				f"children=[{','.join(children)}], **{attrs})"