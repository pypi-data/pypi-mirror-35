from AlbotOnline.QueueFlowServiceControl.Simulation import *
import random

#Random choosen consts
A_MIN = 0.2; A_MAX = 0.8; B_MIN = 0.1; B_MAX = 0.9
QUEUE_SIZE = 100


#Do some clever decision making here. Instead of a random decision
def flowControl(queue, queueSize, bMin, bMax):
    return bMax if random.random() > 0.5 else bMin

#Do some clever decision making here. Instead of a random decision
def serviceControl(queue, queueSize, aMin, aMax):
    # Do some clever decision making here. Instead of a random decision
    return aMin if random.random() > 0.5 else aMax

#Instansiate a version of the simulator
sim = Simulation(queueSize=QUEUE_SIZE, aMin=A_MIN, aMax=A_MAX, bMin=B_MIN, bMax=B_MAX,
                 flowControl=flowControl, serviceControl=serviceControl
                 )

#Running 100 iterations of the simulation and printing the values
for i in range(100):
    postState = sim.tick()

    print("***********")
    print("Round: ", i)
    print("Wait Cost:", postState.totalWaitCost)
    print("Flow Cost:", postState.totalFlowCost)
    print("Service Cost:", postState.totalServiceCost)
    print("Objects in Queue:", postState.currentQueue)
    print("Queue Size:", postState.queueSize)