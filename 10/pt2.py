filename = "input.txt"
# filename = "example.txt"
x = 1
cycle = 0

def draw(sprite, cycle):
	# print(cycle, list(range(sprite-1,sprite+2)))
	if((cycle-1)%40 in range(sprite-1,sprite+2)):
		print("#", end="")
	else:
		print(".", end="")
	if(cycle % 40 == 0):
		print("")

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		cycle+=1
		draw(x,cycle)
		if(line.split(" ")[0] == "addx"):
			val = int(line.split(" ")[1])
			cycle+=1
			draw(x,cycle)
			x += val
		line = f.readline().strip()