
"""
递归打印嵌套列表
"""

def print_lol(the_list, level=0, indent=False):
    """ 参数the_list为可嵌套的列表 """
    for item in the_list:
        if isinstance(item,list):
            print_lol(item, level+1, indent)
        else:
            if indent:
                for tab in range(level):
                    print("\t", end="")
            print(item)

