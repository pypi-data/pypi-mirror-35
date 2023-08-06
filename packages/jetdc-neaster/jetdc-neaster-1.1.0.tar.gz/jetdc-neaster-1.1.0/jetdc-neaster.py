"""练习1，函数定义"""
def print_lol(the_list, level=0):
 """列表打印函数"""
 for each_item in the_list:
  if isinstance(each_item, list):
   print_lol(each_item, level)
  else:
   for tab_stop in range(level+1):
    print("\t",end='')
   print(each_item)
