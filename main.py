from random import randint

class State:
	def __init__(self, id, left, right, trace, memory_log, leaf):
		self.id = id
		self.left = left
		self.right = right
		self.trace = trace
		self.memory_log = memory_log
		self.reward = 0
		self.leaf = leaf
	def PrintTrace(self):
		print(self.trace)
	def PrintMemoryLog(self):
		print(self.memory_log)

def calculate_reward(state, action):
	if action == 1:
		next_state = state.left
	elif action == 2:
		next_state = state.right
	if next_state.memory_log == ['1W', '2W', '1R']:
		reward = 20
	else:
		reward = 0
	return reward

def epoch(x):
	if states[x].leaf == True:
		states[x].reward = 0
	else:
		if states[x].left == None:
			action = 2
			states[x].reward = calculate_reward(states[x], action) + states[x].right.reward
			epoch(states[x].right.id)
		elif states[x].right == None:
			action = 1
			states[x].reward = calculate_reward(states[x], action) + states[x].left.reward
			epoch(states[x].left.id)
		else:
			action = randint(1, 2)
			if action == 1:
				states[x].reward = calculate_reward(states[x], action) + states[x].left.reward
				epoch(states[x].left.id)
			elif action == 2:
				states[x].reward = calculate_reward(states[x], action) + states[x].right.reward
				epoch(states[x].right.id)
		
state_8 = State(8, None, None, 211, ["2W", "1W", "1R"], True)
state_7 = State(7, None, None, 121, ["1W", "2W", "1R"], True)
state_6 = State(6, None, None, 112, ["1W", "1R", "2W"], True)
state_5 = State(5, state_8, None, 21, ["2W", "1W"], False)
state_4 = State(4, state_7, None, 12, ["1W", "2W"], False)
state_3 = State(3, None, state_6, 11, ["1W", "1R"], False)
state_2 = State(2, state_5, None, 2, ["2W"], False)
state_1 = State(1, state_3, state_4, 1, ["1W"], False)
state_0 = State(0, state_1, state_2, 0, [], False)

states = [state_0, state_1, state_2, state_3, state_4, state_5, 
state_5, state_6, state_7, state_8]

# for i in range(0, 8):
# 	for j in range (1, 8):
# 		if states[i].trace * 10 + 1 == states[j].trace:
# 			states[i].left = states[j]
# 		elif states[i].trace * 10 + 2 == states[j].trace:
# 			states[i].right = states[j]

# for x in range(1,10):
# 	print(randint(0, 8))

# print(states[6].reward)

# epoch(5)

# x = randint(0, 8)

for m in range(1,50):
	x = randint(0, 8)
	epoch(x)

for n in range(0,8):
	print(n, states[n].reward)

# print(states[2].left.trace)
# re = calculate_reward(states[4], 1)
# print(re)

# states[1].right.PrintTrace()
# states[8].PrintMemoryLog()