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
            self.assertTrue(Eg<=Ee)

    def test_flip_energy(self):
        ising = ising2d()
        ising.find_pairs()
        E1=ising.energy()
        ising.all_flip()
        E2=ising.energy()
        self.assertTrue(E1==E2)

    def test_select_random_site(self):
        # This should be able to test whether we are selecting a random x and y point in the lattice
        ising = ising2d()
        ix,iy = ising.select_random_site()
        self.assertTrue(type(ix) is int)
        self.assertTrue(type(iy) is int)
        self.assertTrue(ix<ising.lattice_size[0])
        self.assertTrue(ix<ising.lattice_size[1])
        self.assertTrue(ix>=0)
        self.assertTrue(iy>=0)

    def test_energy_difference(self):
        ising = ising2d()
        ising.energy_prev = 1.
        ising.energy_curr = 1.
        result = ising.keep_change()
        self.assertFalse(result)
        
    def test_single_metropolis_step(self):
        # Run a single full flip with accept/reject, check that only one or zero spins has changed
        ising = ising2d()
        ising.find_pairs()
        ising.initialize_guess()
        initial_lattice = ising.lattice.copy()
        initial_itercnt = ising.itercnt
        ising.single_mc_step()
        final_lattice = ising.lattice.copy()
        final_itercnt = ising.itercnt
        # Check that only one spin at most has been changed
        diff = np.sum(np.sum(np.abs(initial_lattice-final_lattice)))
        self.assertTrue((diff == 0) or (diff == 1))
        # Check that iter increased by 1
        self.assertTrue(final_itercnt-initial_itercnt is 1)

    def test_niter(self):
        ising = ising2d()
        ising.find_pairs()
        ising.initialize_guess()
        E = ising.run_mc(niter=1000)
        self.assertEqual(1000,ising.itercnt)
                
if __name__ == "__main__":
    unittest.main()
