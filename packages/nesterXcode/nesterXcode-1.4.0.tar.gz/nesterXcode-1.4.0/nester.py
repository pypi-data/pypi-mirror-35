"""my first python module: a recursive function to display all lists nested in a list"""

def print_lol(the_list,indent=False,level=0):
    for each_list in the_list:
        if isinstance(each_list,list):
            print_lol2(each_list,indent,level+1)
        else:
                if indent:
                        for tab_stop in range(level):
                                print('\t', end='')
                                
                print(each_list)
