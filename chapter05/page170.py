
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename): 
	try:
		with open(filename) as f:
			data = f.readline() 
		return(data.strip().split(','))
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

james = get_coach_data('chapter05/james.txt')
julie = get_coach_data('chapter05/julie.txt')
mikey = get_coach_data('chapter05/mikey.txt')
sarah = get_coach_data('chapter05/sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
# ['2.01', '2.22', '2.34']
# ['2.11', '2.23', '2.59']
# ['2.22', '2.38', '2.49']
# ['2.18', '2.25', '2.39']
