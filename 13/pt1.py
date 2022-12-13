filename = "input.txt"
# filename = "example.txt"

def split_outermost_arr(text):
	outer_commas = list([-1])
	inside_brackets = 0
	for i, char in enumerate(text):
		# print(i, char)
		if(char == "["): inside_brackets+=1
		elif(char == "]"): inside_brackets-=1
		elif(char == "," and inside_brackets == 0): 
			outer_commas.append(i)
	outer_commas.append(len(text))
	# print(outer_commas)
	out = list()
	for i,comma in enumerate(outer_commas[1:]):
		out.append(text[outer_commas[i]+1:comma])
	out = list(filter(lambda x: x!='', out))
	return out

def compare(left, right):
	# return true if in the right order, false if in the wrong order
	# return None if inconclusive
	# print(left, right)
	if(left.startswith("[") and right.startswith("[")):
		# print("A", left, right)
		left_arr = split_outermost_arr(left[1:-1])
		right_arr = split_outermost_arr(right[1:-1])
		for lind, lval in enumerate(left_arr):
			if(lind >= len(right_arr)): return False
			possible_return = compare(lval, right_arr[lind])
			if(possible_return != None): return possible_return
		if(len(left_arr) < len(right_arr)): return True
	elif(left.startswith("[") or right.startswith("[")):
		# print("B", left, right)
		if(left.startswith("[")): right = "[{}]".format(right)
		else: left = "[{}]".format(left)
		return compare(left, right)
	else:
		# print("C", left, right)
		left = int(left)
		right = int(right)
		if(left < right): return True
		elif(left > right): return False
		else: return None
with open(filename, "r") as f:
	left = f.readline().strip()
	right = f.readline().strip()
	line = f.readline()
	index = 1
	correctly_ordered = list()
	while line:
		# print("{} vs {}".format(left, right))
		if(compare(left,right)): correctly_ordered.append(index)
		left = f.readline().strip()
		right = f.readline().strip()
		line = f.readline()
		index += 1

print(sum(correctly_ordered))