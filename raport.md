<!-- Heading -->
## Star Wars Shooter (Raport)
<!-- Links -->
#### Jeremiasz Macura
[Star Wars Shooter on github](https://github.com/Jeremiaszmacura/pygame_star_wars_projekt)
### Raport
<!-- UL -->
Założeniem projektu było stworzenie gry w języku Python, która napisana jest po "wężowmu",
w sposób czytelny i jednoznaczny. Cały projekt miał być podzielony na moduły, a każdy moduł 
odpowiedzialny z konkretny element projektu. Przy pisaniu progamu posługiwaliśmy się narzędziem 
pylint, który dbał o to, by nasze projekty zostały napisane w "wężowym" stylu, łącznie z 
oznaczeniami zmiennych, funkcji, klas, testów, komentarzy, znaków białej linii i wielu innych.
Jednocześnie projekt wymagał od nas nauki githuba w podstawowym zakresie. Nasz projekt mieliśmy 
zamieścić w repozytorium i regularnie dbał o aktualizację naszego kodu, tym samym doprowadzając 
nasz kod to końcowego efektu.
<!-- UL -->
Uważam, że założenia te zostały przeze mnie spełnione, z tego względu, że brałem udział w 
konsultacjach organizowanych przez prowadzącego Pana Ciurę oraz stosowałem sie do uwag, 
które prowadzacy zamieszać na githubie, w naszych repozytoriach, w zakładce Issue.
Największym wyzwaniem podczas pisania tego kodu było utworzenie testów jak i obsługa 
tablic zawierąca obiekty klas myśliwca i pocisków. Podczas wykonywania testów zwróciłem uwagę 
na błąd w funkcji obsługującej czas rozgrywki, która przyśpieszała wrogie mysliwce. Tego błędu 
nie zauważyłbym gdyby takie testy nie zostały przeprowadzne. 
Mój projekt zawiera wymagania podane przez Pana Ciurę jak i wymagania ogólne do samej budyowy 
projektu podane przez Pana Gonciarza. 
Projekt zawiera 8 modułów, w tym jeden z nich jest testem. Zapiera opis projektu README.md, 
requirements.txt, .gitignore, podrzebne assets oraz raport.md.
#### Pliki

* repozytorium nie zawiera zbędnych katalogów (typu \_\pycache__, .idea, ...)
* dodany został plik .gitignore
* nazwy bibliotek zewnętrzych niezbędnych do działania programu zostały umieszczone w pliku requirements.txt
#### Uwagi drobiazdowe
* został zastosowany pylint,
* zostały użyte instrukcje from ... import ... 
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/81d96e95cd31bfdbf7de46ff39bbc71da7aecdee/main.py#L4
* instrukcje import w odpowiedniej kolejności: standardowe, zewnętrzne, własne moduły
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/main.py#L2
* program nie zawiera zmiennych globalnych
* stałe zostały umieszczone w module const.py, w klasie Consts
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/const.py#L4
* moduły, funkcje i zmienne są w stylu_wężowym (snake_case)
* program nie zawiera nieczytelnych skrótów
* instrukcje warunkowe napisane w sposób minimalistyczny
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/screen.py#L42
* do sklejania napisów zastosowane f-stringi
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/text.py#L52
* docstringi do modułów, klas, metod i funkcji są zawarte w projekcie
* wiersze programu nie są zbyt długie, połamane w miejscach koniecznych
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/text.py#L55
#### Rozmaite rady
* ścieżki do plików napisane przy użyciu "/"
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/const.py#L26
* atrybuty inicjalizowane w odpowiedni sposób
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/player.py#L9
* zastosowane statyczne zmienne, nie dynamiczne
* importowanie modułów nie ma skutków ubocznych typu wipisywania teksu
* wczytywanie plików dokonuję się poprzez moduł const.py i klasę Assets
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/const.py#L20
* funkcja main wywołana poprzez if__name__ == '\_\_main__':
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/main.py#L92
* moduł testu zgodnie z zaleceniami Google nazwany "nazwa_test.py"
* wykorzystany moduł unitest,
https://github.com/Jeremiaszmacura/pygame_star_wars_projekt/blob/5ae33f0e6dd92416a8999166ff48231889a5a101/screen_test.py#L3
#### Rady wyższego poziomu
* konstruktor nie wywołuje: funkcji zmieniających globalny stan programu, nie posiada
instrukcji warunkowych ani pętli, inicjalizacji atrybutów bardziej skomplikowanych niż
zwykłe przypisania, tworzenia obiektów wymagających doinicjowania innymi metodami,
dziwnych obejść, nie korzystających z \_\_init__() po to, żeby móc zwracać kod błedu,
* metody nie naruszją reguły Demeter,
* klasy nie posiadają: w nazwach spójników "i", rozłącznych zbiorach metod, które operują
 na rozłącznych zbiorach atrybutów.
