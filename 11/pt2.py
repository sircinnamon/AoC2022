import math
filename = "input.txt"
# filename = "example.txt"

class Monkey:
	def __init__(self, _id, inventory_text, operation_text, test_text, true_text, false_text):
		self.id = _id
		self.inventory = [int(x) for x in inventory_text.split(": ")[1].split(", ")]
		self.operation = "mul" if "*" in operation_text else "add"
		self.operation_value = operation_text.split(" ")[-1]
		self.test_val = int(test_text.split(" ")[-1])
		self.true_target = int(true_text.split(" ")[-1])
		self.false_target = int(false_text.split(" ")[-1])
		self.inspect_count = 0
		self.reduction_amount = 0

	def __str__(self):
		out = "Monkey {}:".format(self.id)
		out += "\n\tInventory: {}".format(self.inventory)
		out += "\n\tOperation: old {} {}".format(self.operation, self.operation_value)
		out += "\n\tTest: if mod {}, throw {} else throw {}".format(self.test_val, self.true_target, self.false_target)
		out += "\n\tActivity Count: {}".format(self.inspect_count)
		return out

	def operate(self, old):
		val = 0
		if(self.operation_value == "old"): val = old
		else: val = int(self.operation_value)

		if(self.operation == "mul"): val = old*val
		else: val = old+val

		# val = math.floor(val/3)
		val = val % self.reduction_amount
		return val

	def throw_target(self, val):
		self.inspect_count += 1
		if(val % self.test_val == 0):
			return self.true_target
		else: return self.false_target

	def catch_item(self, worry_level):
		self.inventory.append(worry_level)

monkeys = list()
with open(filename, "r") as f:
	line = f.readline()
	while line:
		while("Monkey" not in line): line = f.readline()
		m_id = len(monkeys)
		inv_line = f.readline().strip()
		op_text = f.readline().strip()
		test_text = f.readline().strip()
		true_text = f.readline().strip()
		false_text = f.readline().strip()
		m = Monkey(m_id, inv_line, op_text, test_text, true_text, false_text)
		monkeys.append(m)
		line = f.readline()

reduction_amount = 1
for x in [m.test_val for m in monkeys]:
	reduction_amount = reduction_amount*x
for m in monkeys: m.reduction_amount = reduction_amount

for round in range(10000):
	for m in monkeys:
		while len(m.inventory):
			item = m.inventory.pop(0)
			item = m.operate(item)
			catcher = m.throw_target(item)
			monkeys[catcher].catch_item(item)
	# print(round+1, [m.inventory for m in monkeys])

activity = [m.inspect_count for m in monkeys]
activity.sort()
print(activity[-1] * activity[-2])

