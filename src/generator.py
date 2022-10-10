from pysite.tags import Element

class PyCodeGenerator():
	def __init__(self, document: Element):
		self.document = document

	def generate(self, element: Element=None) -> str:
		element = element if element else self.document

		children = [self.generate(elem) for elem in element.children]

		return \
			f"{element.tag}({element.data!r}, " \
				f"[{','.join(children)}], **{element.attrs})"