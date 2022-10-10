from . import tags

def read_cdf(filename: str, **components: type[tags.Element]) -> tags.Element:
	with open(filename, 'r') as f:
		code = f.read()

	try:
		return eval(
			code,
			{
				**components,
				**{
					name: element for name, element in tags.__dict__.items() 
					if name not in ('_', "standard_tags")
				}
			}
		)
	except BaseException as e:
		raise ValueError(
			f"Invalid CDF!\nPerhaps you forgot to include a kwarg to a component definition?\nError: {e}"
		)