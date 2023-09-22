---
title: "Spłaszczanie struktury kodu i danych"
date: 2023-09-22
draft: false
tags: [programowanie, jakość kodu]

fortune: "One would not expect, therefore, that more than a small fraction of the current effort in research and development (R and D) will be switched into the new direction; but that small fraction, I am sure, is the price we have to pay if we wish to survive."
motto:
  quote: "Any intelligent fool can make things bigger and more complex. It takes a touch of genius — and a lot of courage — to move in the opposite direction."
  author: "Ernst Friedrich Schumacher"
  cite: "Small is Beautiful [in:] The Radical Humanist, Vol. 37, No. 5, p. 22"
---

## Spłaszczanie struktury kodu

Jako osobowość typu porządkującego, zobaczywszy w [The Zen of Python](https://peps.python.org/pep-0020/) zalecenie:
> Flat is better than nested.
>
> --- <cite>PEP20 — The Zen of Python</cite>

poczułem pewien wewnętrzny sprzeciw. Wszak nawet sam Python ma hierarchię modułów zebranych w pakiety. Pliki na dyskach są rozmieszczone w strukturach drzewiastych, nieraz o niemałym stopniu zagnieżdżenia. Dane, na których operują algorytmy, też są umieszczane w różnego rodzaju drzewiastych strukturach. Skąd więc zalecenie spłaszczania struktur?

Wielu, a może nawet większość, programistów tłumaczy tę regułę, odnosząc ją nie do danych, ale do [struktury kodu](https://en.wikibooks.org/wiki/Computer_Programming/Coding_Style/Minimize_nesting) i nierzadko twierdząc nawet, że odnosi się ona wyłącznie do kodu. Wówczas staje się ona oczywiste. Warto tu wspomnieć chociażby o historii rozwoju programu DiffMerge[^1], który borykał się z masą błędów po fazie gwałtownego rozwoju w 2004 roku. Duża część kodu zyskała wówczas poziom zagnieżdżenia instrukcji `if` powyżej 3 (co wcześniej się w tym kodzie praktycznie nie zdarzało) przy jednoczesnym podwojeniu liczby tych instrukcji. Choć autorzy nie przesądzają o całkowitej winie zagnieżdżenia kodu, to uznają je za bardzo ważny czynnik, tym bardziej, że dopiero po obniżeniu zagnieżdżenia w 2006 roku udało się odzyskać jakość tego oprogramowania. Zastąpiono wtedy głęboko zagnieżdżone instrukcje warunkowe instrukcjami `switch` działającymi na specjalnie zaprojektowanej tablicy decyzyjnej, czytelnej dla człowieka. Problem z wielopoziomowymi instrukcjami `switch` nie polega bowiem na nieefektywności, ale na niezrozumiałości dla programisty, który musi utrzymywać w umyśle cały zestaw zagnieżdżonych instrukcji jednocześnie[^2].

## Spłaszczanie struktury danych

Można jednak spróbować odnieść zalecenie spłaszczania struktury także do danych. Organizując w pracy maile w skrzynce pocztowej, zauważyłem, że utrzymywanie zagnieżdżonej struktury jest na dłuższą metę bardzo problematyczne. Maile miałem rozmieszczone w drzewie, które uwzględniało sprawy administracyjne różnego rodzaju, projekty, szkolenia, wymianę informacji z podmiotami współpracującymi, etc. Z biegiem lat okazywało się, że są wiadomości, które pasują do wielu katalogów, bo związane są z kilkoma projektami czy łączą w sobie tematy projektowe z administracyjnymi. Były też takie, które z kolei trudno było przyporządkować do jakiegoś miejsca w hierarchii. Oba typy maili, które koniec końców musiały wylądować w którymś katalogu, rodziły problemy z ich odnalezieniem, bo po pół roku często nie miałem pomysłu na to, jaką decyzję odnośnie przyporządkowania podjąłem. Oczywiście, wówczas z pomocą przychodziła wyszukiwarka i okazywało się, że misternie zbudowane przeze mnie drzewo katalogów ma użyteczność niewielką w porównaniu z odpowiednio sprytnym i szybkim algorytmem wyszukiwania.

Widziałem to szczególnie wyraźnie, korzystając z Gmaila, który, rzecz jasna, ma znakomitą wyszukiwarkę. Gmail umożliwia oznaczanie maili etykietami (organizowanymi przeze mnie w drzewo, a jakże!), ale mają one charakter tagów, tj. do wiadomości można przypisać dowolną liczbę etykiet, włączając w to zero. Etykiety, zwłaszcza przypisywane automatycznie, umożliwiają szybszą identyfikację tematyki maili na długiej liście, ale głównym narzędziem do znajdowania wiadomości jest wyszukiwarka.

Z biegiem lat stosowane przeze mnie struktury danych zaczynają więc stawać się płytsze, szczególnie tam, gdzie mogę posiłkować się sprawną wyszukiwarką. Zamiast poświęcać czas i energię mózgu na organizację drzew, deleguję to zadanie do komputera, który na żądanie odnajduje obiekty, których potrzebuję. W końcu to on jest od żmudnej pracy. W ten sposób ruguję główne problemy z zagnieżdżonymi strukturami:
- obiekty mogą pasować do kilku gałęzi,
- czasem ciężko przypisać obiekt do jakiejkolwiek gałęzi,
- im bardziej rozbudowana struktura, tym trudniej wymyślić, gdzie przyporządkowało się kiedyś obiekt.

Oczywiście, są przypadki, gdy struktury drzewiastej nie da się uniknąć, np. gdy:
- istnieje ograniczenie liczby elementów w kontenerze (np. plików w katalogu),
- brakuje możliwości sprawnego wyszukiwania (duże, złożone obiekty bez metadanych),
- często operuje się na ustalonych grupach obiektów (np. przetwarza cały katalog plików).

Jeżeli przy tym obiekty da się łatwo przyporządkować do miejsca w strukturze złożonej, aż szkoda byłoby z niej nie skorzystać. W innych przypadkach warto pomyśleć o strukturze płaskiej.

[^1]: Obecnie chyba program ten został zastąpiony przez [P4Merge](https://www.perforce.com/products/helix-core-apps/merge-diff-tool-p4merge), a w każdym razie nie mogę odnaleźć w Sieci programu DiffMerge od Preforce Software.
[^2]: Laura Wingerd i Christopher Seiwald, _Kod w ruchu_ [w:] _Piękny kod. Tajemnice mistrzów programowania_, pod red. Andy'ego Orama i Grega Wilsona, Helion 2008
