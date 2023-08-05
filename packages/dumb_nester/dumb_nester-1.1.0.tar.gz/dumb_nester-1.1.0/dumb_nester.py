def print_lol(the_list,val):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,val+1)
        else:
             for tab_stop in range(val):
                print("\t",end='')
             print(each_item)

