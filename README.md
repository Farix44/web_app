Na czas developmentu serwer uruchamiany będzie na localhoscie 127.0.0.1:8000


INSTALACJA:

sprawdzić czy python3 jest zainstalwoany

python3 -V

jak nie to zainstalowac (miminum wersja 3.6, najlepiej najnowsza)

sudo apt-get install python3-pip

sudo apt-get install python3-venv



PRZYGOTOWANIE SRODOWISKA I SERWERA (LINUX):

Sciagamy repo z githuna (zip)

rozpakowywujemy

otieramy konsole i przechodzimy do rozpakowanego pliku (do katalogu web_app-main)

python3 -m venv venv

source venv/bin/activate

pip install django

python3 manage.py runserver

ctrl + c

python3 manage.py migrate

python3 manage.py runserver

pip install django-bootstrap-form


Utworzenie uytkownika admina (tylko login i haslo, mail zostawic pusty)

python3 manage.py createsuperuser


STRONY:

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/kredyty/lista/


Pierwsza strona przechodzi do logowania do panelu admina gdzie można przegladac/dodawać/edytowac/usowac wnioski kredytowe. 

Druga strona to zwykly html wyswietlajacy liste wszystkich wnioskow.
