# Käyttöohje

Lataa projektin [lähdekoodi](https://github.com/Doubleneck/ot-harjoitustyo) koneellesi valitsemalla Code -valikon takaa download.zip.

##Konfigurointi

- [] toistaiseksi toteuttamatta

## Ohjelman käynnistäminen:

Asenna riippuvuudet:

poetry install

(jos komentoa poetry ei löydy, saatat tarvita ensin komennon:

 source $HOME/.poetry/env

, että käyttämäsi shell löytää poetryn oikean polun)

Tietokannan alustus (ei vielä käytössä):

poetry run invoke build

--> siirry poetryn virtuaaliympäristöön komennolla: poetry shell

Sovelluksen käynnistys

poetry run invoke start

## Laskin:

Anna laskimelle lukuja, ja se suorittaa valitsemiasi operaatioita. Ota huomioon, että kyseessä on dummy windows-tyypinen laskin, joka laskee annettuja operaatioita siinä järjestyksessä, kun ne annetaan. Eli laskin ei osaa laskea kertolaskua ennen summaa jne.