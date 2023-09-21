import sys

file = open(sys.argv[1], "r");
output = open("gets_sets_"+ sys.argv[1].split(".")[0] + ".txt", "w")
for line in file:
	line = line[0:-2 if line[-1] == "\n" else -1]
	parameter = line.split(" ")
	output.write("\tpublic " + parameter[0] + " get" + parameter[1].capitalize() + "()\n\t{\n\t\treturn this." + parameter[1] + ";\n\t}\n\n")
	output.write("\tpublic void set" + parameter[1].capitalize() + "(" + parameter[0] + " value)\n\t{\n\t\tthis." + parameter[1] + " = value;\n\t}\n\n")

output.close()