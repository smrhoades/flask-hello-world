from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --your name-- in 3308'

@app.route('/db_test')
def database():
    conn = psycopg2.connect("postgresql://lab10_database_smrhoades_user:CqHRorcahSKsRB3DhXEuUG1uCEYesr9J@dpg-d24kca15pdvs73fo4e5g-a/lab10_database_smrhoades")
    conn.close()
    return "Database Connection Successful"
