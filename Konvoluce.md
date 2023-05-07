# Definice
![[Konvoluace a korelace.PNG]]
$$
A=
\begin{vmatrix}
a & b & c \\\
d & e & f \\\
g & h & i
\end{vmatrix}
$$

$$
B=
\begin{vmatrix}
u & v & w \\\
x & y & z \\\
s & t & r
\end{vmatrix}
$$

## Konvoluce
1. Vytvoríme matici B_transp, která je transponovanou maticí B.

$$
B_{transp}=
\begin{vmatrix}
u & x & s \\\
v & y & t \\\
w & z & r
\end{vmatrix}
$$

2. Rozšířit matici A o nulové okraje tak, aby bylo možné provést konvoluci. Nazvěme tuto matici A_ext.

$$
A_{ext}=
\begin{vmatrix}
0 & 0 & 0 & 0 & 0 \\\
0 & a & b & c & 0 \\\
0 & d & e & f & 0 \\\
0 & g & h & i & 0 \\\
0 & 0 & 0 & 0 & 0
\end{vmatrix}
$$

3. Provést konvoluci matic A_ext a B_transp. Výsledkem bude matice C.
    Násobit prvky matic B_transp a A_ext, kde se B_transp překrývá s A_ext, a poté provést sumaci.

    **První pozice (horní levý roh A_ext):**

    $$
    \begin{vmatrix}
    0 & 0 & 0 \\\
    0 & a & b \\\
    0 & d & e
    \end{vmatrix}
    *
    \begin{vmatrix}
    u & x & s \\\
    v & y & t \\\
    w & z & r
    \end{vmatrix}
    $$

    $$
    \begin{vmatrix}
    0*u & 0*x & 0*s \\\
    0*v & a*y & b*t \\\
    0*w & d*z & e*r
    \end{vmatrix}
    $$

    Suma: $a*y+b*t+d*z+e*r$

    **Posunout B_transp o jedno místo doprava a opakovat:**

    $$
    \begin{vmatrix}
    0 & 0 & 0 \\\
    a & b & c \\\
    d & e & f
    \end{vmatrix}
    *
    \begin{vmatrix}
    u & x & s \\\
    v & y & t \\\
    w & z & r
    \end{vmatrix}
    $$

    $$
    \begin{vmatrix}
    0*u & 0*x & 0*s \\\
    a*v & b*y & c*t \\\
    d*w & e*z & f*r
    \end{vmatrix}
    $$

    Suma: $a*v+b*y+c*t+d*w+e*z+f*r$

    Opakovat tento postup pro zbylé pozice.


## Korelace

1. Stejně jako v případě konvoluce, rozšířit matici A o nulové okraje tak, aby bylo možné provést korelaci. Nazvěme tuto matici A_ext.

2. Násobit prvky matic B a A_ext, kde se B překrývá s A_ext, a poté provést sumaci.

    **První pozice (horní levý roh A_ext):**

    $$
    \begin{vmatrix}
    0 & 0 & 0 \\\
    0 & a & b \\\
    0 & d & e
    \end{vmatrix}
    *
    \begin{vmatrix}
    u & v & w \\\
    x & y & z \\\
    s & t & r
    \end{vmatrix}
    $$

    $$
    \begin{vmatrix}
    0*u & 0*v & 0*w \\\
    0*x & a*y & b*z \\\
    0*s & d*t & e*r
    \end{vmatrix}
    $$

    Suma: $a*y+b*z+d*t+e*r$

    **Posunout B o jedno místo doprava a opakovat:**

    $$
    \begin{vmatrix}
    0 & 0 & 0 \\\
    a & b & c \\\
    d & e & f
    \end{vmatrix}
    *
    \begin{vmatrix}
    u & v & w \\\
    x & y & z \\\
    s & t & r
    \end{vmatrix}
    $$

    $$
    \begin{vmatrix}
    0*u & 0*v & 0*w \\\
    a*x & b*y & c*z \\\
    d*s & e*t & f*r
    \end{vmatrix}
    $$

    Suma: $a*x+b*y+c*z+d*s+e*t+f*r$

    Opakovat tento postup pro zbylé pozice.

## Zdroje
Návod na průchod algoritmem konvoluce:
https://www.youtube.com/watch?v=8rrHTtUzyZA
https://www.youtube.com/watch?v=7KcN_9V5ZjU
https://www.youtube.com/watch?v=8rrHTtUzyZA
https://portal.matematickabiologie.cz/index.php?pg=analyza-a-modelovani-dynamickych-biologickych-dat--signaly-a-linearni-systemy--casove-rady-i--3-zakladni-operace-s-matematickymi-modely-velicin-diskretnich-v-case--3-2-diskretni-konvoluce