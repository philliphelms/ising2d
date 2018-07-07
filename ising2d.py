
import numpy as np
class ising2d :
    def __init__(self,lattice_size=10) :
        self.lattice_size=lattice_size
        self.lattice=np.zeros((self.lattice_size,self.lattice_size),dtype=int)

    def initialize_guess(self):
        for i in range(self.lattice_size):
            for j in range(self.lattice_size):
                self.lattice[i,j] = np.floor(np.random.rand(1)+0.5)

    def flip_spin(self,ix,iy) :
        self.lattice[ix,iy]=1-self.lattice[ix,iy]

    def energy(self):

