from flask import Flask, request, jsonify
from flask_cors import CORS
from markupsafe import escape
import sqlite3

app = Flask(__name__)
CORS(app)
DATABASE = './database.db'

def is_electric(targa) :
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT (Engine) FROM (Cars) WHERE (Plate) == ?', (targa, ))
    rows = cursor.fetchone()

    if rows[0] == 'electric' :
        return True
    else :
        return False

@app.route('/valid/<targa>')
def is_valid(targa):
    
    return jsonify(isEV = is_electric(targa)), 200


def insert_car_in_db(targa, produttore, motore):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Cars (Plate, Manifacturer, Engine) VALUES (?, ?, ?)', (targa, produttore, motore, ))
    conn.commit()
    conn.close()

@app.route('/insert_car', methods=['POST'])
def insert_car():
    data = request.get_json()

    # Check if 'targa' is present in the data
    if 'targa' not in data:
        return jsonify({'error': 'Missing "targa" parameter'}), 400
    if 'produttore' not in data:
        return jsonify({'error': 'Missing "produttore" parameter'}), 400
    if 'motore' not in data:
        return jsonify({'error': 'Missing "motore" parameter'}), 400
    
       # Extract 'targa' from the JSON data
    targa, produttore, motore = data['targa'], data['produttore'], data['motore']

    # Insert data into the database
    insert_car_in_db(targa, produttore, motore)

    return jsonify({'message': 'Data inserted successfully'}), 200

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

    cursor.execute('SELECT * FROM (Cars)')
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    return rows

@app.route('/all_cars')
def all_cars():
    return jsonify(get_all_cars_from_db())

if __name__ == '__main__':
    app.run(debug=True)
