from sys import argv
from typing import Literal, Union
from ..tags import Element
from .generator import PyCodeGenerator
from .xmlparser import PYXParser

def main():
	file: str = argv[1]

	with open(file, 'r') as f:
		code = f.read()

	new_code = ""
	in_double_quote_str = False
	in_single_quote_str = False
	in_esc_code = False
	in_pyx = False
	current_pyx_start: int = None
	pyx_idxs: list[tuple[int, int]] = []
	pyx_blocks: list[str] = []

	def check_start_pyx(code: str, i: int) -> bool:
		if code[i:i+5] == "<pyx>": return True
		return False

	def check_end_pyx(code: str, i: int) -> bool:
		if code[i:i+6] == "</pyx>": return True
		return False

	def strchecker(char: Union[Literal["'"], Literal['"']]) -> int:
		if char == '"':
			if in_double_quote_str and in_esc_code:
				return -1
			if not in_double_quote_str:
				return 1
			
			return 0

		if char == "'":
			if in_single_quote_str and in_esc_code:
				return -1
			if not in_single_quote_str:
				return 1
			
			return 0

	obj = enumerate(code)
	for i, char in obj:
		if in_esc_code:
			in_esc_code = False
			continue

		if (char in ('"', "'")) and (not in_pyx):
			val = strchecker(char)
			if (val == -1): continue

			if in_esc_code:
				in_esc_code = False

			elif char == '"':
				in_double_quote_str = val

			elif char == "'":
				in_single_quote_str = val

		if (char == '\\') and (in_double_quote_str or in_single_quote_str):
			if in_esc_code:
				if not in_pyx: continue
			else:
				in_esc_code = 1

		if char == '<' and not (in_double_quote_str or in_single_quote_str):
			if not in_pyx:
				res = check_start_pyx(code, i)

				if res:
					current_pyx_start = i
					for i in range(5): next(obj)

					in_pyx = True
					pyx_blocks.append("")
				
				continue

			res = check_end_pyx(code, i)

			if res:
				pyx_idxs.append(
					(current_pyx_start, i+7)
				)

				for i in range(7): next(obj)

				in_pyx = False

		if in_pyx:
			pyx_blocks[-1]+=char
			continue

	documents: list[Element] = []

	for block in pyx_blocks:
		parser = PYXParser()
		parser.parse(block)
		documents.append(
			parser.document
		)

	pycodes = [PyCodeGenerator(document).generate() for document in documents]

	prevend = 0

	for i, pycode in enumerate(pycodes):
		start = pyx_idxs[i][0]
		end = pyx_idxs[i][1]

		new_code+=code[prevend:start]
		new_code+=pycode

		prevend = end

		if i == len(pycodes)-1:
			new_code+=code[end:]

	if not new_code: new_code = code

	with open('.'.join(argv[1].split('.')[:-1])+".py", 'w') as f:
		f.write(new_code)

if __name__ == "__main__":
	main()