---
title: "Moc haseł słownikowych"
date: 2023-09-05
draft: false
tags: [kryptografia, bezpieczeństwo]
math: true
fortune: "W porządku. Poszukam w domu, może uda mi się znaleźć linijkę i kawałek sznurka."
motto:
  quote: "— Naszym wrogiem jest obcy statek kosmiczny wyładowany bombami atomowymi — odparłem. — A my mamy kątomierz."
  author: "Neal Stephenson"
  cite: "Peanatema"
---

## Prolog

Załóżmy, że użytkownik chce założyć konto w jakimś serwisie i ustawić hasło `dwa-tygrysy-lubia-mak`. Nie zastanawiajmy się na razie, dlaczego akurat takie, prześledźmy po prostu interakcję ze stroną internetową:

<dl>
<dt>Strona:
<dd>Zaproponuj hasło. Zaskocz mnie.
<dt>Użytkownik:
<dd><code>dwa-tygrysy-lubia-mak</code>
<dt>Strona:
<dd>Jak to tak bez wielkiej litery?
<dt>Użytkownik:
<dd><code>Qwert</code>
<dt>Strona:
<dd>A cyferka?
<dt>Użytkownik:
<dd><code>Qwert1</code>
<dt>Strona:
<dd>Głupcze, znak specjalny, bo cię zhackują!
<dt>Użytkownik:
<dd><code>Qwert1&nbsp;</code>
<dt>Strona:
<dd>Nie, pysiu, spacja to nie, bo… jak zapiszesz na kartce, to jej nie widać. Czy coś tam, sama nie wiem…
<dt>Użytkownik:
<dd><code>Qwert1!</code>
<dt>Strona:
<dd>Ciekawe, czemu od razu tego nie powiedziałam, ale oczekuję co najmniej ośmiu znaków.
<dt>Użytkownik:
<dd><code>Qwerty1!</code>
<dt>Strona:
<dd>Dziękuję, teraz jesteś bezpieczny. Hasło <code>dwa-tygrysy-lubia-mak</code> było głupie. To teraz, z tymi znakami, które na klawiaturze wszystkie są obok siebie, jest z&nbsp;pewnością nie do odgadnięcia. Ja bym na przykład nie dała rady.
</dl>

W dzisiejszych czasach takie historie zdarzają się coraz rzadziej. Niekoniecznie dlatego, że stosowane w Internecie polityki haseł są mądrzejsze. Nie. Raczej dlatego, że używamy menedżerów haseł, które wypluwają automatycznie długi ciąg losowych znaków. Bo używacie menedżera haseł i macie inne hasło do każdej usługi. Prawda? Jeżeli nie, to nie ma sensu, żebyście czytali dalej. Serio.

Skoro czytasz, to znaczy, że używasz menedżera haseł. Punkt dla Ciebie! Nie masz więc problemu z generowaniem haseł, chyba że spodziewasz się używać hasła na innym komputerze (gdzie nie chcesz odszyfrowywać swojego portfela z hasłami), podyktować komuś przez telefon albo jest to po prostu główne hasło do systemu lub owego menedżera. Chciałbyś sobie użyć wówczas zgrabnej frazy `dwa-tygrysy-lubia-mak`. Użyłeś nawet dywizów, bo wiesz przecież, że podsystemy uwierzytelniania często nie tolerują spacji (mimo że mamy rok 2023!). One jednak wolą `Qwerty1!`. Czy naprawdę to lepsze hasło? Co to w ogóle znaczy, że hasło jest „lepsze” lub „gorsze”?

Ongiś, gdy z pierwszych komputerów korzystały pterodaktyle, mówiło się, że trzeba <del>nawpierdzielać</del> wpisać dużo znaków specjalnych. To były takie runy, których wysoki potencjał magiczny miał zabezpieczać hasło. Zły haker, taki obleśny, cały w okruszkach chipsów i plamach od coli, wpisywałby datę urodzin, imię Twojej pierwszej dziewczyny albo `Led Zeppelin`, ale nigdy nie wpadłby na `Qwerty1!`.

No dobrze, nie do końca o to chodzi. Już pterodaktyle wiedziały, że na ogół do łamania haseł służą komputery, nie hakerzy. Żeby jednak wszystko dobrze zrozumieć, musimy sobie wyjaśnić, w jakich okolicznościach łamie się hasła.

## Okoliczności łamania haseł

### Zgadywanie hasła _in situ_

Scenariuszem najbardziej znanym z filmów, a więc najbzdurniejszym (choć zarazem najmniej kłopotliwym pod kątem bezpieczeństwa), jest zgadywanie hasła przez złego człowieka siedzącego przy naszym komputerze. Tutaj rzeczywiście wystarczy nie używać własnego imienia czy daty urodzin, żeby zminimalizować ryzyko praktycznie do zera. Większość systemów powinna stosować _throttling_, czyli spowalniać zgadywanie haseł przez czasowe blokowanie możliwości wprowadzania hasła. Nawet domofony mają takie zabezpieczenie, dlatego po wpisaniu błędnego kodu blokują się na kilka sekund. Z tej też przyczyny serwis z memami może na nas wymusić użycie hasła `ds090j#)(ejSD**`, a do karty bankomatowej ustawiamy PIN `5473`. Po prostu w bankomacie mamy tylko kilka prób, a na dodatek jesteśmy rejestrowani przez kamerę. Chyba że jesteśmy w maseczce. Albo szaliku i ciemnych okularach. Albo zasłonimy kamerę. No dobrze, nic nie mówiłem o kamerze.

### Atak na panel logowania _on-line_

Znacznie bardziej atrakcyjne dla atakującego są systemy, do których logujemy się zdalnie. Tu nie tylko można zgadywać hasło, siedząc bezpiecznie w swojej piwnicy i&nbsp;pogryzając niezdrowe przekąski, ale po prostu napisać automat, który przeprowadzi atak słownikowy czy mniej lub bardziej wyrafinowany _brute-force_. Tu też na przeszkodzie powinien stanąć _throttling_ albo <abbr title="Completely Automated Public Turing test to tell Computers and Humans Apart">CAPTCHA</abbr>, ale gdyby takiego zabezpieczenia zabrakło, ograniczeniem jest tylko przepływność łącza internetowego i wydajność serwera. Nawet zakładając, że możemy sprawdzać tylko 10 haseł na sekundę, w ciągu doby możemy zweryfikować 864&nbsp;000 haseł. Zaczyna się robić nieprzyjemnie.

### Atak _off-line_, czyli wszystkie ręce na pokład

Załóżmy jednak, że interfejs logowania jest odpowiednio zabezpieczony albo nasze hasło jest na tyle długie, że on-line'owy _brute-force_ zająłby lata. Czy jesteśmy bezpieczni? Nie, bowiem dopiero kolejny sposób zgadywania haseł jest naprawdę wydajny, a ponadto stanowi realne i powszechne zagrożenie. Szansę na to, że ktoś będzie chciał włamać się konkretnie na wasze konto e-mail, bankowe, w ulubionej grze czy na GitHubie musicie ocenić sami. Istnieją jednak wycieki. Włamanie na serwer, szpieg w siedzibie firmy, wściekły na pracodawcę pracownik — to przykładowe przyczyny pojawienia się bazy danych z loginami i hasłami na czarnym rynku lub nawet jej upublicznienia. Mogłoby się wydawać, że w tym momencie jest pozamiatane, oto bowiem zły człowiek dostaje na tacy:

```
ala:qwerty
becia:Tralala42TrudneHaslo!
czesio:Tralala42TrudneHaslo!
```

Ala nie ma czym się przejmować, widać, że jej nie zależy, ale Becia i Czesio… Lepiej, żeby stosowali inne hasło do każdej witryny. W przeciwnym wypadku właśnie ktoś próbuje im się logować nie tylko na zaatakowaną stronę, ale na wszystkie popularne serwisy, korzystając z ich pieczołowicie wymyślonego hasła.

Po co więc stosować trudne hasła? Może należy pójść drogą Ali? Otóż nie. Takie bazy haseł praktycznie nie występują. Owszem, czasem po założeniu konta w jakimś sklepie internetowym dostajemy maila: <cite>Witamy w naszym sklepie z chrupkami! Twój login to ala, a hasło to qwerty</cite>. Zdarza się to coraz rzadziej i świadczy o tym, że <del>jakiś idiota</del> nieodpowiedzialny admin trzyma Wasze hasło zapisane jawnym tekstem[^1]. Ponadto ma Was za niezbyt rozgarniętych, bo przecież używacie menedżera haseł i nikt Wam hasła nie musi przypominać. Tym bardziej minutę po jego ustaleniu.

W praktyce już ichtiozaury stosowały haszowanie haseł i ich bazy wyglądały tak:

```
ala:65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5
becia:0c7156b93cd5df495fb019ae000af5145879a17a779151bfb684920fc8945b64
czesio:0c7156b93cd5df495fb019ae000af5145879a17a779151bfb684920fc8945b64
```

Jak widać, z hasłami stało się coś dziwnego, a odpowiada za to któraś z [funkcji haszujących](https://pl.wikipedia.org/wiki/Funkcja_skr%C3%B3tu), zwanych też funkcjami skrótu lub funkcjami mieszającymi. Funkcje te mają wiele zastosowań i zestaw specyficznych własności, z których dla nas najbardziej istotną jest to, że łatwo jest policzyć hasz, znając hasło, ale operacja odwrotna — obliczenie hasła na podstawie skrótu — jest praktycznie niemożliwa. Pozostaje tylko zgadywanie.[^2]

{{< figure src="ichthyosaurus.webp" link="https://commons.wikimedia.org/wiki/File:In_the_Days_of_the_Sea_Monsters_Plesiosaurus_and_Ichthyosaurus_b1072272_018_tif_9s161666b.tif" title="Tak naprawdę ichtiozaury nie korzystały z komputerów" >}}

System uwierzytelniający w tym przypadku nie zna hasła. Gdy użytkownik wprowadza hasło, liczony jest jego skrót, a uwierzytelnienie następuje w przypadku, gdy skrót jest zgodny z tym zapisanym w bazie. Hasło nie może więc wyciec z bazy danych na serwerze, bo go tam nie ma, a zgadnięcie hasła na podstawie skrótu jest niemożliwe. A właściwie powinno być…

Nie trzeba być bardzo spostrzegawczym, żeby zauważyć, że Becia i Czesio mają takie samo hasło. Nie trzeba też być geniuszem, żeby wpaść na pomysł, by zebrać tysiące najbardziej popularnych haseł, policzyć hasze, choćby miało to trwać rok, i trzymać je w pliku:

```
a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3 -> 123
65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5 -> qwerty
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad -> abc
```

Takie pliki są wprawdzie olbrzymie, nawet gdy stosuje się sprytną metodę ich pakowania — [tęczowe tablice](https://pl.wikipedia.org/wiki/T%C4%99czowe_tablice) — niemniej działają. A właściwie działały, gdyż na szczęście bardzo łatwo je unieszkodliwić. Wystarczy przy tworzeniu hasza dokleić do hasła losowy ciąg znaków, tzw. [sól](https://pl.wikipedia.org/wiki/S%C3%B3l_(kryptografia)), by to samo hasło w każdej bazie i dla każdego użytkownika, który z niego korzysta, miało inną postać. Sól możemy dopisać jawnie przy haszu, by umożliwić ponowne przeliczenie skrótu przy uwierzytelnianiu — nie obniża to bezpieczeństwa — a atakującemu pozostaje mozolne zgadywanie.

Tu pojawia się dla nas pewien problem, bo funkcje skrótu, ze względu na swoje szerokie zastosowania, mają bardzo brzydką cechę — liczy się je bardzo szybko. W dzisiejszych czasach nie trzeba trzymać w domu superkomputera za miliony dolarów, można za to przeznaczyć kilkanaście tysięcy USD na wynajęcie mocy obliczeniowej w&nbsp;chmurze lub kupić koparkę jakiejś kryptowaluty, opartej na interesującej nas funkcji haszującej. Dla bardzo popularnej funkcji SHA-256 będzie to Bitcoin, którego hasze można przeliczać koparką [Bitcoin Miner S19 Pro+ Hyd.](https://shop.bitmain.com/product/detail?pid=00020221229153045195XzfP62rE069C), liczącą 191 bilionów skrótów w ciągu sekundy.

{{< figure src="antspace.png" link="https://shop.bitmain.com/product/detail?pid=00020221229153045195XzfP62rE069C" title="Można też kupić cały kontener wypełniony po brzegi koparkami" >}}

W odpowiedzi na to zagrożenie powstały standardy takie jak [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2), które z góry zakładają nie tylko solenie haseł, ale liczenie skrótu z hasła, skrótu ze skrótu, później skrótu ze skrótu ze skrótu… i tak np. 10&nbsp;000 razy. Algorytmy takie jak [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), [scrypt](https://en.wikipedia.org/wiki/Scrypt) i [Argon2](https://en.wikipedia.org/wiki/Argon2) zostały opracowane z myślą o tym, by poza obciążeniem procesora maksymalizować także zużycie pamięci podczas liczenia skrótu hasła. Co prawda generuje to koszt na serwerze w trakcie uwierzytelniania, a użytkownik musi zaczekać np. dodatkową sekundę, by system przeliczył hasz jego hasła, ale jest to koszt, który godzimy się ponieść, by maksymalnie utrudnić życie atakującemu. Właściwie dla odpowiednio silnej konfiguracji tego rodzaju algorytmów nawet proste hasło będzie bardzo trudne do złamania, gdyż nie da się w rozsądnym tempie liczyć skrótów.

I tu dochodzimy do wniosku, którego pewnie się spodziewaliście — trudno jednoznacznie określić, jak silne musi być hasło, byśmy czuli się bezpieczni. Niemniej, aby cokolwiek o tym powiedzieć, najpierw musimy wymyślić, jak mierzyć jego moc.

## Moc hasła

Intuicyjnie czujemy, że hasło `tkf` jest słabsze od `znfkkl`. Co jednak gdy atakujący założy, że nikt nie używa krótkich, trzyznakowych haseł i sprawdza je dopiero po sprawdzeniu haseł cztero-, pięcio- i sześcioznakowych? Wówczas `tkf` będzie silniejsze, ponieważ jego złamanie zajmie więcej czasu. Podobnie `a*d-6i` wydaje się lepsze od `ynfkkl`, ale co jeżeli program łamiący hasła zgaduje je w porządku leksykograficznym (alfabetycznym)? Wówczas hasło `z` byłoby lepsze od wszystkich wymienionych…

Programy łamiące hasze, np. najbardziej znany [John The Ripper](https://www.openwall.com/john/), wspierają różne formy ataku i można je skonfigurować zależnie od stanu wiedzy na temat atakowanego systemu. Jeżeli wiemy, że system wymusza zmianę hasła raz w miesiącu, warto próbować prostych haseł z doklejoną nazwą miesiąca. A jeżeli wiemy, że system wymusza znaki specjalne, wiadomo, że nie ma sensu atakować haseł złożonych z samych liter czy cyfr.

Co ciekawe, gdyby system pozwalał na hasła bez znaków specjalnych, atak byłby w&nbsp;ogólności trudniejszy, bo przecież możliwych haseł byłoby więcej! Dlaczego więc wszyscy dokoła wymuszają znaki specjalne? Bo jeżeli użytkownikom zostawimy wolną rękę, to wiadomo, że większość wybierze raczej proste hasło w stylu `qwerty` lub `pomidorowa`, a wówczas wystarczy stworzyć słownik złożony z wszystkich wyrazów w&nbsp;danym języku i fraz łatwych do wpisania z klawiatury (`qwerty`, `asdf`, `1234` itp.) i sprawdzać kolejne pozycje. Wymuszenie użycia znaków specjalnych, wielkich liter i&nbsp;cyfr sprawia, że prosty atak słownikowy nie zda egzaminu i będzie trzeba zastosować metodę siłową lub połączenie obydwu (bo przecież użytkownicy wciąż będą wymyślać „trudne” hasła w stylu `Pomidorowa3`). Tu należy jednak zaznaczyć, że <abbr title="John The Ripper">JTR</abbr> nie zgaduje haseł w porządku leksykograficznym, ale tworzy listę wzorców opartych na najbardziej popularnych trójznakach, które w wymyślny sposób miesza ze sobą. Skutkiem tego rzeczywiście potrafi sprawdzać niektóre dłuższe hasła ze znakami specjalnymi wcześniej niż krótsze i złożone z samych małych liter. Jako punkt wyjścia przyjmuje się jednak, że cracker zgaduje hasła w sposób losowy, ale poczynając od najkrótszych i złożonych z najprostszych zbiorów znaków.

Dla czterocyfrowego PIN-u mamy zatem 10&nbsp;000 możliwych kombinacji. Nazwiemy to dziedziną hasła i na razie nie będziemy przejmować się tym, że rzadko kiedy atakujący będzie musiał sprawdzić wszystkie kombinacje, a PIN `1234` z pewnością zostanie sprawdzony w trzech pierwszych próbach, razem z `0000` i `1111`.

Skąd bierze się 10&nbsp;000? Otóż mamy do dyspozycji 10 symboli na czterech pozycjach, co daje:

$10 \cdot 10 \cdot 10 \cdot 10 = 10^4 = 10000$

I tę właśnie liczbę kombinacji możemy określić mocą hasła. Zauważmy, że dla ośmioznakowego hasła, w którym pozwolimy sobie na użycie małych i wielkich liter, cyfr oraz znaków specjalnych dostępnych wprost z klawiatury, co daje 95 symboli, otrzymujemy:

$95^8 = 6 634 204 312 890 625$

Liczby rzędu biliardów nie są jednak zbyt wygodne w używaniu, w szczególności w porównywaniu z innymi. Zastosujemy więc matematyczną sztuczkę w postaci narzędzia, jakim jest logarytm. Logarytm sprowadza bardzo małe i bardzo duże liczby do wspólnego poziomu. Użyjemy logarytmu o podstawie 2, dzięki czemu otrzymamy wynik w bitach. Dla naszego czteroznakowego PIN-u mamy:

$H = log_2(10^4) \approx 13{,}3$

zaś dla wspomnianego hasła ośmioznakowego:

$H = log_2(95^8) \approx 52{,}6$

Taką miarę mocy hasła często nazywa się entropią, co stanowi nawiązanie teorii informacji i definiowanej w jej ramach miary ilości informacji.

## Hasła słownikowe

### Silne hasła słownikowe

Przyjmijmy sobie, na razie _a priori_, że ośmioznakowe hasło ze znakami specjalnymi o&nbsp;mocy 52,6 bita jest „bezpieczne”. Zresztą wiele systemów tak je właśnie traktuje. Korzystając z naszego wzoru, szybko wykażemy, że hasło złożone z dwunastu samych małych liter, czyli 26 symboli, wcale nie jest słabsze:

$H = log_2(26^{12}) \approx 56{,}4$

Dlaczego więc zabrania się takich haseł? Dlaczego nie powinniśmy używać hasła `tabakierkach`? Otóż obliczając moc hasła, założyliśmy, że atakujemy je algorytmem _brute-force_. Jeżeli jednak cracker załaduje sobie np. [słownik języka polskiego](https://sjp.pl/sl/growy/), który ma 3&nbsp;185&nbsp;486 pozycji (uwzględniamy fleksję, jak w Scrabble'ach), możemy potraktować to słowo jako pojedynczy symbol dobrany z trzech milionów możliwości:

$H = log_2(3185486^1) \approx 21{,}6$

Nie za wiele, a zakładając, że użytkownik wprowadzi hasło w formie podstawowej (mianownik rzeczownika, bezokolicznik czasownika itp.) i cracker zacznie atak od takich właśnie form, będzie to jeszcze mniej. Zakładając, że przeciętny Polak ma zasób słów rzędu 10&nbsp;000[^3] [^4], mamy:

$H = log_2(10000^1) \approx 13{,}3$

Nikt nam jednak nie broni użyć czterech słów, co daje nam wynik porównywalny z&nbsp;wcześniej analizowanym ośmioznakowym bełkotem:

$H = log_2(10000^4) \approx 53{,}2$

Po zlogarytmowaniu to niepozorny wynik, ale mówimy tu o dziesięciu biliardach kombinacji. Wprawdzie użytkownicy będą mieli tendencję do łączenia ze sobą wyrazów w&nbsp;logiczne i&nbsp;poprawne gramatycznie frazy, co zawęża dziedzinę, ale stworzenie programu łamiącego hasła, który uwzględni to dla wszystkich języków, trywialne nie jest.

### Słabe hasła ze znakami specjalnymi

Ponadto wcale wymuszenie hasła zawierającego znaki specjalne nie daje gwarancji, że hasło będzie trudne do złamania. Czy te systemy uwzględniają sprawdzanie hasła pod kątem sztuczek, które stosują użytkownicy?

1. Weź beznadziejne hasło, jak `qwerty`.
2. Zamień pierwszą literę na wielką, uzyskując `Qwerty`.
3. Zamień litery `e` na cyfrę `3`, a na `@` itd. (tzw. [_leet-speak_](https://pl.wikipedia.org/wiki/Leet_speak)), uzyskując `Qw3rty`.
4. Dodaj znak specjalny, najlepiej pierwszy z brzegu: `Qw3rty!`.
5. Dopełnij hasło cyframi do żądanej długości: `Qw3rty!1`.

Spróbujmy oszacować moc tego hasła, tym razem zakładając w miarę inteligentne zgadywanie. Wyjściowe `qwerty` znajdziemy na liście [47&nbsp;023 najpopularniejszych haseł](https://github.com/dropbox/zxcvbn/blob/master/data/passwords.txt). Jest tam na czwartym miejscu, więc wiemy, że na pewno będzie sprawdzane jako jedno z pierwszych, ale przyjmijmy optymistycznie 47&nbsp;023 kombinacje:

$H = log_2(47023^1) \approx 15{,}5$

Sprawdzając wszystkie hasła w wersjach — złożonej z samych małych liter i z wielką literą na początku — mamy dwa razy więcej kombinacji, czyli zyskujemy jeden bit mocy:

$H = log_2(47023^1 \cdot 2) \approx 16{,}5$

Podmiana _leet-speakowa_ w przypadku takich haseł też nie daje wiele, bo to tylko kilka kombinacji więcej. Załóżmy szacunkowo, że średnio cztery razy więcej:

$H = log_2(47023^1 \cdot 2 \cdot 4) \approx 18{,}5$

Dorzucamy teraz jeszcze dwa symbole uzupełniające do ośmiu znaków (10 cyfr i 33 znaki specjalne):

$H = log_2\left(47023^1 \cdot 2 \cdot 4 \cdot (10 + 33)^2 \right) \approx 29{,}4$

Jak widać, wynik jest słaby. Słabszy nawet niż użycie po prostu dwóch beznadziejnych haseł bez żadnych zmian, np. `qwerty 1234`:

$H = log_2(47023^2) \approx 31{,}0$

### Paradoksy polityk haseł

O co tu chodzi? Z jednej strony nie pozwala się użytkownikowi wprowadzić solidnego hasła w rodzaju `dwa-tygrysy-lubia-mak`, które na dodatek łatwo zapamiętać, a wymusza się stosowanie haseł trudnych do zapamiętania, choć mogą one być tworzone według prymitywnych wzorców i łatwe do złamania? Cóż… Kryptografia nie zawsze jest intuicyjna. Hasło `lubimy smaczne placki` jest porównywalne z `7%dF-x`, ale to drugie wygląda jednak nieco mądrzej i bezpieczniej, a pierwsze wydaje się podejrzanie łatwe.

Nie chodzi jednak tylko o mylącą intuicję, z którą można walczyć prostymi obliczeniami. Jest coś, co wykorzenić trudniej — przesądy, a przesądy w <abbr title="Information Technology">IT</abbr> są równie silne jak w innych dziedzinach życia i, tak jak wszędzie, biorą się z lenistwa i bazowania na przestarzałych przesłankach. Zasady sugerujące nadrzędność bełkotliwych haseł opracował dla amerykańskiego Narodowego Instytutu Norm i Techniki <abbr title="National Institute of Standards and Technology">NIST</abbr> Bill Burr[^5] w 2003 roku, bazując na pracach Claude'a Shanona z połowy XX wieku i dokumentach z lat osiemdziesiątych. Opisał je w ośmiostronicowym załączniku _Estimating Password Entropy and Strength_ do normy [NIST 800-63](https://csrc.nist.gov/CSRC/media/Publications/sp/800-63/ver-10/archive/2004-06-30/documents/sp800-63-v1-0.pdf). W [wywiadzie dla The Wall Street Journal](https://www.wsj.com/articles/the-man-who-wrote-those-password-rules-has-a-new-tip-n3v-r-m1-d-1502124118) przyznał, że szył z głowy, bo kazano mu coś tam napisać o bezpiecznych hasłach.

Nie tylko on był jednak winien, gdyż z dokumentu można samodzielnie wywnioskować, że jest to zestaw pewnych domniemywań i pobożnych życzeń, i to nie tylko między wierszami, gdyż o regule znaków specjalnych pisze wprost: 

> the benefit is probably modest and nearly independent of the length of the password
>
> --- <cite>NIST 800-63</cite>

Podkreśla za to korzyści ze sprawdzania, czy hasło proponowane przez użytkownika jest w słowniku, czego nie robi prawie nikt. Prościej wszak kazać użytkownikowi wpisywać krzaczki niż analizować jego hasła, uaktualniać słowniki, zastanawiać się, jakie języki należy obsłużyć, oprogramowywać podstawienia _leet-speak_ itp. Skutkiem tego bezpieczeństwo niewiele się poprawia, a użytkownikom trudno jest zapamiętać hasła. Tyle dobrego, że menedżery haseł równie dobrze zapamiętują kilkanaście znaków specjalnych, jak kilka słów.

## Jaka moc zapewnia bezpieczeństwo?

### Analityczne wyznaczenie mocy

Teraz dochodzimy do najtrudniejszego aspektu naszych rozważań. Moc hasła możemy jako-tako oszacować prostymi obliczeniami, ale aby określić, jakiej wartości oczekujemy, musimy rozwiązać równanie, w którym uzależniamy ją od oczekiwanego średniego czasu łamania $t$ (wyrażonego w sekundach) i prędkości łamania $v$ (wyrażonej w haszash na sekundę):

$H = log_2(2tv)$

Czas mnożymy przez dwa, gdyż średni czas łamania to połowa czasu potrzebnego na sprawdzenie całej dziedziny haseł.

Wartość $t$ to względnie mały problem — określamy ją w zasadzie według swoich potrzeb. Ja bym przyjął, że do poważnych zastosowań zadowala nas rok. To nie wydaje się dużo w porównaniu z setkami lat, które pojawiają się czasem w algorytmach oceniających hasła, ale wynika to z niskiej wartości $v$, która jest w nich przyjmowana. Zakłada się tam bardzo silne algorytmy haszujące lub atak na słabsze algorytmy za pomocą zwykłego PC-ta. Co prawda iloczyn $tv$ może okazać się podobny, nie wydaje mi się jednak realne rozpatrywanie czasów łamania rzędu wieków czy mileniów. Trudno mi sobie wyobrazić, żeby ktokolwiek uznał, że warto poświęcić na łamanie jakiegokolwiek mojego hasła więcej niż kilka miesięcy. Nie wydaje mi się też, by ktoś chciał robić to maszyną przeznaczoną do oglądania seriali i śmiesznych kotów. Jeżeli ktoś się za to zabierze, raczej skorzysta z odpowiednio silnego sprzętu.

Co to jednak znaczy „odpowiednio silnego”? Jaka moc obliczeniowa jest dziś w zasięgu ręki? Wspomniałem wcześniej o Atminerze, jednak jest to maszyna już na poziomie sprzętowym przeznaczona do mielenia tylko jednej funkcji haszującej — SHA-256. Jej przydatność przy łamaniu innych skrótów może być dramatycznie mniejsza. Tym bardziej że poza mocą obliczeniową maszyny, na prędkość $v$ ma też wpływ dobór algorytmu i jego parametrów. Możemy się domyślić, że dla słabych haszy uzyskamy bardzo duże $v$ nawet na zwykłym PC, więc zmusi nas to do używania bardzo silnego hasła i jego zapamiętanie będzie dosyć trudne. Z kolei dla nowoczesnych wariacji <abbr title="Password-Based Key Derivation Function">PBKDF</abbr> nawet słabe hasło może zapewnić bezpieczeństwo. Prawdopodobnie dla największych wartości $v$ będziemy musieli polegać wyłącznie na menedżerze haseł, a jedynie w serwisach z silną kryptografią będziemy mogli sobie pozwolić na ręczne wpisywanie hasła.

Skoro jednak tak ciężko określić $v$, spróbujmy podejść do problemu od strony numerycznej i najpierw policzyć czas ataku dla różnych algorytmów haszujących, potem zaś wyciągnąć jakieś wnioski.

### Moc obliczeniowa

Od razu widzimy, że atakiem online praktycznie nie musimy zaprzątać sobie głowy, gdyż nawet zakładając brak _throttlingu_ (przez rok nieustannych prób logowania!) i&nbsp;100 prób na sekundę ($v = 100$) wystarczy entropia:

$H = log_2(2 \cdot 365,25 \cdot 24 \cdot 60 \cdot 60 \cdot 100) \approx 32{,}6$

Bądźmy jednak poważni i weźmy pod uwagę atak na haszowaną bazę haseł za pomocą jakiegoś konkretnego sprzętu. [Najnowsze doniesienia](https://twitter.com/Chick3nman512/status/1580712040179826688) o użyciu zestawu 8 kart graficznych RTX 4090 po overclockingu mówią o 184 tysiącach haszy na sekundę dla algorytmu bcrypt. Jest to jednak porządny, nowoczesny algorytm. W przypadku prostszych wersji <abbr title="NT LAN Manager">NTLM</abbr> używanego przez Microsoft do uwierzytelniania użytkowników, mamy już… 300 miliardów prób na sekundę. Tak, sześć rzędów wielkości gorzej! Mamy do dyspozycji dosyć bogaty [benchmark](https://gist.github.com/Chick3nman/32e662a5bb63bc4f51b847bb422222fd) tego zestawu, możemy więc przeliczyć czas ataku dla kilku zupełnie różnych algorytmów haszujących.

Ale na tym nie poprzestaniemy. Metoda wyceniania kosztu łamania hasła w jednostkach czasu, czyli TTC (_Time-To-Crack_), jest dosyć popularna, ale przecież, dysponując odpowiednią kwotą, można ten czas łatwo skrócić, zrównoleglając obliczenia. Użycie 128 wątków, skróci czas ataku 128 razy i osłabi nasze hasło o 7 bitów. Niektórzy proponują więc metodę [MTC (_Money-To-Crack_)](https://jacobegner.blogspot.com/2020/11/password-strength-in-dollars.html). [1Password](https://blog.1password.com/how-long-should-my-passwords-be/) w 2018 oszacował, że stosowana przez nich metoda haszowania jest na tyle skuteczna, że koszt złamania hasła 56-bitowego wyniesie w ich przypadku około 76 milionów USD. W zeszłym roku 1Password opublikował zresztą [bardzo ciekawy artykuł](https://blog.1password.com/cracking-challenge-update/), opisujący ogłoszenie konkursu, który pozwolił im oszacować koszt łamania haseł, który wyniósł około 6 USD za $2^{32}$ prób, co daje średni koszt 3USD za hasło 32-bitowe. Tak, hasło `g(F4%` warte jest około 3USD i to przy solidnym haszowaniu. Oczywiście, jako że mamy do czynienia z miarą logarytmiczną, każdy dodatkowy bit nie dodaje do kosztu 6USD, ale mnoży go przez dwa.

W oparciu o powyższe dane można zbudować sobie taką tabelę:

|Hasło                     |Moc   |MD5    |7-Zip     |bcrypt   |VC       |MTC       |
|:-------------------------|-----:|:------|:---------|:--------|:--------|:---------|
|123456                    |19,9 b| 0 s   |  0 s     |  5 s    |  5 min. | 0,00  USD|
|strzygla uszami           |26,6 b| 0 s   | 37 s     |  9 min. |  9 h    | 0,14  USD|
|Strzygla-uszami7          |31,9 b| 0 s   | 25 min.  |351 min. | 14 dni  | 5,59  USD|
|H^5F(a                    |39,4 b| 4 s   |  3 dni   | 45 dni  |  7 lat  | 1,03 kUSD|
|zieleni mnostwo widzialem |39,9 b| 6 s   |  4 dni   | 61 dni  | 10 lat  | 1,40 kUSD|
|Zieleni-mnostwo-widzialem8|45,2 b| 4 min.|171 dni   |  7 lat  |392 lata |55,88 kUSD|
|4r#dHD&6                  |52,6 b|11 h   | 78 lat   |  1 k-lat| 65 k-lat| 9,27 MUSD|
|dwa tygrysy lubia mak     |53,2 b|17 h   |117 lat   |  2 k-lat| 98 k-lat|13,97 MUSD|
|Dwa-tygrysy-lubia-mak5    |58,5 b|28 dni |  5 k-lat | 67 k-lat|  4 M-lat| 0,56 GUSD|
|4H@de-+od                 |59,1 b|44 dni |  7 k-lat |105 k-lat|  6 M-lat| 0,88 GUSD|

Mamy tutaj zestawione algorytmy: żałosny MD5, algorytm z archiwizera 7-Zip (zapewne AES-256), bcrypt w leciwej wersji SHA-1 oraz VeraCrypt na pełnej petardzie w trybie SHA-512 XTS-1024. Ostatnia kolumna to wycena MTC na bazie badań przeprowadzonych przez 1Password.

Od razu rzuca się w oczy przepaść między najgorszym a najlepszym algorytmem w zestawieniu. Jeżeli zakładamy, że nasz skrót będzie „chroniony” słabą funkcją, pozostaje nam tylko menedżer haseł i bardzo długie, losowe ciągi znaków. Nie mówcie, że słyszeliście to ode mnie, ale pokusiłbym się o optymistyczne założenie, że tak słabe funkcje nie są stosowane w poważnych serwisach, a więc, paradoksalnie, możemy użyć słabszego hasła, np. złożonego z trzech słów z modyfikacjami, do uwierzytelniania w sytuacji, gdy nie możemy użyć menedżera haseł. Widzimy, że od 40 bitów entropii czas łamania idzie w tygodnie, a nawet lata, a koszt przekracza tysiąc dolarów. Oczywiście, każdy musi sam sobie odpowiedzieć, czy jego konto nie jest warte więcej i czy nie potrzebuje dorzucić czwartego słowa.

### Nowa norma NIST

Jak niektórzy słusznie zauważą, nie musisz wierzyć facetowi przebranemu za <del>księdza</del> bezpiecznika. Sprawdźmy, więc co mówią bardziej aktualne normy <abbr title="National Institute of Standards and Technology">NIST</abbr>? [Rewizja 2 NIST 800-131A](https://csrc.nist.gov/publications/detail/sp/800-131a/rev-2/final) z 2019 roku stwierdza, że w systemach kryptograficznych na poziomie federalnym należy posługiwać się rozwiązaniami o mocy 112 bitów lub równoważnej (niektóre algorytmy wymagają więcej bitów, by zapewnić bezpieczeństwo na tym poziomie) i odwołuje sie do [NIST 800-57](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final), który w rewizji 5 z 2020, mówi, że od 2030 należy przejść na systemy 128-bitowe. Czy to oznacza, że potrzebujemy 18 krzaków, żeby czuć się bezpiecznie? Otóż… [NIST 800-63B w sekcji 5.1.1 Memorized Secrets](https://pages.nist.gov/800-63-3/sp800-63b.html#memsecret) podaje, że dla haseł wybieranych samodzielnie przez użytkownika wystarczy 8 znaków, a&nbsp;w&nbsp;przypadku sekretu generowanego losowo przez system wystarczy 6 znaków i może to być PIN złożony z samych cyfr! Daje to nam doprawdy znikomą moc:

$H = log_2(10^6) \approx 19{,}9$

O co tu chodzi? Otóż 112 bitów odnosi się do sekretu używanego np. do zaszyfrowania dysku. Nikt nie używa takiego sekretu wprost, bo wówczas zmiana hasła wymagałaby odszyfrowania i ponownego zaszyfrowania całego dysku, co mogłoby trwać godziny, a&nbsp;nawet dni. 112-bitowy sekret jest więc dostępny po podaniu hasła o znacznie mniejszej mocy, ale obwarowane jest to wieloma założeniami, o których mówiliśmy wcześniej: haszowanie hasła silnym algorytmem, _throttling_, sprawdzanie hasła pod kątem wycieków i łatwych do odgadnięcia fraz itp. Ponadto w ogóle użycie hasła jako jedynego składnika uwierzytelniania dozwolone jest tylko na najniższym poziomie bezpieczeństwa [AAL1](https://pages.nist.gov/800-63-3/sp800-63b.html#63bSec4-Table1). Potwierdza to nasze wcześniejsze przemyślenia --- w dobrze zaprojektowanych systemach można używać haseł o niewielkiej mocy. Ponadto dochodzi tu bardzo ważne założenie --- podniesienie poziomu bezpieczeństwa odbywa się nie przez wydłużanie hasła i dokładanie dodatkowych wymagań na użycie znaków specjalnych, ale przez dodanie do procesu uwierzytelniania dodatkowych składników, jak klucze sprzętowe, generatory tokenów itp.

Sprawa jest więc bardzo złożona i myślę, że rozsądnych odpowiedzi jest kilka i&nbsp;wszystko należy zacząć od „to zależy”. Od czego? Od tego, co ma być chronione przez nasze hasło, a przede wszystkim, czy chcemy je zapamiętać.

## Podsumowanie

Powyższy artykuł ma na celu wykazanie, że stosowanie znaków specjalnych w hasłach, mimo że zwiększa bezpieczeństwo, to nie jest ani niezbędne (można je zastąpić wydłużaniem hasła), ani wystarczające (łatwo stworzyć słabe hasło ze znakami specjalnymi). W tym celu liczyliśmy entropię haseł, musimy jednak pamiętać, że takie obliczenia mają sens przy dwóch podstawowych założeniach.

Po pierwsze przyjmujemy, że interesuje nas średni lub maksymalny czas łamania hasła. Nie zmienia to jednak faktu, że prawdopodobieństwo odgadnięcia nawet najsilniejszego hasła za pierwszym podejściem jest niezerowe. Hasło nigdy nie będzie w&nbsp;pełni bezpieczne.

Po drugie nasze obliczenia są prawdziwe tylko, gdy hasła są tworzone losowo, a&nbsp;ludzki umysł nie jest dobrym generatorem danych losowych! Nasze mózgi bardzo nie lubią losowości i braku przyczynowości, stąd, między innymi, tyle <a href="https://pl.wikipedia.org/wiki/Lista_b%C5%82%C4%99d%C3%B3w_poznawczych">błędów poznawczych</a>. Starałem się przyjąć ostrożne założenia przy ocenie haseł złożonych z wyrazów, gdzie losowość będzie szczególnie niska ze względu na chęć tworzenia łatwych do zapamiętania fraz. Przyjąłem, że dla języka polskiego mamy przestrzeń 10&nbsp;000 symboli, bo rozbudowana fleksja naszego języka będzie równoważyć chęć do zestawiania logicznych ciągów słów. Jest to jednak równie wiarygodne, jak inne analizy <abbr title="Instytut Chłopskiego Rozumu">IChR</abbr>. Jako ciekawostkę podam, że bardzo przydatna biblioteka do oceny mocy haseł [zxcvbn](https://github.com/dropbox/zxcvbn) traktuje dowolny ciąg znaków jako zbiór symboli z przestrzeni o rozmiarze 10, gdyż [zakłada, że są to ciągi generowane przez ludzi](https://github.com/dropbox/zxcvbn/issues/135). Tak, dla zxcvbn hasło `df*R(#mg` ma tak niską moc jak `54285546`!

Należy więc z rezerwą podchodzić do wartości bezwzględnych wyników naszych obliczeń, a skupiać się na zależnościach między nimi. Ponadto przy ocenie bezpieczeństwa haseł o określonej mocy należy pamiętać, że moc obliczeniowa komputerów wciąż rośnie, a łamanie haszy znakomicie się zrównolegla. Na szczęście, funkcje haszujące nie zostają w tyle, a współczesne <abbr title="Password-Based Key Derivation Function">PBKDF</abbr> mogą nawet automatycznie dostosowywać się do możliwości crackerów. Pozostaje tylko mieć nadzieję, że są one stosowane przez programistów.

Żartuję. Tak naprawdę należy stosować bardzo mocne hasła, gdy to tylko możliwe.

[^1]: Albo zaszyfrowane, ale przecież kod serwera ma gdzieś zapisany klucz szyfrujący hasła i umie je odszyfrować, więc to tylko jedno małe utrudnienie dla atakującego.
[^2]: Tomasz Zieliński, [Jak serwer sprawdza hasło, skoro nie przechowuje haseł, czyli rzecz o funkcjach skrótu](https://informatykzakladowy.pl/jak-serwer-sprawdza-haslo-skoro-nie-przechowuje-hasel-czyli-rzecz-o-funkcjach-skrotu/)
[^3]: Rada Języka Polskiego, [_Ile jest słów w języku polskim_](https://rjp.pan.pl/porady-jezykowe-main/1047-ile-jest-sow-w-jzyku-polskim)
[^4]: Mirosław Bańko, [_Ile słów zna przeciętny Polak?_](https://sjp.pwn.pl/poradnia/haslo/Ile-slow-zna-przecietny-Polak;2384.html)
[^5]: Który oprogramowywał wojskowe mainframe'y w czasie wojny w Wietnamie, ale to tylko clickbaitowa ciekawostka.
