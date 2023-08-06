def print_bhitra(given_list,level):
	for each_item in given_list:
		if isinstance(each_item,list):
			print_bhitra(each_item,level=0)
		else:
			for tab_stop in range(level):
				print("\t")
	print(each_item)
