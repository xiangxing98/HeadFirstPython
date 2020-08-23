

### Exception Handling vs Extra Code

> What does each block of code do?


Extra Code:

- imports os
- checks if the path to and the file actually exist
- if the file exist open the file
	- go through all lines in data.
	- if there is a ":" colon in the line
		- put first part of line in role
		- second in line_spoken
		- print role
		- print said
		- print line_spoken
	- close file

- if there is no file with that name print: the file is missing



Exception:

- if any code inside the try fails do what the exception contains
	- open file
	- go through every line in file
		- if any code inside try fails go to inner except: divide line with :, into role and line_spoken
		- print role
		- print said
		- print line_spoken
		
				
	- except:
		- skip to next line  




- except: print the datafile is missing
