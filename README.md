# Elitarny Algorytm Genetyczny (EGA) dla Problemu Zbioru Plonów

Ten projekt implementuje **Elitarny Algorytm Genetyczny (EGA)** w celu rozwiązania problemu zbioru plonów, który jest zadaniem optymalizacji z ograniczeniami. Celem jest maksymalizacja wydajności zbioru przy jednoczesnym spełnieniu równania wzrostu i nałożonych ograniczeń.

## Opis Problemu

Problem zbioru plonów polega na maksymalizacji funkcji celu:

\[
J = \sum_{k=0}^{N-1} \sqrt{u_k}
\]

przy następujących ograniczeniach:

- **Równanie wzrostu:**

  \[
  x_{k+1} = a \cdot x_k - u_k
  \]

  gdzie:

  - \( a \) to stały współczynnik wzrostu (np. \( a = 1.1 \))
  - \( x_0 \) to stan początkowy (np. \( x_0 = 100 \))
  - \( u_k \) to zmienna sterująca reprezentująca ilość zbioru w okresie \( k \)

- **Ograniczenia sterowania:**

  \[
  u_k \geq 0
  \]

  dla każdego \( k \), co zapewnia nieujemne wartości zbioru.

- **Ograniczenie równości:**

  \[
  x_0 = x_N
  \]

  co oznacza, że stan na początku i końcu okresu jest taki sam.

## Elitarny Algorytm Genetyczny (EGA)

EGA jest zastosowany do rozwiązania tego problemu poprzez modelowanie procesu ewolucyjnego, który optymalizuje funkcję celu z zachowaniem ograniczeń.

### Implementacja Algorytmu

#### Populacja Osobników

- **Reprezentacja osobników:**

  Każdy osobnik jest wektorem rzeczywistych liczb:

  \[
  u = [u_0, u_1, ..., u_{N-1}]
  \]

  gdzie \( u_k \) to ilość zbioru w okresie \( k \).

- **Rozmiar populacji:**

  100 osobników.

- **Inicjalizacja populacji:**

  Wartości \( u_k \) są inicjalizowane losowo z zakresu \([0, a \cdot x_0]\), przy zapewnieniu spełnienia ograniczeń problemu.

#### Funkcja Celu

- **Cel:**

  Maksymalizacja funkcji celu:

  \[
  J = \sum_{k=0}^{N-1} \sqrt{u_k}
  \]

- **Ograniczenia:**

  - **Równanie wzrostu:** \( x_{k+1} = a \cdot x_k - u_k \)
  - **Ograniczenie równości:** \( x_0 = x_N \)
  - **Nieujemność:** \( u_k \geq 0 \) oraz \( x_k \geq 0 \)

#### Selekcja

- **Metoda selekcji:**

  **Selekcja turniejowa**

- **Opis:**

  Losowo wybierane są grupy osobników (np. po 5), a z każdej grupy wybierany jest osobnik z najwyższą wartością funkcji celu do puli rodziców.

#### Operatory Genetyczne

- **Krzyżowanie:**

  - **Typ:** Krzyżowanie arytmetyczne
  - **Mechanizm:**

    Potomkowie są tworzeni jako kombinacja liniowa genów rodziców:

    \[
    \text{Potomek} = \alpha \cdot \text{Rodzic}_1 + (1 - \alpha) \cdot \text{Rodzic}_2
    \]

    gdzie \( \alpha \) jest losową liczbą z zakresu \([0,1]\).

- **Mutacja:**

  - **Typ:** Mutacja gaussowska
  - **Mechanizm:**

    Do genów potomków dodawany jest szum gaussowski o średniej 0 i odchyleniu standardowym \( \sigma \), zapewniając zachowanie ograniczeń.

#### Subpopulacja

- **Elitarność:**

  Najlepsze 5% osobników jest bezpośrednio przenoszone do następnej generacji bez zmian.

#### Podstawienie

- **Metoda:**

  **Reprodukcja częściowa** - połączenie elity z nowo wygenerowanym potomstwem tworzy nową populację.

## Struktura Projektu

Projekt składa się z następujących plików:

- **`main.py`**: Główny plik uruchamiający algorytm EGA z klasy.
- **`algorytm.py`**: Plik z klasą algorytmu EGA.
- **`fitness.py`**: Zawiera implementację funkcji celu oraz sprawdzanie ograniczeń.
- **`selection.py`**: Implementuje selekcję turniejową.
- **`crossover.py`**: Zawiera funkcje krzyżowania arytmetycznego.
- **`mutation.py`**: Odpowiada za mutację gaussowską.
- **`constraints.py`**: Zapewnia spełnienie ograniczeń przez osobniki.
- **`Visualization.py`**: Odpowiada za wizualizację wyników algorytmu.
- **`utils.py`**: Zawiera funkcje pomocnicze, np. inicjalizację populacji.

## Użyte Biblioteki

- **NumPy**: Do operacji numerycznych i manipulacji tablicami.
- **Matplotlib**: Do wizualizacji wyników.

## Uruchomienie

Instrukcje dotyczące uruchamiania projektu zostaną dodane w przyszłości.

---

*Uwaga:* Szczegółowe implementacje funkcji w poszczególnych modułach powinny zostać uzupełnione zgodnie z powyższymi opisami.
