# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/pakkaus.jpg)

Pakkaukset: _ui_ sisältää käyttöliittymästä, _services_ sovelluslogiikasta ja _repositories_ tietojen pysyväistallennuksesta vastaavan koodin. 

Ohjelmassa on pääluokat [GUI](../src/ui/gui.py), [CalculatorService](../src/services/calculator_service.py), [OperationsService](../src/services/operations_service.py) ja [CalculatorRepository](../src/repositories/calculator_repository.py), jotka ovat alla olevan kuvan mukaisessa 
suhteessa toisiinsa: 
![Luokkakaavio](./kuvat/UML.jpg)
## Käyttöliittymä

Ohjelmalla ei ole erikseen käyttäjiä.
Graafinen käyttöliittymä sisältää yksinkertaisen näkymän:

Laskin, jossa näyttö:
- numeronäppäimet
- näppäimet toiminnallisuuksille +, -, =, etc.
- näppäin STAT tulostaa terminaaliin tilaston.

Myös terminaali toimii osana käyttöliittymää, koska tietokannan haut tulostuvat terminaaliin.


Näkymien näyttämisestä vastaa [GUI](../src/ui/gui.py)-luokka. Käyttöliittymä on pyritty eristämään sovelluslogiikasta. 

GUI ainoastaan kutsuu [CalculatorService](../src/services/calculator_service.py)-luokan metodeja, joka edelleen kutsuu [OperationsService](../src/services/operations_service.py) luokan metodeja.

## Sovelluslogiikka



Toiminnallisuudesta vastaa luokka [CalculatorService](../src/services/calculator_service.py). Luokka kutsuu erillisen luokan [OperationsService](../src/services/operations_service.py)  metodeja, joilla laskimen toiminnallisuus syntyy.



Calculator tallentaa ja pääsee käsiksi suoritettujen operaatioiden tilastoihin tallennuksesta vastaavan pakkauksessa _repositories_ sijaitsevan luokan [CalculatorRepository](../src/repositories/calculator_repository.py) kautta. 


## Tietojen pysyväistallennus

Pakkauksen _repositories_ luokka `CalculatorRepository` huolehtii tietojen tallettamisesta käyttämällä SQLite -tietokantaa. 


### Tiedostot

Tilastodata tehdyistä laskutoimituksista tallennetaan SQLite-tietokannan tauluun `operations`, joka alustetaan [initialize_database.py](../src/initialize_database.py)-tiedostossa.

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Laskuoperaatioiden suorittaminen


- [ ]Tänne joku sekvenssikaavio

![TÄNNE JOKU SEKVENSSIKAAVIO](./kuvat/jokusekvenssi.png)


## Ohjelman rakenteeseen jääneet heikkoudet


### Käyttöliittymä



