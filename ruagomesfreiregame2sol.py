import random

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
        self.Q = [[0]*nA]*nS
        self.visitedTimes = [[0]*nA]*nS
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
        #nA = len(aa)
        #a = random.randint(0, nA-1)
        a = 0
        minValue = 9999
        for visIdx in range(len(aa)):
            if self.Q[st][visIdx] < minValue:
                minValue = self.Q[st][visIdx]
                a = visIdx
        # define this function
        self.visitedTimes[st][a] += 1
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
        maxValue = -1
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
        m =-1
        for i in range(len(set)):
            if set[i] > m:
                m = set[i]
                imax = i
        return imax

