# Ohjelmistotekniikan harjoitustyö:laskin

Sovellus on työpöytälaskin graafisella käyttöliittymällä. 
[Release_1 viikko6](https://github.com/Doubleneck/ot-harjoitustyo/releases/tag/viikko6)
[Release_1 viikko5](https://github.com/Doubleneck/ot-harjoitustyo/releases/tag/Viikko5)  
##  Python-versio:

Sovelluksen toiminta on testattu Python-versiolla `3.8`.

## Dokumentaatio

- [käyttöohje](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)  
- [vaatimusmäärittely](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
- [tuntikirjanpito](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [arkkitehtuurikuvaus](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [testausdokumentti](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Asennus

1. Asenna riippuvuudet:
```bash
poetry install
```
Jos komentoa poetry ei löydy, saatat tarvita ensin komennon:
```bash
 source $HOME/.poetry/env
 ```
2. Tietokannan alustus:
```bash
poetry run invoke build
```
--> siirry poetryn virtuaaliympäristöön komennolla: 
```bash
poetry shell
```
3. Sovelluksen käynnistys
```bash
poetry run invoke start
```
### Testaus

Testaus suoritetaan virtuaaliympäristössä komennolla:
```bash
poetry run invoke test
```
### Testikattavuus

Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon.



