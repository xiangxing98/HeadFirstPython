# indent true, level = 0
def print_lol(a_list, indent=True, level=0):
    """Prints each item in a list, recursively descending
       into nested lists (if necessary)."""

    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1) # 3parameters
        else:
            if indent:
                for l in range(level):
                    print("\t", end='')
            print(each_item)

names = ['Qiang','Jason','Liang',['Stone','John','Abner',['Shi']],'Hou',['Stone']]
print_lol(names, 0)
print("-----------------new line-----------------")
# Qiang
# Jason
# Liang
# Stone
# John
# Abner
# Shi
# Hou
# Stone
# -----------------new line-----------------
print_lol(names, True, 0)
print("-----------------new line-----------------")
# Qiang
# Jason
# Liang
# 	Stone
# 	John
# 	Abner
# 		Shi
# Hou
# 	Stone
# -----------------new line-----------------

print_lol(names, True, 4)
print("-----------------new line-----------------")
# 				Qiang
# 				Jason
# 				Liang
# 					Stone
# 					John
# 					Abner
# 						Shi
# 				Hou
# 					Stone
# -----------------new line-----------------