import numpy as np
##
# \brief     Module containing class for 2d Ising Calculations
# \author    Phillip Helms
# \date      July 2018
# \details
# This module is the main class in this simple program, which uses the 
# Metropolis algorithm to study the 2D Ising Model.
# 
# The code is not complete as it is primarily being used as a forum to 
# practice various programming skills such as Test Driven Development (TDD),
# Pair Programming, Continuous Integration (via Travis), 
# and Documentation (via Doxygen).
# 
# To run a 2D ising model calculation:
# ```
# from ising2d import *
#
#
# # Initialize ising2d object
# ising = ising2d(lattice_size=(15,15),J=1.0,beta=100.)
#
# # Find all nearest neighbors
# ising.find_pairs()
#
# # Initialize random guess
# ising.initialize_guess()
#
# # Run MC Calculations
# Energy = ising.run_mc(niter=100)
# ```
class ising2d:
    ## The constructor for the ising2d object
    # \param self The ising2d object pointer
    # \param lattice_size A length 2 tuple containing the \f$(Nx,Ny)\f$ dimensions of the lattice.
    # \param J The interaction parameter in the ising model
    # \param beta \f$1/(kT)\f$
    def __init__(self,lattice_size=(10,10),J=1.,beta=0.5):
        ## The Lattice Size
        # (A length-2 tuple)
        self.lattice_size=lattice_size
        ## A numpy array of ints containing the current lattice configuration
        self.lattice=np.zeros((self.lattice_size[0],self.lattice_size[1]),dtype=int)
        ## The interaction parameter in the ising model
        self.J = J
        ## The inverse temperature \f$1/(kT)\f$
        self.beta = beta
        ## A count of the number of metropolis steps that have been performed
        self.itercnt = 0

    ## Initialize a random guess for the Monte Carlo Calculation
    # \param self The ising2d object pointer
    def initialize_guess(self):
        for i in range(self.lattice_size[0]):
            for j in range(self.lattice_size[1]):
                self.lattice[i,j] = np.floor(np.random.rand(1)+0.5)

    ## Flip the spin at a given lattice site either from up to down or the inverse.
    # \param self The ising2d object pointer
    # \param ix The x-coordinate for the desired lattice site
    # \param iy The y-coordinate for the desired lattice site
    def flip_spin(self,ix,iy):
        self.lattice[ix,iy]=1-self.lattice[ix,iy]

    ## Flip all of the spins in the lattice
    # \param self The ising2d object pointer
    def all_flip(self):
        self.lattice = np.ones(self.lattice.shape,dtype=int)-self.lattice

    ## Make a list containing all nearest neighbor sites in the lattice
    # \param self The ising2d object pointer
    def find_pairs(self):
        ## A list of the nearest neighbor pairs within the system
        # For a given entry in the list, self.interaction_inds[i]
        # gives, in tuples, the x- and y-coordinates for the first 
        # and second interacting sites, i.e. \f$\left(\left(x_1,y_1\right),\left(x_2,y_2\right)\right)\f$
        self.interaction_inds = []
        for i in range(self.lattice_size[0]-1):
            for j in range(self.lattice_size[1]-1):
                # Interact to the right
                self.interaction_inds.append(((i,j),(i+1,j)))
                # Interact below
                self.interaction_inds.append(((i,j),(i,j+1)))
    
    ## Return (+/-) 1 for the spin
    # \param self The ising2d object pointer
    # \param spin The spin of a site as stored in the lattice, i.e. 0 -> Spin-Down, 1 -> Spin-up
    # \return Spin The actual spin of the system, i.e. -1 -> Spin-Down, 1 -> Spin-up
    def actual_spin(self,spin):
        return 2*(spin-0.5)

    ## Calculating energy of the current configuration as specified in lattice by
    # looping over all nearest neighbor interactions contained in interaction_inds
    # \param self The ising2d object pointer
    # \return E The Energy of the current spin configuration
    def energy(self):
        E = 0.
        for i in range(len(self.interaction_inds)):
            spin1 = 2*self.lattice[self.interaction_inds[i][0]]-1
            spin2 = 2*self.lattice[self.interaction_inds[i][1]]-1
            E -= self.J*spin1*spin2
        return E

    ## Select a random site \f$(x,y)\f$, usually for flipping
    # \param self The ising2d object pointer
    # \return \f$(x,y)\f$ The x and y coordinate for a random site in the lattice
    def select_random_site(self):
        return np.random.randint(self.lattice_size[0]), np.random.randint(self.lattice_size[1])

    ## Determine whether a change should be kept or rejected 
    # via the criteria:
    # \f${rand()} > e^{\beta\left(E_{prev}-E_{curr}\right)}\f$
    # \param self The ising2d object pointer
    # \return keep True if the state should be kept, False if it should be discarded
    def keep_change(self):
        random_comp = np.random.rand()
        E_diff = self.energy_prev-self.energy_curr
        return random_comp > np.exp(self.beta*E_diff)

    ## Execute a single Metropolis step
    # 
    # 1. Determine initial energy
    # 2. Flip a random site
    # 3. Determine energy of new configuration
    # 4. Check if change should be kept, and keep or revert the change accordingly
    # \param self The ising2d object pointer
    def single_mc_step(self):
        ## The energy of the previous configuration
        self.energy_prev = self.energy()
        ix,iy = self.select_random_site()
        self.flip_spin(ix,iy)
        ## The energy of the current configuration
        self.energy_curr = self.energy()
        if not self.keep_change():
            self.flip_spin(ix,iy)
            self.energy_curr = self.energy()
        self.itercnt += 1

    ## Run niter Monte Carlo Metropolis steps
    # Performs niter steps of the Metropolis Monte Carlo algorithm 
    # to try to determine the ground state of the 2d Ising Model. 
    # The energy of the final configuration is returned. 
    # \param self The ising2d object pointer
    # \param niter The number of desired metropolis steps (de
    # \return E Energy of the final configuration
    def run_mc(self,niter=1000):
        for i in range(niter):
            self.single_mc_step()
            print(self.energy_curr)
        return self.energy_curr
