import unittest
import Nucleotides


class TestNucleotides(unittest.TestCase):

    def test_modification(self):
        tides = Nucleotides.Nucleotides()
        self.assertEqual(1, tides.get_a() + 1)
        self.assertEqual(1, tides.get_c() + 1)
        self.assertEqual(1, tides.get_g() + 1)
        self.assertEqual(1, tides.get_t() + 1)

    def test_repr(self):
        tides = Nucleotides.Nucleotides()
        tides.set_a(tides.get_a() + 1)
        tides.set_c(tides.get_c() + 1)
        tides.set_g(tides.get_g() + 1)
        tides.set_t(tides.get_t() + 1)

        self.assertEqual("A: 1, C: 1, G: 1, T: 1", tides.__repr__())

    def test_get_counts(self):
        tides = Nucleotides.Nucleotides()
        tides.set_a(tides.get_a() + 1)
        tides.set_c(tides.get_c() + 1)
        tides.set_g(tides.get_g() + 1)
        tides.set_t(tides.get_t() + 1)

        self.assertEqual("1 1 1 1", tides.get_counts())

if __name__ == "__main__":
    unittest.main()

