
"""
递归打印嵌套列表
"""

def print_lol(the_list):
    """ 参数the_list为可嵌套的列表 """
    for item in the_list:
        if isinstance(item,list):
            print_lol(item)
        else:
            print(item)