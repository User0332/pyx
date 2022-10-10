from pysite.tags import *

def mystyle(children=None):
	return (
		html('\n\t\t', [style('\n\t\t\t\t.mybutton {\n\t\t\t\t\tbackground-color: green;\n\t\t\t\t\tborder: 2px dotted blue;\n\t\t\t\t\tfont-size: 18px;\n\t\t\t\t\tcolor: red;\n\t\t\t\t\ttext-align: center;\n\t\t\t\t}\n\t\t\t', [], **{})], **{})	)