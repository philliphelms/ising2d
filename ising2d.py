
import numpy as np
class ising2d :
    def __init__(self,lattice_size=10) :
        self.lattice_size=lattice_size
        self.lattice=np.zeros((self.lattice_size,self.lattice_size),dtype=int)
