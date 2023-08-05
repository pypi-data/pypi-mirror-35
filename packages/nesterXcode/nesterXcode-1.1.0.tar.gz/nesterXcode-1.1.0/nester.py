"""my first python module: a recursive function to display all lists nested in a list"""

def print_lol2(the_list):
	for each_list in the_list:
		if isinstance(each_list,list):
			print_lol2(each_list)
		else:
			print(each_list)
