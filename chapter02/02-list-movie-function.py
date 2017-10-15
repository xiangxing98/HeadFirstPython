from nester import print_lol
movies = [
     'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
     ['Graham Chapman',
      ['Michael Palin', 'John Cleese','Terry Gilliam','Eric Idle','Terry Jones']]]

# def print_lol(the_list,indent=False,level=0,fh=sys.stdout)

print_lol(movies)
print("-----------------new line-----------------")
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# Graham Chapman
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle
# Terry Jones
# -----------------new line-----------------
print_lol(movies,0)
print("-----------------new line-----------------")
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# Graham Chapman
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle
# Terry Jones
# -----------------new line-----------------
print_lol(movies,True,0)
print("-----------------new line-----------------")
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# 	Graham Chapman
# 		Michael Palin
# 		John Cleese
# 		Terry Gilliam
# 		Eric Idle
# 		Terry Jones
# -----------------new line-----------------
print_lol(movies,True,-2)
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# Graham Chapman
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle
# Terry Jones