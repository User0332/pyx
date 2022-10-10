from pysite.tags import *

def mybutton(data: str, children=None, onclickjs: str="", id: str=""):
	return (
		<pyx>
			<button class="mybutton" id={id} onclick={onclickjs}>{data}</button>
		</pyx>
	)