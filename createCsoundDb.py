inputFile = open("opcodes.txt")
outputFile = open("db/csound.json", 'w')
outputFile.write("{\n")

for line in inputFile:
	tokens = line.split(";")
	#entry name
	entry = "\t"+tokens[0] + ": {\n"
	#descr
	entry = entry+"\t\t\"descr\": \""+tokens[2][1:-1].translate(None, "\"")+"\",\n"
	#name
	entry = entry+"\t\t\"name\": "+tokens[0]+",\n"
	#params
	entry = entry+"\t\t\"params\": [],\n"
	#path
	entry = entry+"\t\t\"path\": \"csound/"+tokens[0][1:-1]+".html\",\n"
	#syntax
	entry = entry+"\t\t\"syntax\": \""+tokens[3][1:-1].translate(None, "\"")+"\",\n"
	#type
	entry = entry+"\t\t\"type\": "+tokens[1]+"\n"
	entry = entry+"\t},\n"
	outputFile.write(entry)
	

outputFile.write("}")
outputFile.close()
#now sort out trailing ,
inputFile = open("csound.json")
dbFile = inputFile.readlines()
numberOfLines = len(dbFile)

dbFile[numberOfLines-2] = "\t}\n"

outputFile = open("csound.json", 'w')

for lines in dbFile:
  outputFile.write("%s" % lines)

outputFile.close()
inputFile.close()

