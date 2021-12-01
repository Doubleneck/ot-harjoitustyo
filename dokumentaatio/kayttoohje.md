# Käyttöohje

Lataa projektin [lähdekoodi](https://github.com/Doubleneck/ot-harjoitustyo) koneellesi valitsemalla Code -valikon takaa download.zip.

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

Anna laskimelle lukuja, ja se suorittaa valitsemiasi operaatioita. Ota huomioon, että kyseessä on dummy windows-tyypinen laskin, joka laskee vain annettuja operaatioita yhden kerrallaan. Eli kaksipaikkaisten operaatioiden jälkeen täytyy painaa "=".
Saadulla luvulla voi siis jatkaa laskemista, mutta et voi suoraan laskea esim 3+4+5. Laskin huolehtii tästä estämällä uusien operaattoreiden painamisen.

Laskin tekee tietokantaan tilastoa käytetyistä operaatioista. Saat tilaston näkymään komentorivillä painamalla laskimen nappia "STAT"

Muistitoiminto:

M-ADD lisää näkyvän luvun muistipaikkaan.
M-CALL hakee lisätyn luvun muistipaikasta.
M-RESET tyhjentää muistipaikan (asettaa arvon 0)

Huom, on tarkoituskin, että C, joka nollaa laskimen ei nollaa muistipaikkaa.


