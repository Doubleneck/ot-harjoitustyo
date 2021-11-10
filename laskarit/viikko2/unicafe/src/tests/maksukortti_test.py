import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_oikean_saldon(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10")      

    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(12.5)
        self.assertEqual(str(self.maksukortti), "saldo: 22.5")     

    def test_rahan_ottaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(2.5)
        self.assertEqual(str(self.maksukortti), "saldo: 7.5")      

    def test_rahan_ottaminen_ei_vahenna_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(2.5)
        #saldo nyt 7.5
        self.maksukortti.ota_rahaa(8)
        self.assertEqual(str(self.maksukortti), "saldo: 7.5")      

    def test_rahan_ottaminen_palauttaa_True_jos_saldo_riittaa(self):
        self.assertEqual(True, self.maksukortti.ota_rahaa(10))  

    def test_rahan_ottaminen_palauttaa_False_jos_saldo_ei_riita(self):
        self.assertEqual(False, self.maksukortti.ota_rahaa(11))       