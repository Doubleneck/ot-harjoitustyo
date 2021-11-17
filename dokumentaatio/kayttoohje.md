# Käyttöohje

Lataa projektin [lähdekoodi](https://github.com/Doubleneck/ot-harjoitustyo) koneellesi valitsemalla Code -valikon takaa download.zip.

##Konfigurointi

- [] toistaiseksi toteuttamatta

## Ohjelman käynnistäminen:

Asenna riippuvuudet:
```bash
poetry install
```
(jos komentoa poetry ei löydy, saatat tarvita ensin komennon:
```bash
 source $HOME/.poetry/env
```
Tietokannan alustus (ei vielä käytössä):
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

Anna laskimelle lukuja, ja se suorittaa valitsemiasi operaatioita. Ota huomioon, että kyseessä on dummy windows-tyypinen laskin, joka laskee annettuja operaatioita siinä järjestyksessä, kun ne annetaan. Eli laskin ei osaa laskea kertolaskua ennen summaa jne.
