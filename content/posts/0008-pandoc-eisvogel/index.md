---
title: "Tworzenie dokumentów z Pandoc i Eisvogel"
date: 2025-02-19
draft: false
tags: [typografia, latex, pandoc]

fortune: "Młody człowieku, w matematyce nie ma nic do zrozumienia, trzeba się po prostu przyzwyczajać."
motto:
  quote: "Są dwie przyczyny, z powodu których powinien Pan swą „funkcję niepewności” nazwać entropią. Pierwszą z nich jest to, że funkcja taka jest już używana w mechanice statystycznej i tak właśnie się nazywa, a drugą, być może ważniejszą, jest to, że nikt tak dokładnie nie wie czym właściwie jest entropia, stąd też we wszystkich dyskusjach będzie Pan miał zawsze przewagę."
  cite: "John von Neumann"
---

## Kilka słów o Pandocu

[Pandoc](https://pandoc.org) jest **bardzo** wszechstronnym narzędziem do konwersji dokumentów między różnymi formatami. Najbardziej znany jest z konwersji plików tekstowych w formacie [Markdown](https://daringfireball.net/projects/markdown/) z wmieszanym [LaTeX-em](https://www.latex-project.org) na <abbr title="Portable Document Format">PDF</abbr> i <abbr title="Electronic Publication">EPUB</abbr>, przy której szczególnie uwidacznia się jego zdolność do zamieniania prostych formatów w bardzo złożone przy niewielkim zaangażowaniu użytkownika.

Wadą Pandoca, przynajmniej na Arch Linuksie, jest masa bardzo często aktualizowanych haskellowych zależności. Po zainstalowaniu pakietu ze standardowego repozytorium miałem wrażenie, że aktualizacje systemowe zajmują się głównie odświeżaniem Pandoca i jego zależności. Rozwiązałem to instalując z <abbr title="Arch User Repository">AUR</abbr> wersję skompilowaną z&nbsp;zależnościami, czyli <a href="https://aur.archlinux.org/packages/pandoc-bin">pakiet `pandoc-bin`</a>, zajmujący na dysku około 147&nbsp;MiB.

Niestety, to jest dopiero początek okupowania dysku, bowiem głównym silnikiem Pandoca służącym do renderowania PDF-ów jest, jakże by inaczej, LaTeX. Ten zajmuje u mnie blisko 2&nbsp;GiB, z czego lwią część stanowią dodatkowe fonty. Tu jednak nie szukałem żadnych optymalizacji. Obecnie jestem pogodzony z faktem, że gdy wyrzucę LaTeX-a drzwiami, wróci oknem. Zbyt dobrze działa.

## Prosty dokument

Weźmy teraz plik, prezentujący podstawowe formatowanie Markdown:

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

Kompilujemy to prostą komendą:

```
pandoc simple.md -o simple.pdf
```

Efekt cechuje się typową dla LaTeX-a schludnością. Szeryfowy font nie sprzyja jednak czytaniu z ekranu, a całość, poza ładnie pokolorowanym kodem, nastraja czytelnika podobnie jak błoto pośniegowe w Wigilię Bożego Narodzenia.

## Szablon Eisvogel

Tu przychodzi z pomocą szablon [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) zaprojektowany do tworzenia materiałów dydaktycznych, szczególnie z zakresu IT. Myślę, że nada się też znakomicie do różnego rodzaju raportów, sprawozdań i dokumentacji technicznych. Zestaw [przykładów](https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master/examples) pokazuje, że twórcy zadbali o implementację szeregu istotnych funkcji. Najważniejsze jednak, że za chwilę nasz dokument będzie się prezentował znacznie ciekawiej, wciąż zachowując elegancję.
