#!/usr/bin/python3
# Author --Yassine Hachami

def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
