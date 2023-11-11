from flask import Flask, request, jsonify
from flask_cors import CORS
from markupsafe import escape
import sqlite3

app = Flask(__name__)

CORS(app)

DATABASE = './database.db'

ELETTRICA = {
    'targa': "EL123AB",
    'engine': "elettrica"
}

BENZINA = {
    'targa': "BE123AB",
    'engine': "benzina"
}

AUTO = [
    ELETTRICA,
    BENZINA
]

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

@app.route('/valid/<targa>')
def is_valid(targa):
    valid = False
    for auto in AUTO :
        if auto["targa"] == targa and auto["engine"] == "elettrica":
            valid = True
    return jsonify(isEV=valid)

def insert_targa(targa):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Customer (Targa) VALUES (?)', (targa, ))
    conn.commit()
    conn.close()

@app.route('/insert_car', methods=['POST'])
def insert_car():
    data = request.get_json()

    # Check if 'targa' is present in the data
    if 'targa' not in data:
        return jsonify({'error': 'Missing "targa" parameter'}), 400

       # Extract 'targa' from the JSON data
    targa = data['targa']

    # Insert data into the database
    insert_targa(targa)

    return jsonify({'message': 'Data inserted successfully'})

# curl -X POST -H "Content-Type: application/json" -d '{"targa": "TARGA123"}' http://127.0.0.1:5000/insert_car

def targa_in_db(targa) :
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM (Customer) WHERE (Targa) = ?', (targa,))
    count = cursor.fetchone()[0]

    conn.close()

    return count > 0

@app.route('/car_in_db/<targa>')
def car_in_db(targa):
    return jsonify(present=targa_in_db(targa))

def get_all_cars_from_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Fetch all rows from the "Customer" table
    cursor.execute('SELECT (Targa) FROM (Customer)')
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    return rows

@app.route('/all_cars')
def all_cars():
    return jsonify(get_all_cars_from_db())

if __name__ == '__main__':
    app.run(debug=True)
