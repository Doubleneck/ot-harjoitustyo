import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate (unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)    

    def test_luodun_kassapaatteen_saldo_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)    

    def test_luodun_kassapaatteen_edulliset_on_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)      

    def test_luodun_kassapaatteen_maukkaat_on_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)      

    def test_syo_edullisesti_kateisella_kertyy_kassaan_oikein_kun_maksu_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_palauttaa_vaihtorahat_oikein_kun_maksu_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10) 

    def test_syo_edullisesti_kateisella_kasvattaa_myytyja_kun_maksu_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)  
        self.kassapaate.syo_edullisesti_kateisella(250)  
        self.kassapaate.syo_edullisesti_kateisella(250)  
        self.assertEqual(self.kassapaate.edulliset, 3)       

    def test_syo_edullisesti_kateisella_ei_kerry_kassaan_kun_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_palauttaa_vaihtorahat_oikein_kun_maksu_ei_riita(self): 
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200) 

    def test_syo_edullisesti_ei_kasvata_myytyja_kun_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)  
        self.kassapaate.syo_edullisesti_kateisella(0)    
        self.assertEqual(self.kassapaate.edulliset, 0)  

    def test_syo_maukkaasti_kateisella_kertyy_kassaan_oikein_kun_maksu_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_palauttaa_vaihtorahat_oikein_kun_maksu_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10) 

    def test_syo_maukkaasti_kateisella_kasvattaa_myytyja_kun_maksu_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)  
        self.kassapaate.syo_maukkaasti_kateisella(410)  
        self.kassapaate.syo_maukkaasti_kateisella(420)  
        self.assertEqual(self.kassapaate.maukkaat, 3)       

    def test_syo_maukkaasti_kateisella_ei_kerry_kassaan_kun_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_palauttaa_vaihtorahat_oikein_kun_maksu_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300) 
  

    def test_syo_edullisesti_kortilla_veloittuu_kortilta_kun_saldo_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 760")

    def test_syo_edullisesti_kortilla_palauttaa_True_kun_saldo_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(True, self.kassapaate.syo_edullisesti_kortilla(kortti)) 

    def test_syo_edullisesti_kortilla_kasvattaa_edullisia_kun_saldo_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)  

    def test_syo_edullisesti_kortilla_ei_veloitu_kortilta_kun_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 200")

    def test_syo_edullisesti_kortilla_palauttaa_False_kun_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(False, self.kassapaate.syo_edullisesti_kortilla(kortti)) 

    def test_syo_edullisesti_kortilla_ei_kasvata_myytyja_kun_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)         

    def test_syo_maukkaasti_kortilla_veloittuu_kortilta_kun_saldo_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 600")

    def test_syo_maukkaasti_kortilla_palauttaa_True_kun_saldo_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(True, self.kassapaate.syo_maukkaasti_kortilla(kortti)) 

    def test_syo_maukkaasti_kortilla_kasvattaa_maukkaita_kun_saldo_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)     

    def test_syo_maukkaasti_kortilla_ei_veloitu_kortilta_kun_saldo_ei_riita(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 300")

    def test_syo_maukkaasti_kortilla_palauttaa_False_kun_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(False, self.kassapaate.syo_maukkaasti_kortilla(kortti)) 

    def test_syo_maukkaasti_kortilla_ei_kasvata_myytyja_kun_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)      

    def test_syo_edullisesti_kortilla_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)      

    def test_syo_maukkaasti_kortilla_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)      

    def test_kortin_lataus_muuttaa_kortin_saldoa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 300)  
        self.assertEqual(str(kortti), "saldo: 300")  

    def test_kortin_lataus_ei_muuta_kortin_saldoa_jos_summa_neg(self):
        kortti = Maksukortti(300)
        self.kassapaate.lataa_rahaa_kortille(kortti, -20)  
        self.assertEqual(str(kortti), "saldo: 300")      

    def test_kortin_lataus_muuttaa_kassan_saldoa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 20)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100020)
     