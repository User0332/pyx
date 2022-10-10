from pysite.tags import *

def mybutton(data: str, children=None, onclickjs: str="", id: str=""):
	return (
		html(data='\n\t\t', children=[button(data=data, children=[], **{'class': 'mybutton','id': id,'onclick': onclickjs})], **{})	)