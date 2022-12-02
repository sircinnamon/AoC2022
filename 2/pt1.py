filename = "input.txt"
total_score = 0
scores = {
	"A": 1,
	"B": 2,
	"C": 3
}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		o = line.split(" ")[0]
		p = line.split(" ")[1]
		p = p.replace("X","A")
		p = p.replace("Y","B")
		p = p.replace("Z","C")
		if(o == p): total_score += 3 + scores[p]
		else:
			if (o == "C" and p == "A"): total_score += 6+1 
			elif (o == "A" and p == "B"): total_score += 6+2 
			elif (o == "B" and p == "C"): total_score += 6+3
			else: total_score += scores[p] 
		line = f.readline().strip()

print(total_score) # part 1