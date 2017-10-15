import pickle
from nester import print_lol
man = []
other = []
try:
    data = open('sketch.txt') #打开文件
    for each_line in data:#遍历文件
        try:
            (role,line_spoken) = each_line.split(':',1) #将每行按照:分成2部分
            line_spoken = line_spoken.strip()#去除多余空格
            if role == 'Man':#如果role是man, 把line_spken 压入man list
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()#关闭I/O
except IOError:
    print('The data file is missing!')

try:
    with open('man_data4.txt','wb') as out_man,open('other_data4.txt','wb') as out_other:
         pickle.dump (man,out_man)
         pickle.dump (other,out_other)

except IOError as err:
    print('File Error: '+str(err))

except pickle.PickleError as prr:
    print('Pickle Error: '+str(prr))

new_man=[]
try:
     with open ('man_data4.txt','rb') as man_file:
          new_man = pickle.load(man_file)
except IOError as err:
     print('File Error: '+str(err))
except pickle.PickleError as prr:
     print('Pickle Error: '+str(prr))

print_lol (new_man)
