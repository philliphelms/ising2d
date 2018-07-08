import numpy as np

class ising2d:
    def __init__(self,lattice_size=(10,10),J=1.,beta=0.5):
        self.lattice_size=lattice_size
        self.lattice=np.zeros((self.lattice_size[0],self.lattice_size[1]),dtype=int)
        self.J = J
        self.beta = beta
        self.itercnt = 0

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

    def select_random_site(self):
        return np.random.randint(self.lattice_size[0]), np.random.randint(self.lattice_size[1])

    def keep_change(self):
        random_comp = np.random.rand()
        E_diff = self.energy_prev-self.energy_curr
        return random_comp > np.exp(self.beta*E_diff)

    def single_mc_step(self):
        self.energy_prev = self.energy()
        ix,iy = self.select_random_site()
        self.flip_spin(ix,iy)
        self.energy_curr = self.energy()
        if not self.keep_change():
            self.flip_spin(ix,iy)
        self.itercnt += 1

    def run_mc(self,niter=1000):
        for i in range(niter):
            self.single_mc_step()
            print(self.energy_curr)
        return self.energy_curr
