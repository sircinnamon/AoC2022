filename = "input.txt"
# filename = "example.txt"

head_pos=(0,0)
tail_pos=(0,0)
visited_pos = set()
visited_pos.add((0,0))

moves = {
	"R": (1,0),
	"U": (0,1),
	"D": (0,-1),
	"L": (-1,0)
}

def need_tail_move(head_pos, tail_pos):
	if(abs(head_pos[0]-tail_pos[0])>1):
		return True
	elif(abs(head_pos[1]-tail_pos[1])>1):
		return True
	return False

def calc_move(head_pos, tail_pos):
	move = (0,0)
	if(head_pos[0]>tail_pos[0]):
		move=(1,move[1])
	elif(head_pos[0]<tail_pos[0]):
		move=(-1,move[1])
	if(head_pos[1]>tail_pos[1]):
		move=(move[0],1)
	elif(head_pos[1]<tail_pos[1]):
		move=(move[0],-1)
	return move


with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		move = moves[line.split(" ")[0]]
		count = int(line.split(" ")[1])
		for i in range(count):
			head_pos = (head_pos[0]+move[0],head_pos[1]+move[1])
			if(need_tail_move(head_pos,tail_pos)):
				tail_mov = calc_move(head_pos, tail_pos)
				tail_pos = (tail_pos[0]+tail_mov[0],tail_pos[1]+tail_mov[1])
			visited_pos.add(tail_pos)
		line = f.readline().strip()

print(len(visited_pos))