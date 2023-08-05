'''这是一个"nesterliz001.py"文件提供了一个名为print——lol()的函数，这个函数的作用是打印列表，其中有可能
包含（也可能不包含）嵌套列表。'''
#name = ['john' , 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]

def print_lol(the_list, indent=False, level=0, space=sys.stdout):
	'''这个函数取一个位置参数，名为'the_list'，这可以是任何pytho列表（也可以是包含嵌套列表的列表）。所指定的列表中的每个数据项会（递归地）输出到屏幕上，各数据项各占一行，且在遇到新的列表是自动缩进,'''
	
#增加了space参数，是print_lol()可以被调用
	for each_item in the_list:
			if isinstance(each_item, list):
				print_lol(each_item, indent, level+1, space )
			else:
				if indent:
					for tab_stop in range(level):
						print("\t",end='', file=space)
				print(each_item, file=space)


#print_lol(name,True)

