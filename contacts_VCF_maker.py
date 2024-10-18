file = open("Untitled 1.txt")
outfile = open('Contacts.vcf', 'w')
s = file.readlines()
for line in s:
	line2 = line.split(', ')
	for e in line2:
		outfile.write('BEGIN:VCARD\n')
		outfile.write('N:;;;;\n')
		outfile.write('FN:\n')
		if e.startswith('9989') or e.startswith('9983'):
			outfile.write('TEL;TYPE=CELL:+'+e+'\n')
		else:
			outfile.write('TEL;TYPE=CELL:'+e+'\n')
		outfile.write('END:VCARD\n')
outfile.close()