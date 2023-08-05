# -*- coding: utf-8 -*-

"""Main module."""

class converter():

    def array_to_string(array):
        temp = []
        for i in array:
            temp.append(str(i))
        return "".join(temp)
    
    def string_to_array(string):
        return list(string)
