def print_bhitra(given_list,level=0):
        for each_item in given_list:
                if isinstance(each_item,list):
                        print_bhitra(each_item,level+1)
                else:
                        for tab_stop in range(level):
                                print("\t", end = '')
                        print(each_item)
   
