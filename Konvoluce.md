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
1. Převrátit matici B vzhledem k ose X a Y (180 stupňů rotace). Nazvěme tuto matici B_rot.
$$
B_{rot}=
\begin{vmatrix}
r & t & s \\\
z & y & x \\\
w & v & u
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

3. Provést konvoluci matic A_ext a B_rot. Výsledkem bude matice C.
    Násobit prvky matic B_rot a A_ext, kde se B_rot překrývá s A_ext, a poté provést sumaci.

    **První pozice (horní levý roh A_ext):**

    $$
    \begin{vmatrix}
    0 & 0 & 0 \\\
    0 & a & b \\\
    0 & d & e
    \end{vmatrix}
    *
    \begin{vmatrix}
    r & t & s \\\
    z & y & x \\\
    w & v & u
    \end{vmatrix}
    $$

    $$
    \begin{vmatrix}
    r*0 & t*0 & s*0 \\\
    z*0 & y*a & x*b \\\
    w*0 & v*d & u*e
    \end{vmatrix}
    $$

    Suma: $a*y+b*x+d*v+e*u$

    **Posunout B_rot o jedno místo doprava a opakovat:**

    $$
    \begin{vmatrix}
    0 & 0 & 0 \\\
    a & b & c \\\
    d & e & f
    \end{vmatrix}
    *
    \begin{vmatrix}
    r & t & s \\\
    z & y & x \\\
    w & v & u
    \end{vmatrix}
    $$

    $$
    \begin{vmatrix}
    r*0 & t*0 & s*0 \\\
    z*a & y*b & x*c \\\
    w*d & v*e & u*f
    \end{vmatrix}
    $$

    Suma: $a*z+b*y+c*x+d*w+e*v+f*u$

    Opakovat tento postup pro zbylé pozice.


## Korelace
V lineární algebře odpovídá skalárním součinům.

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