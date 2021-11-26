# Ohjelmistotekniikan harjoitustyö:laskin

Sovellus on työpöytälaskin graafisella käyttöliittymällä. 

##  Python-versio:

Sovelluksen toiminta on testattu Python-versiolla `3.6.0`.

## Dokumentaatio

- [käyttöohje](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)  
- [vaatimusmäärittely](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
- [tuntikirjanpito](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [ ]Arkkitehtuurikuvaus
- [ ]Testausdokumentti

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



