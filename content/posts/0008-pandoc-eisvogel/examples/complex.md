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
