<!-- Heading -->
## Star Wars Shooter
<!-- Links -->
#### Jeremiasz Macura
[Star Wars Shooter on github](https://github.com/Jeremiaszmacura/pygame_star_wars_projekt)
### Opis
<!-- UL -->
* Ekran początkowy zawiera napis przedstawiający tytuł gry oraz prosi o wybór poziomu trudności.
* W zależności od wyboru poziomu trudności zostaje na ekranie wygenerowana odpowiednia ilość wrogich statków kosmicznych (myśliwców imperium), które również w zależności od poziomu trudności posiadają różne początkowe prędkości w osi x oraz osi y.
* Wrogie myśliwce generowane są w losowych pozycjach na osi x oraz ustalonej pozycji na osi y, przy dolnym ograniczeniu osi y, tak aby dawały efekt nadlatywania od góry ekranu w stronę naszego okrętu (którym jest Sokół Millennium), który to generowany jest w połowie osi x i przy górnym ograniczeniu osi y (na dole ekranu rozgrywki).
* Celem gry jest osiągnięcie jak najwyższego wyniku punktowego (punkt = eliminacja wrogiego statku) przy czym wraz z czasem trwania rozgrywki, wrogie myśliwce zaczynają przyspieszać, co utrudnia nam ich zestrzelenie, jak i również zwiększa się liczba generowanych wrogich statków.
* Warunkiem przegranej jest utrata punktów życia. Liczba punktów życia jest nadawana graczowi w sposób adekwatny do wybranego przezeń poziomu trudności. Utrata takiego punktu jest wywołana na skutek przekroczenia naszej linii obrony (górnego ograniczenia osi y - dół ekranu) przez myśliwca.
* Sterowanie statkiem gracza odbywa się za pomocą odpowiednich przycisków na klawiaturze, które umożliwiają poruszanie się we wszystkich kierunkach oraz strzelanie pociskami we wrogie okręty (arrow keys, space bar key).
* Po utracie wszystkich punktów życia główna pętla gry zostaje zatrzymana i pojawia się na ekranie zapytanie o rozpoczęcie nowej rozgrywki lub zakończenie działania programu.
### Testy
<!-- UL-->
##### Test Modułu screen:
* spadek punktów życia do wartości 0 lub mniejszej powoduje przerwanie głównej pętli rozgrywki, przypisanie wartości false do zmiennej running,
* generowane obiekty talblicy tie_fighters są instancjami klasy Tie_fighter,
* mysliwce przeciwnika wraz z upływem każdych kolejneych dziesięciu sekund przyśpieszają o jedną jednoskę,
* funckja obliczająca okresy dziesięciu sekund działa w sposób poprawny i po upływie dziesięciu sekund dodaje taką wartość do zmiennej czasu w funkcji main.
