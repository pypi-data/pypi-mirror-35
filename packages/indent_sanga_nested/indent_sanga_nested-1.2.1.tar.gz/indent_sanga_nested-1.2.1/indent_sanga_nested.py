def nester_indent(given_list, indent = False, level = 0):
    for each_item in given_list:
        if isinstance(each_item,list):
            nester_indent(each_item, indent, level+1)
        else:
            if indent == True:
                for tab_stop in range(level):
                    print("\t", end = '')
            print(each_item)
