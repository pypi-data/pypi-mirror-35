import random

class Simulation:

    def __init__(self, queueSize, aMin, aMax, bMin, bMax, flowControl, serviceControl):
        self.flowControl = flowControl
        self.serviceControl = serviceControl

        self.queueSize = int(queueSize)
        self.queue = 0
        self.flowCost = 0
        self.serviceCost = 0
        self.waitCost = 0

        self.aMin = aMin
        self.aMax = aMax
        self.bMin = bMin
        self.bMax = bMax

    def tick(self):
        if(self._canAddMoreJobs()):
            B = self.flowControl(self.queue, self.queueSize, self.bMin, self.bMax)
            self._addFlowCost(B)
            self._addJobb(B)

        self._addCurrentWaitCost()
        if(self._canServeJobs()):
            A = self.serviceControl(self.queue, self.queueSize, self.aMin, self.aMax)
            self._addServiceCost(A)
            self._serveJob(A)

        return self.getStateVector()


    def getStateVector(self):
        vec = lambda: None
        vec.totalWaitCost = self.waitCost
        vec.totalFlowCost = self.flowCost
        vec.totalServiceCost = self.serviceCost
        vec.currentQueue = self.queue
        vec.queueSize = self.queueSize
        return vec

    def _addCurrentWaitCost(self):
        self.waitCost += self.queue

    #Flow Controller
    def _canAddMoreJobs(self):
        return self.queue < self.queueSize

    def _addJobb(self, B):
        if(random.random() >= B):
            self.queue += 1

    def _addFlowCost(self, B):
        self.flowCost += B



    #Service Controller
    def _canServeJobs(self):
        return self.queue > 0

    def _serveJob(self, A):
        if(random.random() >= A):
            self.queue -= 1

    def _addServiceCost(self, A):
        self.serviceCost += A