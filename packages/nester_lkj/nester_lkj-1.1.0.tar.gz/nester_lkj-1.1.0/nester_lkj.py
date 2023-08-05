"""
这是一个"nester_lkj.py"模块，提供了一个名为print_lol()的函数
用来打印列表，其中包含或不包含嵌套列表
"""
def print_lol(the_list,indent=False,level=0):
"""
这个函数有一个位置参数，"the_list",这可以是任何python列表(包含或不包含嵌套列表)
第二个参数为控制是否显示嵌套列表制表符
第三个参数"level"用来在遇到嵌套列表时插入制表符
"""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="")
            print(each_item)
