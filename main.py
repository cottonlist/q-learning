from random import randint

learning_rate = 1
discount_factor = 0.8
epsilon = 0.1

class State:
	def __init__(self, id, left, right, trace, memory_log, terminal):
		self.id = id
		self.left = left
		self.right = right
		self.trace = trace
		self.memory_log = memory_log
		self.value = 0
		self.qvalue1 = 0
		self.qvalue2 = 0
		self.terminal = terminal
	def PrintTrace(self):
		print(self.trace)
	def PrintMemoryLog(self):
		print(self.memory_log)

def calculate_reward(state, action):
	if action == 1:
		next_state = state.left
	elif action == 2:
		next_state = state.right
	if state.memory_log == ['1W', '2W'] and next_state.memory_log == ['1W', '2W', '1R']:
		reward = 10
	else:
		reward = 0
	return reward

def epoch(x):
	if states[x].terminal == True:
		pass
	else:
		if states[x].left == None:
			action = 2
			states[x].qvalue2 = states[x].qvalue2 + learning_rate * (calculate_reward(states[x], action) + discount_factor * max(states[x].right.qvalue1, states[x].right.qvalue2) - states[x].qvalue2)
			epoch(states[x].right.id)
		elif states[x].right == None:
			action = 1
			states[x].qvalue1 = states[x].qvalue1 + learning_rate * (calculate_reward(states[x], action) + discount_factor * max(states[x].left.qvalue1, states[x].left.qvalue2) - states[x].qvalue1)
			epoch(states[x].left.id)
		else:
			action = randint(1, 2)
			if action == 1:
				states[x].qvalue1 = states[x].qvalue1 + learning_rate * (calculate_reward(states[x], action) + discount_factor * max(states[x].left.qvalue1, states[x].left.qvalue2) - states[x].qvalue1)
				epoch(states[x].left.id)
			elif action == 2:
				states[x].qvalue2 = states[x].qvalue2 + learning_rate * (calculate_reward(states[x], action) + discount_factor * max(states[x].right.qvalue1, states[x].right.qvalue2) - states[x].qvalue2)
				epoch(states[x].right.id)

state_0 = State(0, None, None, 0, [], False)
state_1 = State(1, None, None, 1, ["1W"], False)
state_2 = State(2, None, None, 2, ["2W"], False)
state_3 = State(3, None, None, 11, ["1W", "1R"], False)
state_4 = State(4, None, None, 12, ["1W", "2W"], False)
state_5 = State(5, None, None, 21, ["2W", "1W"], False)
state_6 = State(6, None, None, 112, ["1W", "1R", "2W"], True)
state_7 = State(7, None, None, 121, ["1W", "2W", "1R"], True)
state_8 = State(8, None, None, 211, ["2W", "1W", "1R"], True)
		
# state_8 = State(8, None, None, 211, ["2W", "1W", "1R"], True)
# state_7 = State(7, None, None, 121, ["1W", "2W", "1R"], True)
# state_6 = State(6, None, None, 112, ["1W", "1R", "2W"], True)
# state_5 = State(5, state_8, None, 21, ["2W", "1W"], False)
# state_4 = State(4, state_7, None, 12, ["1W", "2W"], False)
# state_3 = State(3, None, state_6, 11, ["1W", "1R"], False)
# state_2 = State(2, state_5, None, 2, ["2W"], False)
# state_1 = State(1, state_3, state_4, 1, ["1W"], False)
# state_0 = State(0, state_1, state_2, 0, [], False)

states = [state_0, state_1, state_2, state_3, state_4, state_5, 
state_5, state_6, state_7, state_8]

for i in states:
	for j in states:
		if j.trace - i.trace * 10 == 1:
			i.left = j
		elif j.trace - i.trace * 10 == 2:
			i.right = j


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

for m in range(1,100):
	x = randint(0, 8)
	epoch(x)

for n in range(0,8):
	print("State", n, "Q-value 1", states[n].qvalue1, "Q-value 2", states[n].qvalue2)

# print(states[2].left.trace)
# re = calculate_reward(states[4], 1)
# print(re)

# states[1].right.PrintTrace()
# states[8].PrintMemoryLog()