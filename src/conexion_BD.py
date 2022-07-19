import psycopg2 
#pip install venv
#pip install flask
#pip install psycopg2
#env\Scripts\activate
#python env\app.py
try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='WEcameasromance' ,
        database='PI'

    
    )
    print("conexion ye")
except Exception as ex:
    print(ex)

