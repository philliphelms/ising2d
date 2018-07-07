import numpy as np

class ising2d:
    def __init__(self,lattice_size=(2,5),J=1.):
        self.lattice_size=lattice_size
        self.lattice=np.zeros((self.lattice_size[0],self.lattice_size[1]),dtype=int)
        self.J = J

    def initialize_guess(self):
        for i in range(self.lattice_size[0]):
            for j in range(self.lattice_size[1]):
                self.lattice[i,j] = np.floor(np.random.rand(1)+0.5)

    def flip_spin(self,ix,iy):
        self.lattice[ix,iy]=1-self.lattice[ix,iy]

    def all_flip(self):
        self.lattice = np.ones(self.lattice.shape,dtype=int)-self.lattice

    def find_pairs(self):
        self.interaction_inds = []
        for i in range(self.lattice_size[0]-1):
            for j in range(self.lattice_size[1]-1):
                # Interact to the right
                self.interaction_inds.append(((i,j),(i+1,j)))
                # Interact below
                self.interaction_inds.append(((i,j),(i,j+1)))
    
    def actual_spin(self,spin):
        return 2*(spin-0.5)

    def energy(self):
        E = 0.
        for i in range(len(self.interaction_inds)):
            spin1 = 2*self.lattice[self.interaction_inds[i][0]]-1
            spin2 = 2*self.lattice[self.interaction_inds[i][1]]-1
            E -= self.J*spin1*spin2
        return E
