filename = "input.txt"
# filename = "example.txt"

def count_faces(cubes, c):
	exposed = 0
	if((c[0],c[1],c[2]+1) not in cubes): exposed+=1
	if((c[0],c[1],c[2]-1) not in cubes): exposed+=1
	if((c[0],c[1]+1,c[2]) not in cubes): exposed+=1
	if((c[0],c[1]-1,c[2]) not in cubes): exposed+=1
	if((c[0]+1,c[1],c[2]) not in cubes): exposed+=1
	if((c[0]-1,c[1],c[2]) not in cubes): exposed+=1
	return exposed



cubes = set()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		c = [int(x) for x in line.split(",")]
		cubes.add((c[0], c[1], c[2]))
		line = f.readline().strip()

total = 0
for cube in cubes:
	total+= count_faces(cubes, cube)
print(total)