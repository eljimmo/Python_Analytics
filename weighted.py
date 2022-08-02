import numpy as np
import math

ratio=[0.20, 0.25, 0.35,0.10, 0.10]
rates=[7.5, 8.5, 8, 5, 6]
def weighted_average(ratio,rates):
    wa=0
    for i in range(len(ratio)):
        wa= wa+ ratio[i]*rates[i]
    print("Weighted Average returns: ",wa)
    
    weighted_average(ratio,rates)
