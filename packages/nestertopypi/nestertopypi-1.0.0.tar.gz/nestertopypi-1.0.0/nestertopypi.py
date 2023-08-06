"""这是nester.py模块，提供名为print_lol（）的函数，函数作用是打印（嵌套）列表"""
def print_lol(the_list):
        for i in the_list:
                if isinstance(i,list):
                        print_lol(i)
                else:
                        print(i)
