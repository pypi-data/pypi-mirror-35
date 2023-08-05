import sys
def print_lol(the_list,indent=False,level=0,fn = sys.stdout):
    for each in the_list:
        if isinstance(each,list):
            print_lol(each,indent,level+1,fn)
        else:
            if indent:
            	for heihei in range(level):
                    print("\t",end='',file = fn)
            print(each,file = fn)
