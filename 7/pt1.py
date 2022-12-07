import re
filename = "input.txt"
cd_cmd = r'^\$ cd (.*)$'
ls_cmd = r'^\$ ls$'
files = {}
curr_dir = "/"

def seek(files, path):
	keys = path.split("/")
	out = files
	for k in keys:
		if(k==""):continue
		out = out[k]
	return out

def sum_folder(fdict):
	total = 0
	for item in fdict.values():
		if(type(item) is dict):
			total += sum_folder(item)
		else:
			total += item
	return total

def sum_all_folders(fdict):
	sizes = list()
	sizes.append(sum_folder(fdict))
	for item in fdict.values():
		if(type(item) is dict):
			sizes += sum_all_folders(item)
	return sizes

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		if "$" in line:
			if re.match(cd_cmd, line):
				folder = re.match(cd_cmd, line)[1]
				if(folder == "/"):
					curr_dir = "/"
				elif (folder == ".."):
					curr_dir = "/".join(curr_dir.split("/")[:-1])
				else:
					curr_dir = curr_dir + "/" + folder
				line = f.readline().strip()
			elif(re.match(ls_cmd, line)):
				line = f.readline().strip()
				while("$" not in line and line):
					if(line.startswith("dir")):
						dirname = line.replace("dir ", "")
						curr_dir_dict = seek(files, curr_dir)
						if(dirname not in curr_dir_dict):
							curr_dir_dict[dirname] = {}
					else:
						filesize = int(line.split(" ")[0])
						filename = line.split(" ")[1]
						curr_dir_dict = seek(files, curr_dir)
						curr_dir_dict[filename] = filesize
					line = f.readline().strip()
# print(files)
# print(sum_all_folders(files))
print(sum(filter(lambda x: x<100000, sum_all_folders(files))))