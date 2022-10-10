from pysite import Element

class MyButton(Element):
	def __init__(self, text: str, onclickjs: str):
		super().__init__("button", text, onclick=onclickjs)