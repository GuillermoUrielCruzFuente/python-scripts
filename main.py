# install dependecies with pip
import pyperclip

def replace_breaklines_with_spaces(text):
	text_with_no_breaklines = ''

	for line in text:
		temp_line = line.rstrip() + " "
		text_with_no_breaklines += temp_line

	return text_with_no_breaklines

def reset_file(file_path):
	file = open(file_path, mode="w")
	file.write("")
	file.close()

# open txt file with utf-8 encoding
# make sure to use the correct encoding
text_file = open("text.txt", encoding="utf-8")

normalized_text = replace_breaklines_with_spaces(text_file)

text_file.close()

pyperclip.copy(normalized_text)

reset_file("text.txt")
