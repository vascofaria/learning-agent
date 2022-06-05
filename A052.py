# Grupo 52, Bruno Meira (89421), Vasco Faria (89559)

import random

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment

class LearningAgent:

	# init
	# nS maximum number of states
	# nA maximum number of action per state
	def __init__(self,nS,nA):
		self.nS = nS+1
		self.nA = nA
		self.Q = []
		self.visitedTimes = []
		for i in range(nS):
			self.Q.append([])
			self.visitedTimes.append([])
		self.alpha = 0.6
		self.gamma = 0.9

	# Select one action, used when learning
	# st - is the current state        
	# aa - is the set of possible actions
	# for a given state they are always given in the same order
	# returns
	# a - the index to the action in aa
	def selectactiontolearn(self,st,aa):
		# print("select one action to learn better")
		a = 0

		if len(self.Q[st]) == 0:
			for i in range(len(aa)):
				self.Q[st].append(0)
				self.visitedTimes[st].append(0)

		# ------Random Choice-----
		#nA = len(aa)
		#a = random.randint(0, nA-1)

		# -----Random Less Visited-----
		minValue = self.visitedTimes[st][0]
		for visIdx in range(len(aa)):
		    if self.visitedTimes[st][visIdx] < minValue:
		        minValue = self.visitedTimes[st][visIdx]
		        a = visIdx
		minList = []
		cnt = 0
		for i in range(len(aa)):
		    if self.visitedTimes[st][i] == minValue:
		        minList.append(i)
		        cnt += 1
		a = minList[random.randint(0, cnt-1)]
		self.visitedTimes[st][a] += 1

		# -----Great Rewarded Value-----
		#maxValue = self.Q[st][0]
		#for ind in range(len(aa)):
		#    if self.Q[st][ind] > maxValue:
		#        maxValue = self.Q[st][ind]
		#        a = ind
		#maxList = []
		#cnt = 0
		#for i in range(len(aa)):
		#    if self.Q[st][i] == maxValue:
		#        maxList.append(i)
		#        cnt += 1
		#a = maxList[random.randint(0, cnt-1)]

		return a

	# Select one action, used when evaluating
	# st - is the current state        
	# aa - is the set of possible actions
	# for a given state they are always given in the same order
	# returns
	# a - the index to the action in aa
	def selectactiontoexecute(self,st,aa):
		# print("select one action to see if I learned")

		if len(self.Q[st]) == 0:
			for i in range(len(aa)):
				self.Q[st].append(0)
				self.visitedTimes[st].append(0)

		a = 0
		maxValue = self.Q[st][0]
		for actionIdx in range(len(aa)):
			if self.Q[st][actionIdx] > maxValue:
				maxValue = self.Q[st][actionIdx]
				a = actionIdx
		maxList = []
		cnt = 0
		for actionIdx in range(len(aa)):
			if self.Q[st][actionIdx] == maxValue:
				maxList.append(actionIdx)
				cnt += 1
		a = maxList[random.randint(0, cnt-1)]

		return a


	# this function is called after every action
	# st - original state
	# nst - next state
	# a - the index to the action taken
	# r - reward obtained
	def learn(self,ost,nst,a,r):
		#print("learn something from this data")
		if len(self.Q[nst]) != 0:
			best_ind = 0
			maxValue = self.Q[nst][0]
			for i in range(len(self.Q[nst])):
				if self.Q[nst][i] > maxValue:
					maxValue = self.Q[nst][i]
					best_ind = i

			self.Q[ost][a] += self.alpha*(r + self.gamma*self.Q[nst][best_ind] - self.Q[ost][a])
		else:
			self.Q[ost][a] += self.alpha*(r - self.Q[ost][a])

		return
