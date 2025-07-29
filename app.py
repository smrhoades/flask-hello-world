from flask import Flask
import psycopg

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Sara Rhoades in 3308'

@app.route('/db_test')
def database():
    conn = psycopg.connect("postgresql://lab10_database_smrhoades_user:CqHRorcahSKsRB3DhXEuUG1uCEYesr9J@dpg-d24kca15pdvs73fo4e5g-a/lab10_database_smrhoades")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def database_create():
    conn = psycopg.connect("postgresql://lab10_database_smrhoades_user:CqHRorcahSKsRB3DhXEuUG1uCEYesr9J@dpg-d24kca15pdvs73fo4e5g-a/lab10_database_smrhoades")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Table Successfully Created"
