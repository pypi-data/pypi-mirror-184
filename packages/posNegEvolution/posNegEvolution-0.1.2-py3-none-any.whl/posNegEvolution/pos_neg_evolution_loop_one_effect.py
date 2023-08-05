import numpy as np
import math
import itertools
import scipy as sc
import copy
from threading import Thread
from multiprocessing import Pool

def death(iPop, pdt):
    return iPop[pdt,:]
    
def divide(iPop, pdv):
    return sc.sparse.vstack([iPop, copy.deepcopy(iPop[pdv,:])]).tocsr()
    
def mutate(iPop, pdm, mut_effect):
    cells = len(pdm)
    if cells == 0:
        return iPop
    (a,b) = iPop._shape
    rows = copy.deepcopy(iPop[pdm,:]).toarray()
    rows[:, 0] = rows[:, 0]*(1+abs(mut_effect))**(1 - 2*(mut_effect < 0))
    rows[:, 1] = rows[:, 1] + 1
    iPop = sc.sparse.vstack([iPop, rows]).tocsr()
    (c,d) = iPop._shape
    return iPop

def deleteZeroColumn(iPop):
    mask = np.ones(iPop._shape[1], dtype=bool)
    for i in range(iPop._shape[1]):
        _sum = (iPop[:,i]).count_nonzero()
        if _sum == 0:
            mask[i] = False
    return iPop[:,mask]

def posNegEvolutionLoopOneEffect(iPop, cap, tau, mut_prob, mut_effect, resume, lmbd):
    """    
    Description:
        One cycle to update population - tau loop iteration method
        Prameters:
            iPop: population matrix 
                One row represents one cell
                Fitness, [Mutations] (in not VAF apprach mutation number (pos and neg))
            cap: population capacity
            tau: tau step
            mut_prob: list in form of: [driver mutation probability, passenger mutation probability]
            mut_effect: list in form of: [driver mutation effect, passenger muatation effect]
            resume: acknowledge to resume simulation !!TODO!!
            q: common queue
            THREADS: threads number used in simulation !!TODO!!            
    """
    popSize = iPop._shape[0]
    
    mdt = popSize/cap
    mdv = iPop[:,0].toarray()[:,0]
    
    pdt = np.random.exponential(1, popSize)/mdt
    pdv = np.random.exponential(1, popSize)
    pdm = np.random.binomial(1, mut_prob[0], popSize)
    pdm = np.random.binomial(1, mut_prob[0], popSize)
    
    pdt = pdt > tau
    pdv = pdv/mdv < tau
    pdm = pdm > np.zeros(popSize)
    
    pdv = pdv & pdt
    pdm = pdm & pdv
    pdv[pdm] = False
    
    nr = np.array(range(popSize))
    pdv = nr[pdv]
    pdt = nr[pdt]
    pdm = nr[pdm]
    
    iPop = divide(iPop, pdv)
    
    iPop = mutate(iPop, pdm, mut_effect[0]) 
    
    pdt = np.append(pdt, range(max(pdt)+1, iPop._shape[0]))
    iPop = death(iPop, pdt)
    
    # iPop = deleteZeroColumn(iPop)
    
    return iPop