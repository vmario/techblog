---
title: "Lista zadań w Vimie"
date: 2022-05-11
draft: false
tags: [vim, gtd, fun]
fortune: "Tak naprawdę nikt tego nie potrzebował, ale przecież to lubimy"
motto:
  quote: "W klasie pani kazała nam wyjąć zeszyty i przepisywać z tablicy zadania do rozwiązania w domu. Bardzo mnie to zmartwiło, szczególnie jak pomyślałem o tacie, bo kiedy wraca z biura, jest zmęczony i nie ma ochoty na robienie zadań z arytmetyki."
  author: "René Goscinny"
  cite: "Mikołajek i inne chłopaki"
---

## Po co to komu?

Do zarządzania zadaniami w życiu prywatnym stosuję aplikację [TickTick](https://ticktick.com), następcę znakomitego [Wunderlist](https://en.wikipedia.org/wiki/Wunderlist), kupionego przez Microsoft w 2015 i po 5 latach zaoranego na rzecz [Microsoft To Do](https://todo.microsoft.com). TickTicka używam w wersji darmowej i, jak dotąd, ani niewielkie ograniczenia, ani brak kilku funkcji (np. kalendarza), nie przekonały mnie do inwestycji w wersję płatną. Po prostu darmowa wersja tego narzędzia pokrywa moje potrzeby.

W pracy jednak unikam tego rodzaju programów, by minimalizować [shadow IT](https://en.wikipedia.org/wiki/Shadow_IT) (skala problemu i tak jest [duża](https://niebezpiecznik.pl/post/co-robia-pracownicy-kiedy-admini-nie-patrza/)). W szczególności nie wykorzystuję narzędzi chmurowych, przez które mogłyby wyciec newralgiczne dane, a niewątpliwie do takich zaliczałaby się aplikacja do planowania zadań. Pomyślałem, że najprostszą alternatywą byłby zwykły plik tekstowy w formacie [Markdown](https://daringfireball.net/projects/markdown/), którym zarządzałbym w Vimie. Oczywiście, Vim ma pluginy do list zadań, ale stwierdziłem, że prosty plik w zupełności mi wystarczy, gdyż od bardziej skomplikowanych funkcji, jak określanie zależności między zadaniami czy przypomnienia, mam w pracy inne narzędzia, np. bugtracker i firmowy kalendarz. Ja potrzebowałem tylko zapisać kilka bieżących zadań, czasem dopisać do tego jakieś notatki.

## Plik z zadaniami

Przygotowałem zatem prosty plik z legendą i logo. Logo _ASCII art_ jest bardzo ważne. Dzięki temu, gdy ktoś będzie Wam zaglądał przez ramię, skupi się na logo, nie na treści, jest to zatem element opsecowy.

{{< figure src="screenshot_00.webp" link="screenshot_00.webp" title="Plik z zadaniami w postaci wyjściowej" >}}

## Konfiguracja Vima

Jak widać, format pliku jest oczywisty i u większości z Was lista zadań będzie już wyglądała jako-tako. Jeżeli nie używacie Neovima, będzie to oczywiście wymagało dodania do `.vimrc` co najmniej:

``` vim
set nocompatible
syntax on
```

Pójdźmy jednak krok dalej i dodajmy dodatkową konfigurację dla plików Markdown:

``` vim
function! ExtendMarkdownToDo()
endfunction
autocmd FileType markdown call ExtendMarkdownToDo()
```

W funkcji `ExtendMarkdownToDo` włączmy zawijanie wierszy na wyrazach, o ile nie mamy już tej opcji włączonej w naszej konfiguracji:

``` vim
set linebreak
```

Dodajmy zmianę statusu zadania kombinacjami <kbd>t&lt;Spacja&gt;</kbd>, <kbd>tx</kbd>, <kbd>tc</kbd> i <kbd>t-</kbd> oraz dodawanie nowego zadania przed i po bieżącym za pomocą, odpowiednio — <kbd>tO</kbd> i <kbd>to</kbd>. Dorzućmy też skoki do poprzedniego i następnego projektu za pomocą <kbd>Ctrl-k</kbd> i <kbd>Ctrl-j</kbd> oraz skoki do najważniejszych sekcji:

``` vim
nnoremap <silent> t<Space> :s/\[.\]/[ ]/<CR>
nnoremap <silent> tx :s/\[.\]/[x]/<CR>
nnoremap <silent> tc :s/\[.\]/[c]/<CR>
nnoremap <silent> t. :s/\[.\]/[.]/<CR>
nnoremap <silent> t- :s/\[.\]/[-]/<CR>
nnoremap <silent> to o<Esc>cc  - [ ] 
nnoremap <silent> tO O<Esc>cc  - [ ] 
nnoremap <silent> tT /^Today$<CR>:nohlsearch<CR>zt
nnoremap <silent> tD /^Done$<CR>:nohlsearch<CR>zt
nnoremap <silent> tB /^Backlog$<CR>:nohlsearch<CR>zt
nnoremap <silent> tS /^Scratchpad$<CR>:nohlsearch<CR>zt
nnoremap <silent> <C-j> /^*<CR>:nohlsearch<CR>
nnoremap <silent> <C-k> ?^*<CR>:nohlsearch<CR>
```

Możemy jeszcze wymyślić wiele innych skrótów, ale nie chcemy iść w stronę pisania od nowa pluginu, który można pobrać gotowy z Sieci. Zresztą ja w swojej głowie więcej klawiszologii nie zmieszczę.

Mamy już zatem składnię Markdown uzupełnioną o prosty schemat dokumentu (koniecznie z logotypem!) i kilka skrótów klawiaturowych, które ułatwią zmianę statusu zadania. Statusy każdy może zdefiniować sobie według własnego widzimisię — jest to bardzo proste.

Na koniec przydałaby się jeszcze jakaś wisienka na torcie, która wniosłaby walor bajerancko-edukacyjny do całego przedsięwzięcia. Użyjmy zatem opcji `conceal` mechanizmu kolorowania składni, umożliwiającej ukrywanie i podmienianie znaków. Dzięki temu zastąpimy prymitywne `[x]` unicodowym ptaszkiem:

``` vim
syntax match taskStatus '\[ \]' conceal cchar= 
syntax match taskStatus '\[x\]' conceal cchar=✔
syntax match taskStatus '\[c\]' conceal cchar=✘
syntax match taskStatus '\[\.\]' conceal cchar=⧖
syntax match taskStatus '\[-\]' conceal cchar=»
```

Dorzucimy kolor i włączymy mechanizm ukrywania:

``` vim
set conceallevel=2
set concealcursor=nv
highlight conceal ctermfg=cyan ctermbg=NONE guifg=cyan guibg=NONE
```

Dla opcji `conceallevel` możliwe są wartości:

<dl>
<dt>0
<dd>tekst pokazywany bez zmian (domyślnie);
<dt>1
<dd>tekst podmieniany, a gdy wartość docelowa nie została podana, przyjmowany jest znak z listchars (domyślnie spacja);
<dt>2
<dd>tekst podmieniany, a gdy wartość docelowa nie została podana — ukrywany;
<dt>3
<dd>tekst ukrywany.
</dl>

Wybrałem opcję `2`, bo wówczas dokument rozjeżdża się przy znakach, dla których zapomniałbym podać `cchar`.

Opcję `concealcursor` ustawiłem tak, by tylko przy edycji pokazywany był oryginalny tekst.

## Końcowy efekt

Efekt końcowy w zupełności mnie zadowala. Trochę kolorów i unicodowe ikonki wieńczą dzieło.

{{< figure src="screenshot_01.webp" link="screenshot_01.webp" title="Plik z zadaniami w postaci końcowej" >}}

Cała konfiguracja przedstawia się zaś następująco:

``` vim
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Lista zadań w Markdown
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

set nocompatible
syntax on

function! ExtendMarkdownToDo()
set linebreak
set conceallevel=2
set concealcursor=nv
highlight conceal ctermfg=cyan ctermbg=NONE guifg=cyan guibg=NONE
syntax match taskStatus '\[ \]' conceal cchar= 
syntax match taskStatus '\[x\]' conceal cchar=✔
syntax match taskStatus '\[c\]' conceal cchar=✘
syntax match taskStatus '\[\.\]' conceal cchar=⧖
syntax match taskStatus '\[-\]' conceal cchar=»
nnoremap <silent> t<Space> :s/\[.\]/[ ]/<CR>
nnoremap <silent> tx :s/\[.\]/[x]/<CR>
nnoremap <silent> tc :s/\[.\]/[c]/<CR>
nnoremap <silent> t. :s/\[.\]/[.]/<CR>
nnoremap <silent> t- :s/\[.\]/[-]/<CR>
nnoremap <silent> to o<Esc>cc  - [ ] 
nnoremap <silent> tO O<Esc>cc  - [ ] 
nnoremap <silent> tT /^Today$<CR>:nohlsearch<CR>zt
nnoremap <silent> tD /^Done$<CR>:nohlsearch<CR>zt
nnoremap <silent> tB /^Backlog$<CR>:nohlsearch<CR>zt
nnoremap <silent> tS /^Scratchpad$<CR>:nohlsearch<CR>zt
nnoremap <silent> <C-j> /^*<CR>:nohlsearch<CR>
nnoremap <silent> <C-k> ?^*<CR>:nohlsearch<CR>
endfunction

autocmd FileType markdown call ExtendMarkdownToDo()
```

## Podsumowanie

Mamy zatem w około trzydziestu linijkach obsłużoną listę zadań, której format jest na tyle prosty, że:

- można ją edytować w dowolnym edytorze;
- można ją śledzić w repozytorium np. Git;
- dzięki legendzie jest właściwie samodokumentująca.

Z kolei konfiguracja naszego Vima pozwala w miarę wygodnie przeglądać, dodawać i odhaczać zadania.
