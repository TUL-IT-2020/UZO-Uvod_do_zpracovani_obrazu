# Lineární algebra:
$$
A=
\begin{vmatrix}
a & b & c \\\
d & e & f \\\
g & h & i
\end{vmatrix}
B=
\begin{vmatrix}
u & v & w \\\
x & y & z \\\
s & t & r
\end{vmatrix}
$$
## Konvoluce
1. Vytvoríme matici B_rot, která je transponovanou maticí B.
$$
B_{rot}=
\begin{vmatrix}
r & t & s \\\
z & y & x \\\
w & v & u
\end{vmatrix}
$$
2. Rozšířit matici A o nulové okraje tak, aby bylo možné provést konvoluci. Nazvěme tuto matici A_ext.
3. Násobit prvky matic B_rot a A_ext, kde se B_rot překrývá s A_ext, a poté provést sumaci.
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
0*r & 0*t & 0*s \\\
0*z & a*y & b*x \\\
0*w & d*v & e*u
\end{vmatrix}
$$

Suma: $a*y+b*x+d*v+e*u$

Posunout B_rot o jedno místo doprava a opakovat.

## Korelace
Násobit prvky matic B a A_ext, kde se B překrývá s A_ext, a poté provést sumaci.

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

Posunout B o jedno místo doprava a opakovat.
# Hranový detektor
## Robertsův operátor:
-   Jednoduchý, rychlý
-   2D konvoluce, 2 masky (2x2):
	$$
	Gx=
	\begin{vmatrix}
	1 & 0 \\\
	0 & -1  
	\end{vmatrix}
	Gy=
	\begin{vmatrix}
	0 & 1 \\\
	0 & -1  
	\end{vmatrix}
    $$
-   Výsledek: R = √(Gx² + Gy²)

## Laplace:
-   2.  derivace obrazu
-   2D konvoluce, maska (3x3):
    $$
    \begin{vmatrix}
    -1 & -1 & -1 \\\
    -1 & +8 & -1 \\\
    -1 & -1 & -1
    \end{vmatrix}
    $$

## Sobel & Prewitt:
-   2D konvoluce, 2 masky (3x3)
-   Sobel:
    $$
    Gx=
    \begin{vmatrix}
    -1 & 0 & +1 \\\
    -2 & 0 & +2 \\\
    -1 & 0 & +1
    \end{vmatrix}
    Gy=
    \begin{vmatrix}
    +1 & +2 & +1 \\\
    0 & 0 & 0 \\\
    -1 & -2 & -1
    \end{vmatrix}
    $$
-   Prewitt:
    $$
    Gx=
    \begin{vmatrix}
    -1 & 0 & +1 \\\
    -1 & 0 & +1 \\\
    -1 & 0 & +1
    \end{vmatrix}
    Gy=
    \begin{vmatrix}
    +1 & +1 & +1 \\\
    0 & 0 & 0 \\\
    -1 & -1 & -1
    \end{vmatrix}
    $$
-   Výsledek: R = √(Gx² + Gy²)

## Robinsonův operátor:
-   Aproximace první derivace
-   2D konvoluce, 8 masek (3x3): R0, R1, ..., R7
-   Výsledek: R = max(|R0|, |R1|, ..., |R7|)

## Kirschův operátor:
-   Aproximace první derivace
-   2D konvoluce, 8 masek (3x3): K0, K1, ..., K7
-   Výsledek: R = max(|K0|, |K1|, ..., |K7|)

# Barvení objektu:
## První průchod:
-   Procházet obraz po řádcích
-   Pro nenulový element f(i, j):
    -   Zkontrolovat sousedy podle masky (již obarvené)
    -   Přiřadit hodnotu (barvu) dle následujících pravidel:
        -   Všechny sousedy jsou pozadí (0): Přiřadit novou barvu
        -   Právě jeden soused má nenulovou hodnotu: Přiřadit hodnotu tohoto souseda
        -   Více sousedů s nenulovými hodnotami:
            -   Přiřadit hodnotu kteréhokoli nenulového souseda
            -   Pokud sousední elementy mají různé hodnoty (kolize barev), zaznamenat ekvivalentní dvojice do tabulky ekvivalence
Příklady:
$$
8_{sousedů}:
\begin{vmatrix}
    1 & 1 & 1 \\\
    1 & X & 1 \\\
    1 & 1 & 1
\end{vmatrix}
4_{sousedů}:
\begin{vmatrix}
    0 & 1 & 0 \\\
    1 & X & 1 \\\
    0 & 1 & 0
\end{vmatrix}
$$

# Vzdálenosti: 
## Šachovnicová vzdálenost
-   Dvourozměrný prostor (mřížka)
-   Pohyb po diagonále, vertikálně, horizontálně
-   Vypočítává se jako max(|x1-x2|, |y1-y2|)
-   Příklad: bod A(3,5) a B(8,1) => šachovnicová vzdálenost = max(|3-8|, |5-1|) = max(5, 4) = 5
## Euklidovská vzdálenost
-   Nejkratší vzdálenost mezi 2 body
-   Vypočítává se jako √((x1-x2)² + (y1-y2)²)
-   Příklad: bod A(3,5) a B(8,1) 
	=> euklidovská vzdálenost = √((3-8)² + (5-1)²) = √(25 + 16) = √41 ≈ 6.4
## Manhattan dist.
-   Dvourozměrný prostor (mřížka)
-   Pohyb pouze vertikálně a horizontálně
-   Vypočítává se jako |x1-x2| + |y1-y2|
-   Příklad: bod A(3,5) a B(8,1) => manhattanská vzdálenost = |3-8| + |5-1| = 5 + 4 = 9

# Morfologické operace na jednoduché množině:
## Otevření
-   Kombinace eroze a dilatace
-   Postup:
    1.  Eroze: Zmenšení objektu odstraněním okrajových bodů
    2.  Dilatace: Zvětšení objektu přidáním bodů na okraj
-   Vlastnosti:
    -   Odstraňuje drobné objekty
    -   Hladí kontury objektů
    -   Udržuje vzdálenost mezi objekty
## Uzavření
-   Kombinace dilatace a eroze
-   Postup:
    1.  Dilatace: Zvětšení objektu přidáním bodů na okraj
    2.  Eroze: Zmenšení objektu odstraněním okrajových bodů
-   Vlastnosti:
    -   Vyplňuje drobné díry v objektech
    -   Hladí kontury objektů
    -   Udržuje vzdálenost mezi objekty
## Dilatace:
-   Zvětšení objektů přidáním bodů na okraj
-   Postup:
    1.  Procházet obraz po řádcích
    2.  Pro nenulový element f(i, j):
        -   Přidat body ze strukturního elementu do objektu

## Eroze:
-   Zmenšení objektů odstraněním okrajových bodů
-   Postup:
    1.  Procházet obraz po řádcích
    2.  Pro nenulový element f(i, j):
        -   Odstranit body, které neodpovídají strukturnímu elementu