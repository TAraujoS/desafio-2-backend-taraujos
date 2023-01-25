# CNAB - BACKEND

This project was developed to receive the upload of a CNAB file, with data on the financial transactions of several stores. The application handles the data and stores them in a relational database and displays this information on screen.

---

## Main Technologies:
- Python
- Django RestFramework
- SQLite

---

## How to Start:
1- Create a virtual environment from your terminal:
```
python -m venv venv
```
2- Activate the virtual environment: 
```
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```
3- Install all dependecies: 
```
pip install -r requirements.txt
```

4- Configure the .env with the values of your machine:

---

## Steps for running in a development environment:

1- Run the migrations with the command:
```
python manage.py migrate
```

2- To run the server run the command:
```
python manage.py runserver
```