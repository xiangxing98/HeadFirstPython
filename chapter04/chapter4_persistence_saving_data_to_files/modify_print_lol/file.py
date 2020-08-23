
import nester

man     = []
other   = []



try:
    data = open('sketch.txt')
for each_line in data:
                try:
                        (role, line_spoken) = each_line.split(':', 1)
                        line_spoken = line_spoken.strip()
			if role == 'Man':
                                man.append(line_spoken)
                        elif role == 'Other':
                                other.append(line_spoken)

			with open('man_data.txt', 'w') as man_file:
				nester.print_lol(man, file=man_file)

                        with open('other_data.txt', 'w') as other_file:
                                nester.print_lol(other, file=other_file)
		except ValueError:
			pass
except IOError as err:
	print('File error: ' + str(err))







