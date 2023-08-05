"""This module allows to print ALL list objects even with nested lists"""
def print_all(some_list):
    """This function iterates thru some list and, if meets nested lists, prints its objects too"""
    for index in some_list:
        if isinstance(index,list):
            print_all(index)
        else:
            print(index)
