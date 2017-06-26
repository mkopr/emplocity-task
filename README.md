Task for emplocity
===================

[pdf file](https://www.vaniercollege.qc.ca/tlc/tipsheets/reading-and-analyzing/how-to-analyze-a-poem.pdf)

Requirements:
-------------
- [Flask](https://http://flask.pocoo.org/)
- [Flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/)
- [Flask-admin](https://flask-admin.readthedocs.io)
- [pdfminer](https://github.com/euske/pdfminer/)

Technologies:
-------------
- Python 2.7
- SQLite for database
- [Skeleton](http://getskeleton.com/) for CSS

Installation:
-------------
```
git clone https://github.com/mkopr/emplocity-task.git (or manually download)
cd emplocity-task
pip install -e .
emplocity_server
```

For virtualenv:
```
git clone https://github.com/mkopr/emplocity-task.git (or manually download)
cd emplocity-task
mkvirtualenv -a <emplocity-task dir> -p python2.7 emplocity-task
pip install -e .
emplocity_server
```

Content of the task:
--------------------
```
Prosta aplikację we flasku wykorzystującą:

- flask
- flask-sqlalchemy
- flask-admin
- sqlite jako bazę danych
- pdfminer jako biblioteka narzędziowa.

Chciałbym żebyś zrobił prostą, jednostronnicową aplikację (tj. 1 url wystarczy), 
która będzie wyświetlała output z pdfminera w kolumnach. 
Sposób prezentacji zostawiam Tobie - jedną kolumna na pewno powinna być treść 
(połączenie liter i/lub wierszy w jeden obszar) - drugim np. pozycja na stronie 
(jeżeli takie info jest dostępne) lub obiekt nadrzędny wobec danego obiektu 
(pdfminer zwraca obiekty w postaci drzew - tak przynajmniej to rozumiem).
Posłużyć się możesz dowolnym pdf'em (ale pewnie najlepiej znajdź jakiś prosty, 
z tekstem i jednostronnicowy)
```
