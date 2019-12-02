import random
import time
# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

    # init
    # nS maximum number of states
    # nA maximum number of action per state
    def __init__(self,nS,nA):

        # define this function
        self.nS = nS
        self.nA = nA
        self.Q = []
        self.visitedTimes = []
        for i in range(nS):
            self.Q.append([])
            self.visitedTimes.append([])
            for j in range(nA):
                self.Q[i].append(0)
                self.visitedTimes[i].append(0)
        self.alpha = 0.6
        self.discFactor = 1
        # define this function
              
        
    # Select one action, used when learning  
    # st - is the current state        
    # aa - is the set of possible actions
    # for a given state they are always given in the same order
    # returns
    # a - the index to the action in aa
    def selectactiontolearn(self,st,aa):
        # define this function
        # print("select one action to learn better")

        # Random Choice
        #nA = len(aa)
        #a = random.randint(0, nA-1)

        # Random Less Visited
        a = 0
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
        #print("State: " + str(st))
        #print("List of actions: " + str(aa))
        #print("List of Counters: " + str(self.visitedTimes[st]))
        #print('Next State: ' + str(aa[a]))
        #print(self.Q)
        #time.sleep(0.5)

        # Great Rewarded Value
        #a = 0


        return a

    # Select one action, used when evaluating
    # st - is the current state        
    # aa - is the set of possible actions
    # for a given state they are always given in the same order
    # returns
    # a - the index to the action in aa
    def selectactiontoexecute(self,st,aa):
        # define this function
        a = 0
        maxValue = self.Q[st][0]
        for actionIdx in range(len(aa)):
            if self.Q[st][actionIdx] > maxValue:
                maxValue = self.Q[st][actionIdx]
                a = actionIdx
        # print("select one action to see if I learned")
        return a


    # this function is called after every action
    # st - original state
    # nst - next state
    # a - the index to the action taken
    # r - reward obtained
    def learn(self,ost,nst,a,r):
        # define this function
        #print("learn something from this data")
        best = self.maxInd(self.Q[nst])
        self.Q[ost][a] += self.alpha*(r + self.discFactor*self.Q[nst][best] - self.Q[ost][a])
        return

    def maxInd(self, set):
        imax = 0
        m = set[0]
        for i in range(len(set)):
            if set[i] > m:
                m = set[i]
                imax = i
        return imax

