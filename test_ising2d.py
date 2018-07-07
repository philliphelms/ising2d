import unittest
from ising2d import *

class ising_2d_test(unittest.TestCase):

    def test_lattice_size_shape(self):
        ising = ising2d()
        self.assertEqual(len(ising.lattice_size),2)

    def test_spin_matrix_shape(self):
        ising=ising2d()
        self.assertEqual(ising.lattice_size[0],ising.lattice.shape[0])
        self.assertEqual(ising.lattice_size[1],ising.lattice.shape[1])

    def test_initialization(self) :
        ising=ising2d()
        ising.initialize_guess()
        for i in range(ising.lattice_size[0]) :
            for j in range(ising.lattice_size[1]) :
                spin=ising.lattice[i,j]
                self.assertEqual(((spin==0) or (spin==1)),True)

    def test_flip_single_spin(self):
        ising = ising2d()
        ising.initialize_guess()
        # Select random x and y coordinate
        indx = np.random.randint(ising.lattice_size[0])
        indy = np.random.randint(ising.lattice_size[1])
        # Check initial state
        initial_state = ising.lattice[indx,indy]
        # Flip Spin
        ising.flip_spin(indx,indy)
        # Check final state
        final_state = ising.lattice[indx,indy]
        if initial_state is 1:
            self.assertEqual(final_state,0)
        elif initial_state is 0:
            self.assertEqual(final_state,1)

    def test_ferromagnetic_energy(self) :
        ising = ising2d()
        ising.find_pairs()
        Eg=ising.energy()
        for i in range(10) :
            ising.initialize_guess()
            Ee=ising.energy()
            print(Eg)
            print(Ee)
            self.assertTrue(Eg<=Ee)

#    def test_flip_energy(self):
#        E1=ising.energy()
#        ising.all_flip()
#        E2=ising.energy()
#        self.assertTrue(E1==E2)
                
                
if __name__ == "__main__":
    unittest.main()


