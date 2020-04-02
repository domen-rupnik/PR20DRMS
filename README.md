### Fakulteta za računalništvo in informatiko, Univerza v Ljubljani
# Projektna naloga pri predmetu Podatkovno Rudarjenje
Naslov: Prvič registrirana vozila v Sloveniji
<br>
Avtorja: Domen Rupnik 63180254, Matic Šuc 63180290
<br>
Mentor: doc. dr. Tomaž Curk
<br>
## Uvod
V nadaljevanju je predstavljena dosedanje delo pri projektni nalogi pri predmetu Podatko Rudarjenje, z naslovom Prvič registrirana vozila v Sloveniji.

## Podatki
Podatki so pridobljeni iz spletne strani [podatki.gov.si](https://podatki.gov.si/dataset/prvic-registrirana-vozila-po-mesecih), kjer so za vsak mesec zbrani podatki o registraciji vozil v Sloveniji, v csv datotekah, poimenovanih 'Podatki_mesecleto'. V projektni nalogi, bova uporabljala 60 takih datotek, torej podatke za obdobje od leta 2015 do leta 2019. Vsaka vrstica je opisana s 101 atributom. Atributi vecinoma opisujejo lastnosti in identifikacijo vozila, podtke o lokaciji registracije in nekaj osnovnih podatkov o lastniku vozila oz osebi, ki ga je registrirala.

Pri delu s podatki je bilo odkritih nekaj napak, na katere sva bila v nadaljevanju bolj pozorna.

## Izvedene analize
### Vizualizacija najpogostejše barve glede na čas
Eden izmed najinih ciljev pri projektni nalogi je bil, da bi ugotovila, katera je bila najpogostejša barva pri na novo registriranih avtomobilih v Sloveniji. Kmalu sva ugotovila, da je bila za vsak mesec med leti 2015 in 2019, najpogostejša barva bela. Na drugem in tretjem mestu pa sta se izmenjevali svetlo-siva ter temno-siva. Nad rezultatom sva bila presenečena, saj sva pričakovala, da bi bila najpogostejša barva siva. Na koncu sva se odločila, da bova vizualizirala, kakšen odstotek od vseh barv, predstavlja bela barva. Ker je pa vseh mesecev 60, sva se odločila, da jih združiva po polletjih. Od januarja do junija je prvo polletje in od julija do decembra drugo. Glede na graf sva prišla do spoznanja, da je bele barve povprečno pribljižno malo manj kot 20%.

<img src="slike/graf_barva.png" width="500" height="350">

### Vizualizacija števila vozil glede na občino

Zanimalo naju je tudi, katera občina ima največ na novo registriranih vozil. Predvidevala sva, da je to občina Ljubljana, saj je občina, ki ima največ prebivalcev. Po prvem delu analize sva ugotovila, da je to res občina Ljubljana. Med letoma 2015 in 2019 je imela na novo registrianih kar 154.514. To se nama je zdelo zelo čudno, saj ima občina Ljubljana 288.832 prebivalcev. Kar bi pomenilo, da bi vsak drugi prebivalec občine Ljubljana si v tem času kupil novo vozilo. Šla sva pregledovat podatke in ugotovila, da med podatki niso samo na novo registirana vozila, ampak tudi vozila, ki se jih je v tem času odjavilo. Zato sva popravila kodo in novo število na novo registriranih vozil v Ljubljani je bilo 132.185. Še vedno je bila zelo velika številka. Narisala sva graf za 10 občin z največ vozili.

<img src="slike/graf_obcine.png" width="500" height="350">

Odločila sva se, da pogledava, koliko izmed vseh registrianih je registriranih na podjetje. Prišla sva do ključne ugotovitve, ki je ta, da je 86% vozil registriranih na podjetje. Kar pomeni, da je fizičnih kupcev v Ljubljani 17.267. Spet sva vizualizirala 10 občin z največ vozili.

<img src="slike/graf_obcine_fizicni.png" width="500" height="350">

### Vizualizacija goriv registriranih vozil

Pri tej vizualizaciji sta pričakovano prevladovali dizelsko in bencinsko gorivo, ostalih goriv je bilo nesmiselno dodajati na graf. Obe krivulji upadata, kar je posledica sprememb na tem področju avtomobilizma, saj na trg prihajajo predvsem vozila na električni pogon. Zanimiva je tudi razlika registriranih vozil z bencinskim gorivom, med letoma 2017 in 2016.

<img src="slike/graf_bencin_dizel.PNG" width="500" height="350">

### Vizualizacija znamk registriranih vozil

Za to vizualizacijo sva najprej za vsako leto izpisala 3 največ registriranih znamk v tistem letu in ugotovila, da prevladujejo te, ki so vizualizirane na grafu. Presenetljivo je leta 2017, kot 3. najbolj registrirana znamka vozil bila TOMOS, za preostala leta pa je bil razpored enak.

<img src="slike/graf_znamke_po_letih.PNG" width="500" height="350">

### Vizualizacija starosti registriranih vozil

Pri tej vizualizaciji je bilo potrebno podatek o starosti vozil klasificirati. Prvi razred je novo vozilo, v drugi razred sva klasificirala vozila stara največ 5 let, v tretji pa vsa ostala.

<img src="slike/graf_starost_vozil.PNG" width="500" height="350">
