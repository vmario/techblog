---
title: "Tworzenie prezentacji z reveal.js i Hugo"
date: 2025-04-09
draft: false
tags: [narzędzia, hugo, reveal.js]

fortune: "Opowiedz historię. Ludzkie mózgi są stworzone do słuchania historii."
motto:
  quote: "They may forget what you said, but they will never forget how you made them feel."
  cite: "Carl W. Buechner"
---

## Prezentacja jako strona WWW

Po głębszym namyśle ku własnemu zaskoczeniu muszę przyznać, że Microsoft PowerPoint jako narzędzie do tworzenia prezentacji jest nie tyle prostacki, ile właśnie zbyt bogaty. Gdyby go uprościć i&nbsp;dodać funkcję ucinania rąk po wrzuceniu na slajd więcej niż pięćdziesięciu słów[^1], odmieniłby życie wielu z&nbsp;nas na lepsze, szczególnie w&nbsp;momentach, gdy występujemy w&nbsp;roli słuchaczy. Owszem, PowerPoint posiada bardzo ciekawe funkcje. Obecnie potrafi konwertować odręczne bazgroły na kształty, np. konwertuje kartofla na okrąg, choć czasem wychodzi z&nbsp;tego przekrzywiona elipsa, ale to już moja wina, trzeba było się bardziej starać. Wprawdzie jest to średnio przydatne, bo tak naprawdę na prezentacjach najczęściej chcemy dodawać strzałki, ale jak tylko nauczymy się rysować je bez odrywania ręki i&nbsp;odpowiednio równo, i&nbsp;tak, żeby grot był proporcjonalny do linii, to PowerPoint przerobi taką prawie idealną strzałkę na całkiem idealną. Przyda się tu doświadczenie w&nbsp;rysunku technicznym. O&nbsp;ile ćwiczyliśmy go przez dwa lata myszką w&nbsp;Paincie.

Jeżeli chcemy rysować równania matematyczne, program radzi sobie za to całkiem dobrze, choć pierwiastek kwadratowy wychodzi bordowy (_sic_!). To oczywiście nikomu nie przeszkadza, bo jeżeli ktoś potrzebuje wstawić dużo równań do prezentacji, to jest już entuzjastą krzyżówek hetmańskich, czyli użytkownikiem LaTeX-owego [Beamera](https://ctan.org/pkg/beamer), który pozwala wyrazić się w&nbsp;ramach estetyki „schludnie, choć nasrane”. Docelowym formatem jest tu <abbr title="Portable Document Format">PDF</abbr>, więc odkąd przeglądarki internetowe nauczyły się obsługiwać te pliki, można taką prezentację otworzyć na każdym komputerze. Co prawda bez animacji między slajdami możemy mieć wrażenie, że stoimy przed audytorium w&nbsp;płóciennym worku z&nbsp;drewniakami na stopach, ale przynajmniej nie wybierzemy jakiegoś żenującego przejścia, od którego ludzie dostaną choroby lokomocyjnej.

[^1]: Po przekroczeniu trzydziestu powinien być kontrolny kopniak w&nbsp;tyłek. I&nbsp;należałoby to zapisać w&nbsp;jakiejś międzynarodowej konwencji.

Oprócz edytorów <abbr title="What You See Is What You Get">WYSIWYG</abbr> i&nbsp;szablonów LaTeX-owych jest jednak jeszcze trzecia droga — frameworki webowe, w&nbsp;których prezentacja ma postać strony WWW, niekoniecznie dostępnej _on-line_ (choć takie rozwiązanie przedstawiam poniżej). Znanym i&nbsp;lubianym przykładem jest [reveal.js](https://revealjs.com). Zalecany sposób instalacji przewiduje wykorzystanie menedżera pakietów [npm](https://www.npmjs.com), można jednak po prostu sklonować repozytorium, użyć którejś z&nbsp;przykładowych prezentacji z&nbsp;_boilerplatem_ w&nbsp;sekcji `head` oraz `body` i&nbsp;napisać slajdy z&nbsp;użyciem prostego <abbr title="HyperText Markup Language">HTML</abbr>-a lub Markdowna. Jeżeli znamy trochę <abbr title="Cascading Style Sheets">CSS</abbr>, możemy łatwo dodać kilka wodotrysków w&nbsp;postaci animacji, kolorów, wykresów czy ciekawszego formatowania tekstu, zaś znajomość JavaScriptu daje nam właściwie nieograniczone możliwości.

Formatem docelowym jest strona WWW[^2], którą można wygodnie obsługiwać zarówno myszką, jak i&nbsp;klawiaturą. Pewną wadą jest fak, że kończymy z&nbsp;masą plików, które towarzyszą naszemu głównemu plikowi `*.html`, ale właściwie, czym się różni skopiowanie na pendrive'a całego katalogu zamiast pojedynczego pliku `*.pdf` czy `*.pttx`? Otóż różnica polega na tym, że nie musimy niczego kopiować na pendrive'a, ale o&nbsp;tym za chwilę.

[^2]: Istnieje sposób na eksport prezentacji do PDF-a, ale jest to rozwiązanie trikowe, na dodatek pozbawiające nas przejść między slajdami, i&nbsp;wydaje mi się ostatecznością, po którą musimy sięgnąć, jeżeli mamy obowiązek dostarczyć slajdy w&nbsp;postaci papierowej.

## Wykorzystanie generatora stron statycznych

Skoro mamy prezentację w&nbsp;formie strony WWW, dlaczego by nie wrzucić jej po prostu do Internetu? Będzie wówczas dostępna na każdym komputerze podłączonym do Sieci. A&nbsp;gdyby wykorzystać do tego generator stron statycznych, np. [Hugo](https://gohugo.io/)? Otrzymamy wówczas nowe możliwości, szczególnie korzystne w&nbsp;przypadku przygotowywania cyklu prezentacji. Możemy łatwo użyć do każdej z&nbsp;nich tego samego zestawu CSS i&nbsp;konfiguracji reveal.js, zachowując zasadę <abbr title="Don't Repeat Yourself">DRY</abbr>. Prawdziwym udogodnieniem jest jednak możliwość użycia systemu szablonów i&nbsp;zdefiniowanie własnych elementów, których używamy często na slajdach. Dzięki temu nawet fikuśne wynalazki, które pieczołowicie wysmarowaliśmy w&nbsp;HTML-u, możemy łatwo użyć powtórnie. A&nbsp;ponieważ mówimy o&nbsp;generatorze stron statycznych, otrzymamy na wyjściu pliki, które można zarówno hostować w&nbsp;Sieci, jak i&nbsp;skopiować na pendrive'a i&nbsp;otwierać lokalnie. Zatem do roboty!

## Środowisko pracy z Hugo

### Instalacja i konfiguracja

Zaczynamy od instalacji Hugo, który powinien być dostępny w&nbsp;większości popularnych dystrybucji (choć niekoniecznie w&nbsp;najnowszej wersji, bo rozwój tego programu jest bardzo dynamiczny). Następnie tworzymy katalog `slides-site`, a&nbsp;w nim plik konfiguracyjny `hugo.toml`. Nie używam komendy `hugo new site`, bo nie będziemy potrzebować całej struktury katalogów.

W konfiguracji wyłączamy nieużywane sekcje strony, aby Hugo nie krzyczał na nas, że brakuje mu szablonów, które nam nie są potrzebne. Włączamy za to względne ścieżki do plików, dzięki czemu wygenerowane zasoby da się otworzyć w&nbsp;przeglądarce np. z&nbsp;pendrive'a.

{{% code lang="toml" file="examples/hugo.toml" /%}}

### Szablon

Tworzymy katalog `layouts/_default`, a&nbsp;w nim plik `single.html`, czyli najważniejszy plik w&nbsp;projekcie — główny szablon wszystkich prezentacji:

{{% code lang="go-html-template" file="examples/single.html" lines="\"21-26\" \"30-42\"" /%}}

Oprócz [_boilerplate'a_ reveal.js](https://github.com/hakimel/reveal.js/blob/master/index.html) zawiera on kilka ulepszeń (podświetlone linie):

- skrypt z&nbsp;konfiguracją;
- własny arkusz stylów;
- automatycznie generowany slajd tytułowy, wspólny dla wszystkich prezentacji;
- miejsce na treść, którą Hugo wstawi z&nbsp;oddzielnego pliku.

Tutaj można też wstawić pluginy. Polecam [_chalkboard_](https://github.com/rajgoel/reveal.js-plugins/tree/master/chalkboard), który warto dodać do prezentacji, jeżeli będziemy ją przedstawiać, mając dostęp do myszki — umożliwi nam rysowanie po slajdach.

### Skrypty i style

Skrypt konfigurujący reveal.js i&nbsp;pluginy zapisujemy w&nbsp;pliku `static/scripts/configuration.js`:

{{% code lang="js" file="examples/configuration.js" /%}}

Style umieszczamy w&nbsp;`assets/styles/main.sass`. Użyłem ich do zwiększenia wysokości bloku kodu na slajdzie:

{{% code lang="sass" file="examples/main.sass" /%}}

Tu widać korzyść z&nbsp;użycia Hugo — możemy wspierać się preprocesorem [<abbr title="Syntactically awesome style sheets">Sass</abbr>](https://sass-lang.com), dzięki czemu pisanie większych arkuszy stylów staje się całkiem znośne.

### Shortcodes

Teraz coś jeszcze bardziej przydatnego — _shortcodes_, czyli swego rodzaju snippety, które umożliwią łatwe wstawienie powtarzających się elementów na stronę, czy raczej — w&nbsp;naszym przypadku — prezentację. Pliki umieszczamy w&nbsp;`layouts/shortcodes`.

Nowa część prezentacji z&nbsp;nagłówkiem poziomu `h2` (`part.html`):
{{% code lang="go-html-template" file="examples/part.html" /%}}

Standardowy slajd z&nbsp;nagłówkiem poziomu `h3` (`slide.html`):
{{% code lang="go-html-template" file="examples/slide.html" /%}}

Slajd z&nbsp;listą wypunktowaną, która będzie stopniowo odsłaniania (`ul-slide.html`):
{{% code lang="go-html-template" file="examples/ul-slide.html" /%}}

Element listy wypunktowanej (`lf.html`):
{{% code lang="go-html-template" file="examples/lf.html" /%}}

I najbardziej zaawansowany _shortcode_ — listing z&nbsp;płynnymi przejściami między wskazanymi fragmentami, i&nbsp;możliwością pobrania treści z&nbsp;zewnętrznego pliku (`code.html`):
{{% code lang="go-html-template" file="examples/code.html" /%}}

{{< figure src="slide-listing.webp" link="slide-listing.webp" title="Listing z kolorowaniem składni i podświetleniem fragmentu kodu" >}}

### Dodanie reveal.js

W katalogu `static/reveal.js` umieszczamy kod reveal.js, rozpakowując tam pobrane [archiwum z&nbsp;najnowszą wersją](https://github.com/hakimel/reveal.js/archive/master.zip), klonując repozytorium czy korzystając z&nbsp;submodułów Git.

Środowisko pracy jest już gotowe.

## Wydanie i publikacja

### Przykładowa prezentacja

Treść prezentacji umieszczamy w&nbsp;`content/slides-hello/index.html` wraz z&nbsp;jakimś kawałkiem kodu `example.py`.

Dodajemy dwa slajdy z&nbsp;treścią i&nbsp;dwa z&nbsp;tytułami części prezentacji. Slajd tytułowy zostanie wygenerowany automatycznie na podstawie metadanych opisanych w&nbsp;<abbr title="YAML Ain't Markup Language">YAML</abbr>-u i&nbsp;oddzielonych od treści znacznikami (`---`):

{{% code file="examples/index.html" /%}}

{{< figure src="slide-title.webp" link="slide-title.webp" title="Slajd tytułowy generowany z metadanych" >}}

Przykładowy kod w&nbsp;Pythonie nie ma większego znaczenia i&nbsp;służy tylko zaprezentowaniu możliwości wyświetlania listingów i&nbsp;pokazaniu, że omawiany kod można trzymać jako samodzielny plik, który można uruchamiać, testować i&nbsp;poprawiać, a&nbsp;zmodyfikowana zawartość będzie automatycznie aktualizowana na prezentacji, zgodnie z&nbsp;zasadą DRY.

{{% code lang="python" file="examples/example.py" /%}}

### Wygenerowanie treści

Po uruchomieniu serwera Hugo:

```
hugo server
```

możemy obejrzeć prezentację w&nbsp;przeglądarce pod adresem [http://localhost:1313/slides-test](http://localhost:1313/slides-test). Należy zwrócić uwagę, że bezpośrednio pod adresem [http://localhost:1313](http://localhost:1313) nie mamy nic, gdyż nie stworzyliśmy strony głównej. Możemy ją dodać, jeżeli potrzebujemy indeksu prezentacji dla własnej wygody lub w&nbsp;celu publikacji większej liczby prezentacji w&nbsp;Sieci.

### Publikacja

Jeżeli prezentacja wygląda tak, jak chcemy, generujemy wersję do publikacji za pomocą:

```
hugo
```

i kopiujemy katalog `public` na pendrive'a[^3]. Do pokazu będziemy potrzebowali tylko przeglądarki internetowej. Sam dostęp do Sieci nie będzie nam potrzebny.

[^3]: W&nbsp;praktyce różnica między zasobami wygenerowanymi przez `hugo` i&nbsp;`hugo server` jest w&nbsp;omawianym przypadku nieistotna i&nbsp;sprowadza się głównie do skryptu odświeżającego stronę po edycji plików źródłowych, który jest wstrzykiwany przez `hugo server`, a&nbsp;który nie jest potrzebny po zakończeniu pracy nad treścią.

Jeżeli chcemy przesłać nasze działo e-mailem, możemy je spakować np. 7-Zip-em:

```
7z a slides.7z public/
```

Owszem, nie jest to tak zgrabne jak PDF, ale w&nbsp;zasadzie, po co komuś wysyłać prezentację, którą możemy opublikować _on-line_? W&nbsp;tym celu wystarczy np. wrzucić kod na [GitHuba](https://github.com), a&nbsp;potem uruchomić hosting na serwerze [Netlify](https://www.netlify.com), który obsługuje Hugo i&nbsp;sam będzie budował nasze prezentacje. Wszystko za darmo.

### Archiwum z przykładem

Dla zainteresowanych załączam archiwum [slides-site.tar.xz](slides-site.tar.xz) ze źródłami i&nbsp;zbudowaną prezentacją.

## Podsumowanie

Mnie powyższe rozwiązanie sprawdziło się bardzo dobrze. Prezentacji dostępnej w&nbsp;sieci nie da się zgubić, za to bardzo łatwo udostępnić ją zainteresowanym. Problem może się pojawić tylko, jeśli komputer, z&nbsp;którego będziemy prowadzić wykład czy szkolenie, nie będzie miał połączenia z&nbsp;Internetem. Wydaje mi się jednak, że wraz z&nbsp;upływem lat prawdopodobieństwo braku Internetu spada, prawdopodobieństwo problemu z&nbsp;rzutnikiem pozostaje stałe, a&nbsp;krzywe te chyba już się przecięły na korzyść połączenia z&nbsp;Siecią.
