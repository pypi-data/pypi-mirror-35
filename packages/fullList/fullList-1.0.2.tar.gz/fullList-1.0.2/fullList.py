"""This module allows to print ALL list objects even with nested lists.
The second argument 'indent' allows for use of default behavior without indentation.
The third argument 'level' sets number of TAB stops at each line."""
def print_all(some_list, indent=False, level=0):
    """This function iterates thru some list and, if meets nested lists, prints its objects too"""
    for index in some_list:
        if isinstance(index,list):
            print_all(index,indent,level+1)
        else:
            if indent:
                for tab in range(level):
                    print("\t",end='')
            print(index)
