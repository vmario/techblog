---
title: "Tworzenie dokumentów z Pandoc i Eisvogel"
date: 2025-02-25
draft: false
tags: [typografia, latex, pandoc]

fortune: "Młody człowieku, w matematyce nie ma nic do zrozumienia, trzeba się po prostu przyzwyczajać."
motto:
  quote: "Są dwie przyczyny, z powodu których powinien Pan swą „funkcję niepewności” nazwać entropią. Pierwszą z nich jest to, że funkcja taka jest już używana w mechanice statystycznej i tak właśnie się nazywa, a drugą, być może ważniejszą, jest to, że nikt tak dokładnie nie wie czym właściwie jest entropia, stąd też we wszystkich dyskusjach będzie Pan miał zawsze przewagę."
  cite: "John von Neumann"
---

## Wprowadzenie do Pandoca

[Pandoc](https://pandoc.org) jest **bardzo** wszechstronnym narzędziem do konwersji dokumentów między różnymi formatami. Najbardziej znany jest z transformacji plików tekstowych w formacie [Markdown](https://daringfireball.net/projects/markdown/) z wmieszanym [LaTeX-em](https://www.latex-project.org) w <abbr title="Portable Document Format">PDF</abbr> i <abbr title="Electronic Publication">EPUB</abbr>, przy której szczególnie uwidacznia się jego zdolność do zamiany prostych formatów w bardzo złożone przy niewielkim zaangażowaniu użytkownika.

Wadą Pandoca, przynajmniej na Arch Linuksie, jest masa bardzo często aktualizowanych haskellowych zależności. Po zainstalowaniu pakietu ze standardowego repozytorium miałem wrażenie, że aktualizacje systemowe zajmują się głównie odświeżaniem Pandoca i jego zależności. Rozwiązałem to, instalując z <abbr title="Arch User Repository">AUR</abbr> wersję skompilowaną z&nbsp;zależnościami, czyli <a href="https://aur.archlinux.org/packages/pandoc-bin">pakiet `pandoc-bin`</a>, zajmujący na dysku około 147&nbsp;MiB.

Niestety, to jest dopiero początek okupowania dysku, bowiem głównym silnikiem Pandoca służącym do renderowania PDF-ów jest, jakżeby inaczej, LaTeX. Ten zajmuje u mnie blisko 2&nbsp;GiB, z czego lwią część stanowią dodatkowe fonty. Tu jednak nie szukałem żadnych optymalizacji. Pogodziłem się z faktem, że gdy wyrzucę LaTeX-a drzwiami, wróci oknem. Zbyt dobrze działa.

## Prosty przykład

Weźmy teraz plik, prezentujący podstawowe formatowanie Markdown[^1]. Na początku dorzucimy metadane w języku <abbr title="YAML Ain't Markup Language">YAML</abbr>, zgodnie z jego standardem zamknięte między znacznikami początku (`---`) i końca (`...`) dokumentu (z punktu widzenia YAML-a metadane są dokumentem samym w sobie). Są to głównie typowe metadane dokumentu tekstowego, opisujące tytuł czy autora, ale też wskazówki odnośnie procesu konwersji:

    ---
    title: "Lorem ipsum"
    subtitle: "Dolor sit amet"
    footer-left: "Consectetur adipiscing elit"
    author: [Mariusz Chilmon <<vmario@vmario.org>>]
    lang: "pl"
    titlepage: yes
    colorlinks: yes
    ...

    > Talk is cheap. Show me the code.
    >
    > — _Linus Torvalds_

    # Rozdział

    ## Podrozdział

    ,,Zażółć gęślą jaźń''.

    Lorem ipsum dolor --- sit amet,
    [consectetur](https://example.com) adipiscing elit[^1].
    _Vestibulum_ **placerat** ***erat*** `quis` vulputate consequat.

    Pellentesque dui turpis:

    * tincidunt vel sapien eget,
    * feugiat consequat nunc.

    In ultricies augue ut arcu maximus dapibus:

    1. In non eleifend sapien.
    2. Nullam facilisis id nibh vitae rhoncus.

    [^1]: Vestibulum ut mollis libero.

    | Quisque in          | Varius lacus             |
    |---------------------|--------------------------|
    | proin semper        | lacus in massa           |
    | tincidunt hendrerit | mauris quis tellus lorem |

    ```c++
    #include <iostream>
    #include <vector>

    using namespace std;

    // Example code.
    int main() {
        const vector<int> NUMBERS{42, 43};

        for (const auto& number : NUMBERS) {
            [](int n){ cout << n << " "; }(number);
        }

        return EXIT_SUCCESS;
    };
    ```

[^1]: OK, nie tak całkiem podstawowe, bo dorzuciłem trochę LaTeX-owej typografii, ale naprawdę niewiele.

Kompilujemy to prostą komendą, przekazującą przy okazji datę kompilacji, czyli jeszcze jedną metadaną:

```
pandoc simple.md -o simple-generic.pdf --metadata date="$(date +%F)"
```

{{< figure src="simple-generic.webp" link="simple-generic.pdf" title="Efekt domyślnej konwersji do PDF" >}}

<a href="simple-generic.pdf">Efekt</a> cechuje się typową dla LaTeX-a schludnością. Szeryfowy font nie sprzyja jednak czytaniu z ekranu, a całość, poza ładnie pokolorowanym kodem, nastraja czytelnika podobnie jak błoto pośniegowe w Wigilię Bożego Narodzenia.

## Szablon Eisvogel

Tu przychodzi z pomocą szablon [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) zaprojektowany do tworzenia materiałów dydaktycznych, szczególnie z zakresu IT. Myślę, że nada się też znakomicie do różnego rodzaju raportów, sprawozdań i dokumentacji technicznych. Zestaw [przykładów](https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master/examples) pokazuje, że twórcy zadbali o implementację szeregu istotnych funkcji. Najważniejsze jednak, że za chwilę nasz dokument będzie się prezentował znacznie ciekawiej, wciąż zachowując elegancję.

Arch Linux ma ten pakiet w AUR, a po instalacji wystarczy do wywołania Pandoca dopisać argument `--template eisvogel` i, ewentualnie, opcję `--listings`, jeżeli chcemy uzyskać inny wygląd bloków kodów --- właściwie to nawet mniej kolorowy niż w wersji generycznej, ale za to z dodatkowym wyróżnieniem.

```
pandoc simple.md -o simple-eisvogel.pdf --metadata date="$(date +%F)" --template eisvogel --listings
```

I to wszystko. Otrzymujemy znacznie nowocześniej wyglądający <a href="simple-eisvogel.pdf">dokument</a>. Moim zdaniem, poza tabelkami, prezentuje się to znakomicie.

{{< figure src="simple-eisvogel.webp" link="simple-eisvogel.pdf" title="Efekt konwersji z użyciem szablonu Eisvogel" >}}

Zainstalowawszy Pandoca, LaTeX-a i Eisvogel otrzymujemy zatem narzędzie, którym możemy stworzyć zgrabnego PDF-a pisząc w Markdownie. Ponieważ wejściem jest plik tekstowy, możemy cały proces zautomatyzować wedle potrzeby, w skrajnym przypadku generując dokument całkowicie automatycznie.

Jeżeli ktoś nie chce instalować całego środowiska pracy, może wykorzystać <a href="https://hub.docker.com/r/pandoc/extra">obraz Dockera</a>.

## Dodatkowe możliwości

Prostota, estetyka i możliwość oprogramowania to nie jedyne zalety powyższego zestawu narzędzi. Skoro już ściągnęliśmy cały ten kram na dysk, możemy skorzystać z&nbsp;bogactwa LaTeX-a, dającego możliwości przeogromne w porównaniu z procesorami tekstu takimi jak Microsoft Word. Oczywiście, tracimy przy tym wygodę, jaką daje <abbr title="What You See Is What You Get">WYSIWYG</abbr>, ale dostajemy wiele w zamian. Wprawdzie czasem wypozycjonowanie obiektu na stronie przyprawia o siwiznę włosów, ale za to żonglując ukośnikami i nawiasami sześciennymi dostajemy _out of the box_ możliwość rysowania diagramów, włącznie z typowymi dla elektroniki cyfrowej przebiegami czasowymi, pisania dowolnie skomplikowanych równań, czy… osadzenia wyświetlacza alfanumerycznego (włącznie z samodzielnie zdefiniowanymi znakami!). Biorąc pod uwagę bogactwo materiałów na temat LaTeX-a i wsparcie <abbr title="Artificial Intelligence">AI</abbr>, korzystanie z tych zaawansowanych funkcji nie jest tak bardzo skomplikowane, jak mogłoby się wydawać.

Weźmy na tapet <a href="complex.pdf">dokument</a> zawierający:

1. blok komentarza ozdobiony ikoną z <a href="https://ctan.org/pkg/fontawesome">zestawu `fontawesome`</a>,
1. wyświetlacz alfanumeryczny,
1. wzór matematyczny,
1. listing pseudokodu z komentarzami,
1. przebieg czasowy,
1. graf.

Możemy go uzyskać za pomocą poniższego kodu:

    ---
    lang: "pl"
    header-includes: |
      \usepackage{awesomebox}
      \usepackage{algorithm}
      \usepackage{algpseudocode}
      \usepackage{tikz}
      \usetikzlibrary{automata, positioning, arrows, shapes, patterns}
      \usepackage{tikz-timing}
      \usepackage{lcd}
      \LCDcolors[MidnightBlue]{MidnightBlue!10}{MidnightBlue!80}
    ...

    \tikzset{
        >=stealth',
        node distance=2.8cm,
        every state/.style={thick, fill=gray!20, align=center, text width=1.1cm},
        auto,
        font=\footnotesize,
    }

    # Blok komentarza

    \awesomebox[teal]{2pt}{\faBook}{teal}{
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Morbi eu nulla quis tortor ullamcorper porta.
        Interdum et malesuada fames ac ante ipsum primis in faucibus.
        \lstinline{int foo(42)}.
    }

    # Wyświetlacz alfanumeryczny

    Nunc nec risus at est \textLCD[0]{15}+commodo feugiat+ ac at metus. Integer consequat blandit metus quis dignissim. Donec hendrerit mi vitae euismod suscipit. Curabitur facilisis libero a aliquet molestie.

    \DefineLCDchar{degree}{00010001010001000000000000000000000}
    \begin{center}
    \LCD{2}{16}
        |2025-02-19 15:07|
        |Temp: 36.6{degree}C|
    \captionof{figure}{Wyjściowy stan wyświetlacza}
    \end{center}

    # Równanie

    \begin{equation}
    SMA_k = \frac{1}{k} \sum^n_{i=n-k+1} p_i = \frac{p_{n-k+1} + p_{n-k+2} + \cdots + p_{n}}{k}
    \end{equation}

    # Pseudokod

    \begin{algorithm}
    \caption{Średnia krocząca $SMA_{size}$}
    \begin{algorithmic}[1]
        \State $measures_{index}\gets \Call{adc.temperature}$
        \Comment{zapis bieżącego pomiaru}
        \State $sum \gets 0$
        \For{$i \gets 0$ to $size$}
        \Comment{sumowanie wszystkich $size$ ostatnich pomiarów}
            \State $sum \gets sum + measures_i$
        \EndFor
        \State $index\gets index + 1$
        \Comment{obliczamy kolejny indeks w tablicy $measures$}
        \If{$index \geq size$}
        \Comment{pilnujemy, by nie przekroczyć rozmiaru tablicy}
            \State $index\gets 0$
        \EndIf
        \State \Return {$\frac{sum}{size}$}
        \Comment{zwracamy średnią}
    \end{algorithmic}
    \end{algorithm}

    # Przebieg czasowy

    \begin{figure}[h]
        \centering
        \begin{tikztimingtable}
            Przepełnienia timera 1 & L N(T0) G 10L G 10L G 9L [violet]; L [violet, dotted] \\
            Flaga \texttt{TOV1} & L N(F0) 4H N(F2) 6L 4H 6L 4H 5L; L [dotted] \\
            Pomiar ADC & L N(A0) 2H N(A1) 8L 2H 8L 2H 7L [darkgray]; L [darkgray, dotted] \\
            Przerwanie ADC & L 2L N(B1) G 8L 2L G 8L 2L G 7L [violet]; L [violet, dotted] \\
            Obsługa przerwania ADC & L 2L N(C1) H N(C2) H N(C3) 6L 2L H H 6L 2L H H 5L [darkgray]; L [darkgray, dotted] \\
            Konfiguracja \texttt{ADMUX} & 4D{Kanał A0} N(M2) 10D{Kanał A5} 10D{Kanał A0} 6D; [dotted] D{Kanał A5} \\
            Wynik \texttt{ADCH} & 3U N(H1) 10D{Pomiar A0 --- MSB} 10D{Pomiar A5 --- MSB} 7D; [dotted] D{Pomiar A0 --- MSB} \\
            Wynik \texttt{ADCL} & 3U N(L1) 10D{Pomiar A0 --- MSB} 10D{Pomiar A5 --- LSB} 7D; [dotted] D{Pomiar A0 --- LSB} \\
            \extracode
            \tablerules
            \draw
                (T0) edge[->, magenta, bend right] (F0)
                (F0) edge[->, magenta, bend right] (A0)
                (A1) edge[->, magenta, bend right] (B1)
                (A1) edge[->, magenta, bend right] (H1)
                (A1) edge[->, magenta, bend right] (L1)
                (B1) edge[->, magenta, bend right] (C1)
                (C2) edge[->, magenta, bend left] (M2)
                (C3) edge[->, magenta, bend right] (F2)
            ;
        \end{tikztimingtable}
        \caption{Zależności czasowe przy zmianie kanałów ADC}
    \end{figure}

    # Graf

    \begin{figure}[h]
        \centering
        \begin{tikzpicture}
            \node[state, initial, initial text=start] (main) {\texttt{main()}};
            \node[state, below of=main] (loop) {\texttt{main-Loop()}};
            \node[state, right=of main] (k0) {pomiar $k_0$};
            \node[state, right of=k0, draw=blue, text=blue] (k1) {pomiar $k_1\dots k_{n}$};
            \node[state, below of=k1] (t0) {pomiar $t_0$};
            \node[state, left of=t0, draw=blue, text=blue] (t1) {pomiar $t_1$};
            \node[rectangle, draw, below of=t1, thick, pattern=dots, pattern color=gray, align=center, text width=2cm] (global) {zmienne globalne};
            \draw
                (main) edge[->] node{} (loop)
                (loop) edge[loop below] node{} ()
                (main) edge[->] node{\texttt{SEI}} (k0)
                (k0) edge[->] node{\texttt{ISR}} (k1)
                (k1) edge[->] node{ISR} (t0)
                (t0) edge[->] node{\texttt{ISR}} (t1)
                (t1) edge[->] node{\texttt{ISR}} (k0)
                (k1) edge[->, dashed, bend left=60, looseness=1.5] node{zapis} (global)
                (k1) edge[loop right, blue] node{\texttt{ISR}} (global)
                (t1) edge[->, dashed] node{zapis} (global)
                (global) edge[->, bend left, dashed] node{odczyt} (loop)
            ;
        \end{tikzpicture}
        \caption{Maszyna stanów uwzględniająca czas przełączania kanałów}
    \end{figure}

Dla osoby nieznającej LaTeX-a przypomina to bigos ze wmieszanymi zszywkami, ale czy wystruganie diagramu czasowego w Inkscape albo Microsoft Visio byłoby prostsze? Nie wydaje mi się. A wprowadzanie jakichkolwiek poprawek na takim diagramie albo stworzenie tuzina wersji dla różnych zagadnień na pewno jest łatwiejsze w formie tekstowej.

{{< figure src="complex.webp" link="complex.pdf" title="Może to nie jest proste, ale czy Wasz Word to potrafi?" >}}
