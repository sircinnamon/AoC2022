filename = "input.txt"

elves = list()
elf_index = 0
with open(filename, "r") as f:
	line = f.readline()
	while line:
		if(line=="\n"):
			elf_index = elf_index+1
		else:
			val = 0
			if(len(elves) <= elf_index):
				elves.append(0)
			else:
				val = elves[elf_index]
			elves[elf_index] = val + int(line)
		line = f.readline()

# print(elves)
print(max(elves)) # Part 1 answer
# print(elves.index(max(elves)))

tops = list([0,0,0])
for elf in elves:
	min_e = min(tops)
	if(elf > min_e): tops.pop(tops.index(min_e)); tops.append(elf)
# print(tops)
print(sum(tops)) # Part 2 Answer
