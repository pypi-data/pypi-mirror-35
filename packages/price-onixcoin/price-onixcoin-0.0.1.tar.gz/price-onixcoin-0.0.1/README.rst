# Onix prices buy.

Es una aplicación django python que calcular el precio de venta y compra de onix en bolivares y dolares. La aplicación esta dirigida
para el país de venzuela, sin emnbargo puede ser adaptada para otros paises.

Librerias.
_________

django==2.1

python3.6

Inicio rápido
______________

1. Agrega la aplicación al INSTALL_APPS de tú proyecto django::
    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Ejecutas `python manage.py makemigrations price_onixcoin`

3. Ejecutas `python maanage.py migrate`


Instalar la aplicación
______________________

pip install django-price-onixcoin

Posteriormente podrá crear unos crontad que ejecuete los siguientes comandos dentro de tu proyecto django

python3 manage.py price_btc_localbitcoin (cada 20 min)

python3 manage.py yobit_onix (cada 1 min)

python3 manage.py price_onix (cada 1 min)

