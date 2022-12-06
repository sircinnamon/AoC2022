filename = "input.txt"
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		for i in range(4, len(line)):
			segment = line[i-4:i]
			if(len(set(segment)) == 4):
				print("{} at {}".format(segment, i))
				quit()
		line = f.readline().strip()