filename = "input.txt"
grid=[]
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append([int(x) for x in line])
		line = f.readline().strip()

tree_count = 0
for row_ind, row in enumerate(grid):
	for col_ind, tree in enumerate(row):
		col = [x[col_ind] for x in grid]
		# print("{}x{} = {}".format(row_ind, col_ind, tree))
		if(row_ind==0 or col_ind == 0 or row_ind == len(grid)-1 or col_ind == len(row)-1):
			tree_count+=1
		elif(max(row[:col_ind]) < tree):
			tree_count+=1
		elif(max(row[col_ind+1:]) < tree):
			tree_count+=1
		elif(max(col[:row_ind]) < tree):
			tree_count+=1
		elif(max(col[row_ind+1:]) < tree):
			tree_count+=1
print(tree_count)