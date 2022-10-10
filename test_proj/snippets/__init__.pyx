from pysite.tags import *

def mystyle(children=None):
	return (
		<pyx>
			<style>
				.mybutton {
					background-color: green;
					border: 2px dotted blue;
					font-size: 18px;
					color: red;
					text-align: center;
				}
			</style>
		</pyx>
	)