import sys
outfile = open(sys.argv[1],'w')

for line in sys.stdin:
	fields = line.strip().split()
	if len(fields)<6:
		continue
	chrom = fields[0]
	pos = fields[1]
	ref = fields[2].upper()
	profile1 = fields[4].upper()
	if ref =="A":
		alt = "G"
	elif ref == "T":
		alt = "C"
	else:
		print "error"
		continue
	outline = '\t'.join([chrom,pos,str(profile1.count(alt)),str(profile1.count(alt)+profile1.count('.')+profile1.count(','))])+'\n'
	outfile.write(outline)

outfile.close()
