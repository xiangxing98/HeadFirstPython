# Modified By Stone Hou @ 1017-10-15
# 首选yapf unify code format
# python - m pip install yapf
# python - m pip install autopep8
# python - m pip install pep8ify

movies = ['The Holy Grail', 'The Life of Brian', 'The meaning of life1']

# the 2nd movie of the list
print(movies[1])
# The Life of Brian

# the movie list
print(movies)
# ['The Holy Grail', 'The Life of Brian', 'The meaning of life1']

print(len(movies))
# 3

# print string contains " or ' 单引号和双引号的区别
print("Hello 'world")
# Hello 'world

print('Hello "world')
# bash: syntax error near unexpected token `('

# Another advanced Example
cast = ['Clesese', 'Palin', 'Jones', 'Idle']
print(cast)
# ['Clesese', 'Palin', 'Jones', 'Idle']

# appped will add a word at the end of the list
cast.append('Gmail')
print(cast)
# ['Clesese', 'Palin', 'Jones', 'Idle', 'Gmail']

# pop() will pop the last word
print(cast.pop())
# Gmail

print(cast)
# now go back to baseline/startline
# ['Clesese', 'Palin', 'Jones', 'Idle']

# pop(0) will pop the 1st word
print(cast.pop(0))
# 1st word Clesese pop
# Clesese

print(cast)
# ['Palin', 'Jones', 'Idle']

# extend can add a new list
cast2 = ['Yahoo', 'Chapman']
cast.extend(cast2)
print(cast)
# ['Palin', 'Jones', 'Idle', 'Yahoo', 'Chapman']

# insert before position 0
cast.insert(0, 'Fox')
print(cast)
# ['Fox', 'Palin', 'Jones', 'Idle', 'Yahoo', 'Chapman']

# Excise 1 insert years after the movie name
movies = ['The Holy Grail', 'The Life of Brian', 'The meaning of life']
print(movies)
# ['The Holy Grail', 'The Life of Brian', 'The meaning of life']
movies.insert(1, 1975)
movies.insert(3, 1979)  # after insert 1975, the length of movies changed
movies.append(1983)
print(movies)
# ['The Holy Grail', 1975, 'The Life of Brian', 1979, 'The meaning of life',
#  1983]

# Excise 1 create new list
movies2 = [
    'The Holy Grail', 1975, 'The Life of Brian', 1979, 'The meaning of life',
    1983
]
print(movies2)

# deal with the data in the list

# 1. print each var position [x]
fav_movies = ['The Holy Grail', 'The Life of Brian']
print(fav_movies[0])
# The Holy Grail
print(fav_movies[1])
# The Life of Brian

# 2. print iteration via for
fav_movies = ['The Holy Grail', 'The Life of Brian']
for each_flick in fav_movies:
    print(each_flick)
# The Holy Grail
# The Life of Brian

# 3. print via while
fav_movies = ['The Holy Grail', 'The Life of Brian']
count = 0
while count < len(fav_movies):
    print("List Element", count, ": ", fav_movies[count])
    count = count + 1
# List Element 0 :  The Holy Grail
# List Element 1 :  The Life of Brian

# List in List
print("-----------------new line-----------------")
movies = [
    'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
    [
        'Graham Chapman',
        [
            'Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle',
            'Terry Jones'
        ]
    ]
]
print(movies[4][1][3])  # shows Eric Idle
# Eric Idle

print(movies)
# ['The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
# ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam',
# 'Eric Idle', 'Terry Jones']]]

for each_movie in movies:
    print(each_movie)  # 这里只能打印第一层的列表
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam',
# 'Eric Idle', 'Terry Jones']]

# if element is list, handle and do something
# else print out directly
# print list in list
print("-----------------isinstance()-----------------")
movies = [
    'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
    [
        'Graham Chapman',
        [
            'Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle',
            'Terry Jones'
        ]
    ]
]

# Build In Function isinstance
print(isinstance(movies, list))
# True
print(isinstance(movies[4], list))
# True

# print 2nd level instance
movies = [
    'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
    [
        'Graham Chapman',
        [
            'Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle',
            'Terry Jones'
        ]
    ]
]
print("-----------------isinstance()-----------------")
for each_item in movies:
    if isinstance(each_item, list):
        for each_subitem in each_item:  # 添加语句后可以打印到第二层
            print(each_subitem)
    else:
        print(each_item)
print("-----------------new line-----------------")
# -----------------isinstance()-----------------
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# Graham Chapman
# ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
# -----------------new line-----------------

# print 3rd level instance
movies = [
    'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
    [
        'Graham Chapman',
        [
            'Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle',
            'Terry Jones'
        ]
    ]
]
print("-----------------new line-----------------")
for each_item in movies:
    if isinstance(each_item, list):
        for each_subitem in each_item:
            if isinstance(each_subitem, list):  # 继续添加语句可以打印到第三层
                for each_ssubitem in each_subitem:
                    print(each_ssubitem)
            else:
                print(each_subitem)
    else:
        print(each_item)
print("-----------------new line-----------------")

# -----------------new line-----------------
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


# 重复的代码用函数代替
def print_lol(the_list):
    print("-----------------Function Start-----------------")
    for each_item in the_list:
        if (isinstance(each_item, list)):
            print_lol(each_item)  # 这个递归函数真不赖
        else:
            print(each_item)


movies = [
    'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
    [
        'Graham Chapman',
        [
            'Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle',
            'Terry Jones'
        ]
    ]
]

print_lol(movies)
print("-----------------new line End-----------------")
# -----------------Function Start-----------------
# The Holy Grail
# 1975
# Terry Jones&Terry Gilliam
# 91
# -----------------Function Start-----------------
# Graham Chapman
# -----------------Function Start-----------------
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle
# Terry Jones
# -----------------new line End-----------------
