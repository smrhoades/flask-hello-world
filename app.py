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
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def database_insert():
    conn = psycopg.connect("postgresql://lab10_database_smrhoades_user:CqHRorcahSKsRB3DhXEuUG1uCEYesr9J@dpg-d24kca15pdvs73fo4e5g-a/lab10_database_smrhoades")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def database_select():
    conn = psycopg.connect("postgresql://lab10_database_smrhoades_user:CqHRorcahSKsRB3DhXEuUG1uCEYesr9J@dpg-d24kca15pdvs73fo4e5g-a/lab10_database_smrhoades")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.commit()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop')
def database_drop():
    conn = psycopg.connect("postgresql://lab10_database_smrhoades_user:CqHRorcahSKsRB3DhXEuUG1uCEYesr9J@dpg-d24kca15pdvs73fo4e5g-a/lab10_database_smrhoades")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"
