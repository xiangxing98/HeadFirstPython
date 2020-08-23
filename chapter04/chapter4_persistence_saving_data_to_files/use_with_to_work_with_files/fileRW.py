
man     = []
other   = []



try:
	man_file = open('man_data.txt', 'w')
	other_file = open('other_data.txt', 'w')

	print(man, file=man_file)
	print(other, file=other_file)
except IOError as err:
	print('File error: ' + str(err))

finally:
	if 'man_file' in locals():
		man_file.close()
	
	if 'other_file' in locals():
		other_file.close()
