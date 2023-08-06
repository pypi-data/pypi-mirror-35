"""这是本人写的第二个Python模块"""
def print_hh(the_list, level=0):
    for each in the_list:
        if isinstance(each, list):
            print_hh(each, level+1)
        else:
            for i in range(level):
                print('\t', end='')
            print(each)