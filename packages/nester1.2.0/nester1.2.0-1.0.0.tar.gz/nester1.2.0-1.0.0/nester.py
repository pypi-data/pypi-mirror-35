import sys
"""
遞歸循環
"""
def print_lol(the_list,level=0):
    '''
    這個含數有一個位置參數,名為the_list
    這可以是任何PYTHON列表(包含或不包含堑套列表)
    所提供列表中的各個數據項會(遞歸地)打印到屏幕上,而且各佔一行
    :param the_list:
    :param lvl:
    :return:
    '''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print('\t',end='')
            print(each_item)










