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

## Wprowadzenie do Pandoca

[Pandoc](https://pandoc.org) jest **bardzo** wszechstronnym narzędziem do konwersji dokumentów między różnymi formatami. Najbardziej znany jest z konwersji plików tekstowych w formacie [Markdown](https://daringfireball.net/projects/markdown/) z wmieszanym [LaTeX-em](https://www.latex-project.org) na <abbr title="Portable Document Format">PDF</abbr> i <abbr title="Electronic Publication">EPUB</abbr>, przy której szczególnie uwidacznia się jego zdolność do zamieniania prostych formatów w bardzo złożone przy niewielkim zaangażowaniu użytkownika.

## Prosty dokument

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

    | Quisque in          | varius lacus             |
    |---------------------|--------------------------|
    | Proin semper        | lacus in massa           |
    | tincidunt hendrerit | Mauris quis tellus lorem |

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

