def print_lol(a_list, level=0):
    """Prints each item in a list, recursively descending
       into nested lists (if necessary)."""

    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for l in range(level):
                print("\t", end='')
            print(each_item)

# veryfi
names = ['Qiang','Jason','Liang',['Stone','John','Abner',['Shi']],'Hou',['Stone']]
print_lol(names, 0)
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

print_lol(names)
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
print_lol(names, 2)
print("-----------------new line-----------------")
# 2 tabs
# 		Qiang
# 		Jason
# 		Liang
# 			Stone
# 			John
# 			Abner
# 				Shi
# 		Hou
# 			Stone
# -----------------new line-----------------

print_lol(names, -2)
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

for i in range(4):
    print(i)

for i in range(-4):
    print(i)