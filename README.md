# BienStar

## VIRTUAL VENV
# create a virtual venv: python -m ven env 
# activate env: env\Scripts\activate

## Install requirementes.txt
pip install -r requirements.txt

## MIGRATIONS
python manage.py makemigrations
python manage.py migrate


## RUN PROYECT
python manage.py runserver


## API - ADMINISTRADOR
http://127.0.0.1:8000/api_administrator/

sigin user_admin
http://127.0.0.1:8000/api_administrator/sigin/

login user_admin
http://127.0.0.1:8000/api_administrator/login/

logout user_admin
http://127.0.0.1:8000/api_administrator/logout/

administration task - create_user
http://127.0.0.1:8000/api_administrator/createuser/
