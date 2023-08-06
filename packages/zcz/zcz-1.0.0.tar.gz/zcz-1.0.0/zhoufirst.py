"""这是周长智写的第一个python模块"""
def print_cz(the_list, level=0):
	"""This is the first python 
	   codes."""
	for each_item in the_list:
		if isinstance(each_item, list):
			print_cz(each_item, level+1)
		else:
			for i in range(level):
				print('\t',end='')
			print(each_item)