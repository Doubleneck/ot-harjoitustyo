# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaa `CalculatorService`-luokka, jota testataan [TestCalculatorService](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/src/tests/calculator_service_test.py)-testiluokalla. 
`CalculatorService`-olio alustetaan, niin että sille asetetaan alkuarvoksi 16 ja operaatiot suoritetaan siitä lähtien. 
Tilastointia varten olevaa repositorioluokkaa `CalculatorRepository` testataan erikseen. 

### Repositorio-luokka

Repositorioluokkaa `CalculatorRepository` testataan testiluokalla [TestCalculatorRepository](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/src/tests/calculator_repository_test.py). 
Testiluokassa alustetaan tietokannan taulu "operations" tyhjäksi datasta. Testiluokan metodeilla testataan tietokannan alustuksen onnistuminen ja lisäksi jokaisen operaation tallentaminen sekä haku.

### Testauskattavuus

Käyttöliittymää GUI lukuunottamatta sovelluksen testauksen haarautumakattavuus on 97%.

![](./kuvat/testikattavuus.png) 

UnitTestien ulkopuolelle jää initialize_database.py, joka on kuitenkin testattu komentoriviltä. 

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla sekä Linux-ympäristöön. 

### Toiminnallisuudet

Kaikki [määrittelydokumentin](./vaatimusmaarittely.md#perusversion-tarjoama-toiminnallisuus) ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi ja ne toimivat. 
Peruslogiikan toimivuus on pyritty varmistamaan sillä, että käyttäjä ei enää pysty painamaan niitä nappeja, joiden toimintaa ei tietyssä prosessin vaiheessa haluta. Tätä on testattu mahdollisimman laajalla virhesyötteellä.



