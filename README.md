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

docker-compose:

docker-compose -f devops/docker/docker-compose.yaml stop
docker system prune -a -f

terraform
export DO_PAT=<TOKEN>
terraform plan -var "digitalocean_token=${DO_PAT}" -var-file django_sample.tfvar

-- FRONTEND
docker exec -it docker_django-kredyty-html_1 /bin/sh

curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://django-web-app:8000/api/api-token-auth/ > file
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://localhost:8000/api/api-token-auth/

-- BACKEND
apt-get update && apt-get install curl vim
docker-compose -f devops/docker/docker-compose.yaml up -d
docker exec -it docker_django-web-app_1 /bin/sh
docker-compose -f devops/docker/docker-compose.yaml stop
docker system prune -a -f

cd /usr/src/app
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py makemigrations
python manage.py runserver


KOMENDY DO DOCKERA:
docker login
docker build --tag farix44/django_web_app:latest .
docker push farix44/django_web_app

docker build --tag farix44/django_kredyty_html:latest .
docker push farix44/django_kredyty_html
