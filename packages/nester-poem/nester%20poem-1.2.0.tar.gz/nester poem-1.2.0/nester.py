"""This is the standard way to include a multiple - line comment in your code ."""
def print_lol(the_list,level):

    for each_item in the_list:

        if isinstance(each_item,list ):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range (level):
                print("\t",end = '')
            print(each_item)    
