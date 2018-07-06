import unittest
from ising2d import *

class ising_2d_test(unittest.TestCase):
    def test_spin_matrix_shape(self):
        ising=ising2d()
        self.assertEqual(ising.lattice_size,ising.lattice.shape[0])
        self.assertEqual(ising.lattice_size,ising.lattice.shape[1])
#    def test_initialization(self) :
#        ising=ising2d()
#        ising2d.initialize()
        
#        self.lattice
if __name__ == "__main__":
    unittest.main()


