# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
这是‘nester.py’模块，提供了一个名为print_lol()的函数，这个函数的作用是打印列表， 其中可能包含（也可能不包含）嵌套列表。
"""
def print_lol(the_list):
    """这个函数取一个位置参数，名为'the_list' ， 这可以是任何Python列表，所 指定的列表中的每个数据项会递归地输出到屏幕上"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)




