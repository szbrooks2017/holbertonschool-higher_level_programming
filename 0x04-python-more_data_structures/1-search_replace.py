#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def check_element(element):
        return (element if element != search else replace)
    newlist = [check_element(x) for x in my_list]
    return newlist
