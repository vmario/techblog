---
title: "Spłaszczanie struktury kodu i danych"
date: 2023-09-15
draft: false
tags: [meta]

fortune: "XXX"
motto:
  quote: "Any intelligent fool can make things bigger and more complex. It takes a touch of genius — and a lot of courage — to move in the opposite direction."
  cite: "E.F. Schumacher"
---

Jako osobowość typu porządkującego, zobaczywszy w Zen of Python zalecenie:
```
Flat is better than nested.
```
poczułem pewien wewnętrzny sprzeciw. Wszak nawet sam Python ma hierarchię modułów zebranych w pakiety. Pliki na dyskach są rozmieszczone w strukturach drzewiastych, nieraz o niemałym stopniu zagnieżdżenia. Dane, na których operują algorytmy, też są umieszczane w różnego rodzaju drzewiastych strukturach. Skąd więc zalecenie spłaszczania struktur?

Wielu, a może nawet większość, programistów tłumaczy to zalecenie, odnosząc je nie do danych, ale do [struktury kodu](https://en.wikibooks.org/wiki/Computer_Programming/Coding_Style/Minimize_nesting) (twierdząc nawet, że odnosi się ono wyłącznie do kodu). Wówczas staje się ono oczywiste. Warto tu wspomnieć chociażby o historii rozwoju programu [DiffMerge](https://sourcegear.com/diffmerge/???), który borykał się z masą błędów po fazie gwałtownego rozwoju w 2004 roku. Duża część kodu zyskała wówczas poziom zagnieżdżenia instrukcji _if_ powyżej 3 (co wcześniej się w tym kodzie praktycznie nie zdarzało) przy jednoczesnym podwojeniu liczby tych instrukcji. Choć autorzy nie przesądzają o całkowitej winie zagnieżdżenia kodu, to uznają je za bardzo ważny czynnik, tym bardziej, że dopiero po obniżeniu zagnieżdżenia w 2006 roku udało się odzyskać jakość tego oprogramowania. Zastąpiono wtedy głęboko zagnieżdżone instrukcje warunkowe instrukcjami switch działającej na specjalnie zaprojektowanej tablicy decyzyjnej, czytelnej dla człowieka. Problem z wielopoziomowymi instrukcjami switch nie polega bowiem na nieefektywności, ale na niezrozumiałości dla programisty, który musi utrzymywać w umyśle cały zestaw zagnieżdżonych instrukcji jednocześnie. [^1]

Można jednak spróbować odnieść zalecenie spłaszczania struktury także do danych. Organizując w pracy maile w skrzynce pocztowej, zauważyłem, że utrzymywanie zagnieżdżonej struktury jest na dłuższą metę bardzo problematyczne. Maile miałem rozmieszczone w drzewie, które uwzględniało sprawy administracyjne różnego rodzaju, projekty, szkolenia, wymianę informacji z podmiotami współpracującymi. Z biegiem lat okazywało się, że są wiadomości, które pasują do wielu katalogów, bo związane są z kilkoma projektami czy łączą w sobie tematy projektowe z administracyjnymi. Były też takie, które trudno było w ogóle przyporządkować do jakiegoś miejsca w hierarchii. Oba typy maili, które koniec końców musiały wylądować w którymś katalogu, rodziły problemy z ich odnalezieniem, bo po pół roku często nie miałem pomysłu na to, jaką decyzję odnośnie przyporządkowania danego maila podjąłem. Oczywiście, wówczas z pomocą przychodziła wyszukiwarka i okazywało się, że misternie zbudowane przeze mnie drzewo katalogów ma użyteczność niewielką w porównaniu z odpowiednio sprytną i szybką wyszukiwarką.

Zauważyłem to zresztą, korzystając z Gmaila, który, rzecz jasna, ma znakomitą wyszukiwarkę. Gmail umożliwia oznaczanie maili etykietami (organizowanymi przeze mnie w drzewo, a jakże!), ale mają one charakter tagów, tj. do wiadomości można przypisać dowolną liczbę etykiet, włączając w to zero. Etykiety, zwłaszcza przypisywane automatycznie, umożliwiają szybszą identyfikację tematyki maili na długiej liście, ale głównym narzędziem do znajdowania interesującej mnie wiadomości jest wyszukiwarka.

Z biegiem lat stosowane przeze mnie struktury danych zaczynają więc stawać się płytsze, szczególnie tam, gdzie mogę posiłkować się sprawną wyszukiwarką. Zamiast poświęcać czas mojego mózgu na organizację drzew, deleguję to zadanie do komputera, który na żądanie odnajduje to, czego potrzebuję. W końcu to on jest od żmudnej pracy. W ten sposób ruguję główne problemy z zagnieżdżonymi strukturami:
- obiekty mogą pasować do kilku gałęzi,
- czasem ciężko przypisać obiekt do jakiejkolwiek gałęzi,
- im bardziej rozbudowana struktura, tym trudniej wymyślić, gdzie przyporządkowało się kiedyś obiekt.

Oczywiście, są przypadki, gdy struktury drzewiastej nie da się uniknąć, np. gdy:
- istnieje ograniczenie liczby elementów w kontenerze (np. plików w katalogu),
- brakuje możliwości sprawnego wyszukiwania (duże, złożone obiekty bez metadanych),
- często operuje się na ustalonych grupach obiektów.
Jeżeli przy tym obiekty da się łatwo przyporządkować do miejsca w złożonej strukturze, aż szkoda byłoby z niej nie skorzystać. W innych przypadkach warto pomyśleć o płaskiej strukturze.

[^1]: _Piękny kod. Tajemnice mistrzów programowania_, pod red. Andy'ego Orama i Grega Wilsona, Helion
