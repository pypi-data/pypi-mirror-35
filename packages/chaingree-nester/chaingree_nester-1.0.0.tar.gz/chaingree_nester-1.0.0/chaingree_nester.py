#coding=utf-8
"""注释：
提供一个print_lol()函数用来打印列表，其中包含或不包含嵌套列表
"""

def print_lol(the_list,indent=False,level=0):
    for item in the_list:
        if isinstance(item,list):
            print_lol(item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(item)
