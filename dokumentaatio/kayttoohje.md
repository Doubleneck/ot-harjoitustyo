# Käyttöohje

Lataa projektin [lähdekoodi](https://github.com/Doubleneck/ot-harjoitustyo) koneellesi valitsemalla Code -valikon takaa download.zip.

##Konfigurointi

- [] toistaiseksi toteuttamatta

## Ohjelman käynnistäminen:

Asenna riippuvuudet:
```bash
poetry install
```
Jos komentoa poetry ei löydy, saatat tarvita ensin komennon:
```bash
source $HOME/.poetry/env
```
Tietokannan alustus:
```bash
poetry run invoke build
```
Siirry poetryn virtuaaliympäristöön komennolla: 
```bash
poetry shell
```
Sovelluksen käynnistys:
```bash
poetry run invoke start
```
## Laskin:

Anna laskimelle lukuja, ja se suorittaa valitsemiasi operaatioita. Ota huomioon, että kyseessä on dummy windows-tyypinen laskin, joka laskee vain annettuja operaatioita yhden kerrallaan. Eli operaation jälkeen täytyy painaa "=" ja tuloksen jälkeen nollata laskin "c".

Laskin tekee tietokantaan tilastoa käytetyistä operaatioista. Saat tilaston näkymään komentorivillä painamalla laskimen nappia "STAT"


