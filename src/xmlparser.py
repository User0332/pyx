from html.parser import HTMLParser
from pysite.tags import Element

class PYXParser(HTMLParser):
	def __init__(self):
		self.document = Element("html")
		self.current_node: Element = self.document
		self.current_tag = ""
		super().__init__(convert_charrefs=True)

	def handle_starttag(self, tag: str, attrs: list[str]):
		dictattrs = {attr[0] : attr[1] for attr in attrs}
		self.current_tag = tag
		element = Element(tag, data="", children=None, **dictattrs)
		
		self.current_node.children.append(element)
		element.parent = self.current_node

		self.current_node = element

	def handle_endtag(self, tag: str):		
		if tag != self.current_tag:
			raise ValueError(f"The tag '{self.current_tag}' was never closed!")

		self.current_node = self.current_node.parent
		# self.current_node is already set to parent
		self.current_tag = self.current_node.tag

	def parse(self, feed):
		super().feed(feed)

		if self.current_node is not self.document or self.current_tag is not None:
			raise ValueError("A tag wasn't closed!")

	def handle_data(self, data):
		self.current_node.data = data
		