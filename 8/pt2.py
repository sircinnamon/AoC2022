filename = "input.txt"
grid=[]
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append([int(x) for x in line])
		line = f.readline().strip()

def score_view(height, view):
	score = 0
	# print("{} {}".format(height, view))
	for x in view:
		if x<height:
			score+=1
			max_seen = x
		else:
			score+=1
			return score
	return score


max_score = 0
for row_ind, row in enumerate(grid):
	for col_ind, tree in enumerate(row):
		col = [x[col_ind] for x in grid]
		# print("{}x{} = {}".format(row_ind, col_ind, tree))
		if(row_ind!=0 and col_ind != 0 and row_ind != len(grid)-1 and col_ind != len(row)-1):
			left = row[:col_ind]
			right = row[col_ind+1:]
			left.reverse()
			up = col[:row_ind]
			down = col[row_ind+1:]
			up.reverse()
			score = score_view(tree,right)*score_view(tree,left)*score_view(tree,up)*score_view(tree,down)
			max_score = max(max_score, score)
		
print(max_score)