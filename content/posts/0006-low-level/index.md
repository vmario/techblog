---
title: "Podejście niskopoziomowe"
date: 2024-03-16
draft: false
tags: [programowanie]

fortune: "Teraz panowie widzą, że nic nie widać. A dlaczego nie widać, to zaraz panowie zobaczą."
motto:
  quote: "Jesteśmy biedni. Musimy myśleć."
  cite: "Ernest Rutherford"
---

## Problem

Niedawno przenosiłem pewien kod z jednego urządzenia na drugie. Była to biblioteka, dość dobrze wytestowana i&nbsp;sprawująca się na pierwszym urządzeniu bez zarzutu. Ponieważ docelowa platforma była praktycznie identyczna z pierwotną (zarówno procesor, jak i system operacyjny, były takie same), nie spodziewałem się większych problemów. Jednak po osadzeniu kodu na drugim urządzeniu, zaczęło się ono restartować po kilkunastu minutach pracy.

## Analiza behawioralna

Reprodukcję problemu ułatwiło trochę obciążenie programu dużą ilością danych, co zwiększało prawdopodobieństwo wystąpienia tajemniczego błędu — restart następował wówczas na ogół w pierwszych minutach pracy. W ten sposób jednak utknąłem na długo w analizie behawioralnej: starałem się zrozumieć, kiedy błąd występuje, żeby zlokalizować odpowiedzialny za niego fragment kodu, ale nie sposób było znaleźć jakąkolwiek głębszą zależność. Lekka korelacja między ilością przetwarzanych przez program danych a czasem reprodukcji błędu nie dawała punktu zaczepienia.

Na poszukiwania wyraźnego ciągu przyczynowo-skutkowego przepaliłem tu mnóstwo czasu, ponieważ każda zmiana warunków pracy wymagała od kilku do kilkudziesięciu minut testu, który na ogół należało powtórzyć kilka razy dla zebrania jakiejś wartościowej statystyki.

## Bisekcja kodu

Tym razem miałem duży problem z zastosowaniem bisekcji, gdyż niewiele części programu nadawało się do prostego wyłączenia — urządzenie przestawałoby wówczas działać. Wiele warstw abstrakcji musiało ze sobą współgrać, by zachować normalny tok funkcjonowania, w&nbsp;którym objawiał się błąd. Nawet, gdy w końcu udałoby się jakiś fragment kodu wyłączyć, a raczej zastąpić jakimś uproszczonym odpowiednikiem, należałoby poświęcić wiele czasu na testy.

## JTAG

Utknąłem w ten sposób na wiele dni w martwym punkcie. Nie dochodziłem do żadnych nowych wniosków. Błąd wydawał się skorelowany lekko z obciążeniem programu, ale poza tym zupełnie losowy. W tym momencie było jasne, że problem warto byłoby zaatakować od niższych warstw. Sięgnąłem po debugger, konkretnie debugger sprzętowy <abbr title="Joint Test Action Group">JTAG</abbr>. Niestety, zrywał on połączenie z mikrokontrolerem w momencie restartu. Pomogło wyłączenie trybu _real-time_, który zachowywał bieg przerwań po zatrzymaniu wątku głównego. Skoro procesor się restartował i tak nie miało sensu próbowanie utrzymania programu przy życiu. Teraz udało mi się przyłapać procesor w momencie restartu. Niestety, debugger nie był w stanie powiązać bieżącej instrukcji z żadnym kodem, a&nbsp;stos wywołań był pusty.

## Analiza ABI

Obraziwszy się na debugger za to, że nie podał mi rozwiązania na tacy, popadłem w&nbsp;apatię i smętnym wzrokiem wpatrywałem się w&nbsp;przeglądarkę pamięci i rejestrów. Wtedy po raz pierwszy od długiego czasu zrobiłem coś mądrego i sięgnąłem po dokumentację <abbr title="Application Binary Interface">ABI</abbr> kompilatora w nadziei, że któryś z rejestrów specjalnych zawiera jakąś poszlakę w postaci ustawionej flagi błędu. Przy tej okazji odkryłem, że wprawdzie debugger nie widzi już stosu wywołań, ale ABI określa, w którym z rejestrów można odnaleźć adres powrotu. Okazało się, że wskazuje on na obsługę przerwania spowodowanego błędnym adresem instrukcji. Z jakiegoś powodu procesor próbował skoczyć do nieprawidłowej instrukcji. Jak się wkrótce okazało, chodziło o niewyrównany adres w pamięci programu.

Adres ten często się powtarzał przy kolejnych reprodukcjach błędów, ale później zmieniał się, a analiza kodu assemblerowego nie wskazywała na żadną regularność w&nbsp;tychże adresach. Właściwie już w tym momencie powinno być dla mnie jasne, że przyczyną jest przepełnienie stosu, ewentualnie pisanie po nim przez program, bo co innego może powodować skok do losowej, na dodatek niewyrównanej instrukcji?

## Moduł _post-mortem_

Wystraszyłem się jednak niskopoziomowej analizy i wpadłem na głupiomądry pomysł dodania do programu analizy _post-mortem_. Mając pod ręką nieulotną pamięć <abbr title="Ferroelectric Random-Access Memory">FRAM</abbr>, stworzyłem logger, który w buforze kołowym zapisywał, do którego miejsca w pamięci dotarł program. Po restarcie mogłem odczytać kilkaset ostatnich kroków. W ten sposób znów utknąłem na wiele godzin reprodukowania błędu. Moduł _post-mortem_ napisałem dosyć szybko i działał on znakomicie, ale potwierdził on tylko początkowe obserwacje, że problem ma charakter powtarzalny… albo jednak nie…

Żeby pogrążyć się jeszcze bardziej, zacząłem znów wyłączać fragmenty kodu. Było to dosyć pracochłonne, bo trudno było utrzymać działanie urządzenia, ale ograniczyłem się głównie do przerwań. Przeczuwałem, że przyczyną błędu może być jakiś problem z&nbsp;synchronizacją między przerwaniami a pętlą główną lub wywłaszczanie przerwań, w&nbsp;szczególności wywłaszczanie przerwania przez samo siebie. Błąd rzeczywiście był związany z przerwaniem, ale miał inny charakter, a zyskiem całego zużytego czasu było tylko wykazanie, że moduł _post-mortem_ da się prosto zrobić i może być on całkiem przydatny. Hipotetycznie.

## Poznasz głupiego po czynach jego

W końcu wróciłem do dokumentacji ABI. Przeanalizowałem obsługę błędów przez system przerwań, wywoływanie funkcji, przekazywanie argumentów do nich i, _last but not least_, adresację stosów. Gdy obejrzałem w trybie _live_ pamięć, w której umieszczony był stos jednego z przerwań, wszystko stało się jasne. Dzięki temu, że na starcie stos był wypełniany wzorcem typu `0xDEADBEEF` czy innym [_hexspeakiem_](https://en.wikipedia.org/wiki/Hexspeak), jak na dłoni było widać, że dochodzi do przepełnienia. _Stack overflow_ dotyczył jednego z przerwań, gdyż urządzenie pracowało pod kontrolą <abbr title="Real-Time Operating System">RTOS</abbr>-a, który przydzielał obsługom przerwań oddzielne stosy. Przy portowaniu kodu nie zadbałem o sprawdzenie, czy rozmiary stosów są odpowiednie.

Analiza behawioralna i eksperymenty z modułem _post-mortem_ pochłonęły jakieś sześć–osiem dni roboczych i dość szybko sugerowały, że problem jest raczej stochastyczny niż deterministyczny. Analiza ABI i wykonanie za debugger pracy w odtworzeniu historii prowadzącej do resetu mikrokontrolera zajęła około dwóch dni. Poza rozwiązaniem tego problemu wzbogaciło mnie to o wiedzę i umiejętności, które pewnie pozwolą jeszcze w przyszłości zaoszczędzić czas.

Przyczyną takiego a nie innego przebiegu wydarzeń, tj. przede wszystkim traktowania procesora jak czarnej skrzynki, nie była świadoma decyzja, a lęk przed zagłębianiem się w tajniki działania <abbr title="Central Processing Unit">CPU</abbr> i kompilatora. Technika ma jednak tę przyjazną w gruncie rzeczy właściwość, że wnikliwe zapoznanie się z&nbsp;zasadą działania mechanizmu daje nam olbrzymią przewagę nad wszystkimi, którzy mogą ją tylko zgadywać za pomocą mniej lub bardziej pomysłowych eksperymentów. Oczywiście, na ogół niezbędna do tego jest dobrze napisana dokumentacja.
