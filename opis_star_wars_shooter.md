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
* Wciśnięcie klawiszy: strzałka w prawo, strzałka w lewo, strzałka w górę, strzałka w dół, powodują odpowiednio: przesunięcie obiektu gracza w prawo (zwiększa wartości atrybutu position_x), przesunięcie obiektu gracz w lewo (zmniejszenie wartości atrybutu position_x), przesunięcie obiektu gracza w górę (zmniejszenie wartości atrybutu position_y), przesunięcie obiektu gracza w dół (zwiększenie wartości atrybutu position_y).
* Wciśnięcie klawisza spacji powoduje wygenerowanie pocisku w miejscu obiektu gracza i nadanie mu prędkości w osi y.
* Przy menu początkowym wciśnięcie klawisza 1 spowoduje wybranie łatwiejszego poziomu trudności. Wygenerowana zostanie odpowiednia liczba wrogich statków na ekranie i nadana  im zostanie początkowa prędkość z pierwszego zakresu. W przypadku wciśnięcia klawisza 2 analogicznie zostanie wygenerowana większa liczba wrogich myśliwców niż w przypadku pierwszym oraz zostanie im nadana prędkość początkowa z drugiego zakresu.
* W momencie kolizji pomiędzy pociskiem wystrzelonym przez gracza, a wrogim statkiem następuje zwiększenie ilości zdobytych punktów o jeden, dane obiekty: myśliwiec i pocisk, są usuwane z tablicy obiektów. Powoduje to, że nie są one już więcej rysowane na ekranie, a zniszczony myśliwiec udostępnia miejsce w tablicy myśliwcu kolejnemu, który zostaje wygenerowany w odpowiedni sposób na ekranie.
* W momencie przekroczenia linii obrony (górne ograniczenie osi y, dół ekranu) przez wrogi statek liczba punktów życia zmniejsza się o jeden, a myśliwiec jest usuwany z tablicy myśliwców.
* Gdy liczba punktów będzie mniejsza bądź równa zero, pojawi się komunikat o przegranej rozgrywce, informujący użytkownika o liczbie zdobytych punktów.
* Podczas wyświetlania się ekranu informującego o końcu rozgrywki, wciśnięcie klawisza enter spowoduje przekierowanie do ekranu startowego i możliwości ponownego przeprowadzenia rozgrywki. W przypadku wciśnięcia klawisz esc nastąpi zakończenie programu.