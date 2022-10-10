from pysite.tags import *

def mybutton(data: str, children=None, onclickjs: str="", id: str=""):
	return (
		html('\n\t\t', [button(data, [], **{'class': 'mybutton','id': id,'onclick': onclickjs})], **{})	)