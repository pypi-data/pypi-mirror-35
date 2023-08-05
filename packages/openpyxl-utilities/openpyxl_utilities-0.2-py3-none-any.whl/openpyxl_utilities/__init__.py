from shutil import get_terminal_size
from openpyxl.worksheet.worksheet import Worksheet, Cell
import string

name = "openpyxl_utilities"

#	Given a row of cells (a column works too), returns a list of said cells' values
def list_row_values(row):
	return [cell.value for cell in row]

#	Given a worksheet, will adjusts it's columns' widths to fit the longest cell's content. Max and min column width can be given.
def adjust_col_width(ws, min_width=8, max_width=30):
	widths = []
	for col in ws.columns:
		max_lenght = max_lenght_of_column(col)

		ws.column_dimensions[col[0].column].width = max(min((max_lenght + 1), max_width), min_width)

	return widths


#	Given a worksheet, will print it's cells on screen.
def print_sheet(ws, offset=0, print_top=True, print_side=True, spacing=1, exclude_columns=[], beg_column=0, end_column=0):
	for c in exclude_columns:
		if isinstance(c, int):
			c = num_to_col(c)
		elif c.isdigit():
			c = num_to_col(int(c))

	if beg_column > end_column:
		raise ValueError("Begining column must be before ending column.")

	if beg_column < 0 or end_column < 0:
		raise ValueError("Begining and/or ending columns can't be negative.")

	def print_hr(character, end):
		if print_side:
			print(character * side_width, end=chr(449))
		else:
			print(chr(449), end="")

		if offset:
			print("<", end="")

		for w in cols_to_print_w:
			print(character * (w+1), end=end)
		if overflow:
			print("\b>")
		else:
			print("")


	overflow = False

	cols_to_print = []
	console_width = get_terminal_size()[0] - 1
	if print_side:
		side_width = len(str(ws.max_row)) + 1
		width_to_print = 1 + side_width
	else:
		width_to_print = 0
	if offset:
		width_to_print += 1
	columns = []
	cols_to_print_w = []
	letters_to_print = []
	for col in ws.columns:
		columns.append((list(col), col[0].column))

	#while beg_column < 0:
	
	while width_to_print < console_width and len(columns) > (offset+beg_column):
		column, letter = columns.pop(offset)
		if letter not in exclude_columns:
			cols_to_print.append(column)
			width = max_lenght_of_column(column)
			width_to_print += ( width + 3)
			cols_to_print_w.append(width)
			letters_to_print.append(letter)		

	if len(columns) > offset:
		overflow = True
		cols_to_print.pop()
		width_to_print -= (cols_to_print_w.pop() +3)
		letters_to_print.pop()

	rows_to_print = transpose(cols_to_print)

	print(("Worksheet: " + ws.title).center(width_to_print - len(cols_to_print) , "="))

	if print_top:
		if print_side:
			print(" " * side_width, end=chr(449))
		else:
			print("|", end="")

		if offset:
			print("<", end="")

		for letter, width in zip(letters_to_print, cols_to_print_w):
			print(letter.center(width + 1, " "), end="|")
		if overflow:
			print("\b>")
		else:
			print("")
		print_hr("=","+")



	i = 1
	for row in rows_to_print:
		if not empty_row(row):
			if print_side:
				print(str(i).ljust(side_width," "), end=chr(449))
				i+=1
			else:
				print("|", end="")

			if offset:
				print("<", end="")

			for cell, width in zip(row, cols_to_print_w):
				if cell.value != None:
					print(str(cell.value).ljust(width, " "), end=" |")
				else:
					print(" " * (width+1), end="|")
			if overflow:
				print("\b>")
			else:
				print("")
			print_hr("-", "+")


#	Given a row, returns True if all it's cells are empty.
def empty_row(row):
	empty = True
	for cell in row:
		if cell.value != None:
			empty=False
	return empty


#	Given a column, will return the length (in number of characters) of the cell with the  longest length in the column.
def max_lenght_of_column(col):
	width = 0
	for cell in col:
		try: 
			if len(str(cell.value)) > width:
				width = len(str(cell.value))
		except:
			pass
	return width


#	Given a matrix, returns the transpose of said matrix.
def transpose(cols):
	rows = []
	for i in range(len(cols[0])):
		row = []
		for col in cols:
			row.append(col[i])
		rows.append(row)
	return rows


#	Given a sheet, will sort the sheet's rows depending of the said row's value (first row by default) in ascending order (by default). The headers (first row) will
#	remain static by default.
def sort_sheet_by(ws, column_of_order=0, descending=False, fixed_headers=True):
	s_ws = Worksheet(ws.parent, title=ws.title)
	rows = list(ws.rows)
	if fixed_headers:
		s_ws.append(list_row_values(rows.pop(0)))

	for row in sorted(rows, key=lambda x: x[column_of_order].value, reverse=descending):
		s_ws.append(list_row_values(row))

	wb.remove(ws)
	wb.copy_worksheet(s_ws)
	wb.active.title = ws.title


#	Applies a given format (font, fill and or border) to all the cells from a given worksheet. If a different format is desired for the headers (first row)
#	h_font, h_fill, h_border can be used.
def apply_format(ws, font=None, fill=None, border=None, h_font=None, h_fill=None, h_border=None):
	is_headers = True
	if font or fill or border or h_font or h_fill or h_border:
		for row in ws.rows:
			for cell in row:
				if is_headers:
					if h_font:
						cell.font = h_font
					elif font:
						cell.font = font
					
					if h_fill:
						cell.fill = h_fill
					elif fill:
						cell.fill = fill
					
					if h_border:
						cell.border = h_border
					elif border:
						cell.border = border				
				else:
					if font:
						cell.font = font
					if fill:
						cell.fill = fill
					if border:
						cell.border = border
			is_headers = False


def col_to_num(col):
	if isinstance(col, int):
		return col
	elif col.isdigit():
		return col_to_num(int(col))
	num = 0
	for c in col:
		if c in string.ascii_letters:
			num = num * 26 + (ord(c.upper()) - ord('A')) + 1
		else:
			raise ValueError("Column name must be either letters or numbers.")
	return num

def num_to_col(n):
	if isinstance(n, int):
		s = ""
		while n > 0:
			n, remainder = divmod(n - 1, 26)
			s = chr(65 + remainder) + s
		return s
	elif n.isdigit(): 
		return num_to_col(int(n))
	else:
		return n
	
