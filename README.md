# Projekt2
###UWAGA### \
W celu sprawdzenia funkcjonalności wtyczki zaleca się ze skorzystania z dedykowanego pliku "warstwa_test.shp" znajdującego się w katalogu "\warstwa_testowa"


1. Instalacja wtyczki:

Cały folder "Projekt2" umieścić w folderze "plugins" odpowiadającego za przechowywanie wtyczek do programu QGIS. Przykładowa lokalizacja:
"C:\Users\micha\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins"
Gdzie, "C:\Users\(nazwa użytkownika)\..."
Następnie przy pomocy wbudowanej funkcji "Zarządzanie wtyczkami" wyszukać, w katalogu wszystkie wtyczki: "Projekt2". Zaznaczyć odpowiedniego check-boxa i upewnić się, że wtyczka jest zainstalowana.

Obsługiwane systemy:
-Windows

Obsługiwane wersje Qgis'a:
-QGIS 3.28

Programy do edycji wtyczki:
-python w wersji 3.11


2. Zastosowanie wtyczki:

Wtyczka Projekt2 jest wtyczką do programu QGIS, posiada dwie podstawowe funkcjonalności:
- obliczanie różnicy wysokości pomiędzy dwoma wybranymi przez użytkownika punktami,
-obliczanie pola powierzchni pomiędzy dowolną ilość punktów wybranych przez użytkownika*

Wybrane przez użytkownika punkty wyświetlają się w formie tabeli, widoczne są wartości ich współrzędnych i wysokości podanych w METRACH
Użytkownik ma możliwość wyboru układu współrzędnych: PL-2000 i PL-1992. Dodatkowo przy obliczaniu pola powierzchni użytkownik może zmienić jednostkę wyjściową wyniku: METRY KWADRATOWE, ARY, HEKTARY. Z zaznaczonych punktów użytkownik ma również możliwość utworzenia poligonu.

3. Opis działania wtyczki:

Aby wtyczka działała poprawnie należy (wytyczne):
 
-Upewnić się, że oznaczenia zdefiniowane w programie i oznaczenia w opracowywanym pliku QGIS, są identyczne. Program został napisany dla warstwy z następującym oznaczeniem atrybutów:
 -Numer punktu, wyrażony w wartości liczbowej całkowitej, zdefiniowany jako atrybut o nazwie 'ID'
 -Współrzędna prostokątna "X" punktów wyrażona w metrach, zdefiniowana jako atrybut o nazwie 'xcoord'
 -Współrzędna prostokątna "Y" punktów wyrażona w metrach, zdefiniowana jako atrybut o nazwie 'ycoord'
 -Współrzędna prostokątna "Z" punktów wyrażona w metrach, zdefiniowana jako atrybut o nazwie 'zcoord'

-Upewnić się, że wszystkie punkty, z których użytkownik chce skorzystać, znajdują się na JEDNEJ wartswie.

-Obliczanie różnicy wysokości pomiędzy dwoma punktami (instrukcja):
Po instalacji wtyczki i załadowania odpowiedniego(według wytycznych) pliku należy:
 - Z okna oznaczonego jako "Wybór obliczeń" wybrać opcję: "Różnica wysokości".
 - Zaznaczyć DWA punkty na warstwie. Wybrane punkty wyświetlą się w oknie znajdującym się po prawej stronie, będzie widoczna (w tym przypadku) ich wysokość oraz numer.
 - Następnie należy kliknąć przycisk "Oblicz". Zostanie policzona różnica wysokości: (punkt wybrany jako pierwszy) - (punkt wybrany jako drugi) 
 - Wynik zostanie wyświetlony w metrach,w dolnej części okna wraz z informacją, które punkty zostały wykorzystane 
 - Jeśli użytkownik chce wykonać kolejne obliczenia, należy powtórzyć powyższe czynności
 - Jeśli użytkowni chce zakończyć korzystanie z wtyczki, należy kliknąć przycisk "Okej","Anuluj" albo ikonkę "x" w prawym górnym rogu
 - W przypadku wybrania nieodpowiedniej liczby punktów (tj. innej niż 2) program zwróci odpowiedni komunikat, aby dalej korzystać z programu należy postępować zgodnie z powyższą instrukcją

-Obliczanie pola powierzchni pomiędzy punktami (instrukcja):
Po instalacji wtyczki i załadowania odpowiedniego(według wytycznych) pliku należy:
 - Z okna oznaczonego jako "Wybór obliczeń" wybrać opcję: "Pole powierzchni".
 - Zaznaczyć DOWOLNĄ ilość punktów na warstwie. Wybrane punkty wyświetlą się w oknie znajdującym się po prawej stronie, będąwidoczna (w tym przypadku) ich współrzędne oraz numer.
 - Następnie należy kliknąć przycisk "Oblicz". Zostanie policzone pole powierzchni pomiędzy punktami, zgodnie ze wzorem: P = 1/2 * suma od pierwszego do ostatniego elementu z Xi(Yi+1 - Yi-1)
 - Wynik zostanie wyświetlony w jednostce wybranej przez użytkownika, domyślnie w metrach kwadratowych. Możliwe jest wyświetlenie wyniku w ARACH i HEKTARACH poprzez wybranie odpowiedniej opcji z lewej strony okna, nazwaną "Jednostki pola powierzchni"
 - Użytkownik ma również możliwość "narysować" poligon, z zaznaczonych przez siebie punktów wybierając opcję "Rysuj poligon"
 - Jeśli użytkownik chce wykonać kolejne obliczenia, należy powtórzyć powyższe czynności
 - Jeśli użytkowni chce zakończyć korzystanie z wtyczki, należy kliknąć przycisk "Okej","Anuluj" albo ikonkę "x" w prawym górnym rogu
 - W przypadku wybrania nieodpowiedniej liczby punktów (tj. mniejszej niż 3) program zwróci odpowiedni komunikat, aby dalej korzystać z programu należy postępować zgodnie z powyższą instrukcją

-Znane błędy:
 - Opcja "Rysuj poligon" nie zawsze działa poprawnie, użytkownik nie ma możliwości edycji "kształtu" poligonu.










