filename = "input.txt"
# filename = "example.txt"
x = 1
cycle = 0
sums = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		cycle+=1
		if((cycle-20) % 40 == 0):
			sums += x*cycle
		if(line.split(" ")[0] == "addx"):
			val = int(line.split(" ")[1])
			cycle+=1
			if((cycle-20) % 40 == 0):
				sums += x*cycle
			x += val
		line = f.readline().strip()
print(sums)