# Ohjelmistotekniikan harjoitustyö:laskin

Sovellus on työpöytälaskin graafisella käyttöliittymällä. 

##  Python-versio:

Sovelluksen toiminta on testattu Python-versiolla `3.6.0`.

## Dokumentaatio

- [ ]käyttöohje
- [vaatimusmäärittely](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
- [tuntikirjanpito](https://github.com/Doubleneck/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [ ]Arkkitehtuurikuvaus
- [ ]Testausdokumentti

## Asennus

1. Asenna riippuvuudet:

poetry install

(jos komentoa poetry ei löydy, saatat tarvita ensin komennon:

 source $HOME/.poetry/env

, että käyttämäsi shell löytää poetryn oikean polun)

2. Tietokannan alustus (ei vielä käytössä):

poetry run invoke build

--> siirry poetryn virtuaaliympäristöön komennolla: poetry shell

3. Sovelluksen käynnistys

poetry run invoke start

### Testaus

Testaus suoritetaan virtuaaliympäristössä komennolla:

poetry run invoke test

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

poetry run invoke coverage-report

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

poetry run invoke lint

