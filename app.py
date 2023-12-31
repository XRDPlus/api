from flask import Flask, request, jsonify
from flask_cors import CORS
from markupsafe import escape
import sqlite3

app = Flask(__name__)
CORS(app)
DATABASE = './database.db'

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Get is the vehicle is electric

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


# User profiling

def insert_profiling_in_db(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Profiling (Timestamp,Age, Ethnicity, Gender, Emotion, Plate, People, StationID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (data['time_stamp'], data['age'], data['ethnicity'], data['gender'], data['emotion'], data['plate'], data['people'], data['stationID'], )
    )
    conn.commit()
    conn.close()

# Insert user profiling

@app.route('/user_profiling', methods=['POST'])
def user_profiling():
    data = request.get_json()

    if 'time_stamp' not in data:
        return jsonify({'error': 'Missing "time_stamp" parameter'}), 400
    if 'age' not in data:
        return jsonify({'error': 'Missing "age" parameter'}), 400
    if 'ethnicity' not in data:
        return jsonify({'error': 'Missing "ethnicity" parameter'}), 400
    if 'gender' not in data:
        return jsonify({'error': 'Missing "gender" parameter'}), 400
    if 'emotion' not in data:
        return jsonify({'error': 'Missing "emotion" parameter'}), 400
    if 'plate' not in data:
        return jsonify({'error': 'Missing "plate" parameter'}), 400
    if 'people' not in data:
        return jsonify({'error': 'Missing "people" parameter'}), 400
    if 'stationID' not in data:
        return jsonify({'error': 'Missing "stationID" parameter'}), 400

    # Insert data into the database
    insert_profiling_in_db(data)

    return jsonify({'message': 'Data inserted successfully'}), 200

# Get the profiling of the user

def get_profiling_from_db(plate):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM (Profiling) WHERE (Plate) = ?',
        (plate,)
    )
    rows = cursor.fetchall()

    conn.close()

    return rows

@app.route('/profiling/<plate>')
def profiling_by_plate(plate):
    return jsonify(get_profiling_from_db(plate))

# Get if the customer is angry or not

@app.route('/angry', methods=['POST'])
def is_angry():
    data = request.get_json()

    if 'sentiment' not in data:
        return jsonify({'angry': 'Missing "sentiment" parameter'}), 400
    elif data['sentiment'] == "angry" :
        return jsonify(help_needed=True), 200
    else :
        return jsonify(help_needed=False), 200

### Timing of parking

# Insert the time of the parking
def insert_parking_arrival_in_db(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO ParkingArrival (Timestamp, Plate, StationID) VALUES (?, ?, ?)',
        (data['time_stamp'], data['plate'], data['stationID'], )
    )
    conn.commit()
    conn.close()

@app.route('/parking_arrival', methods=['POST'])
def parking_arrival():
    data = request.get_json()

    if 'time_stamp' not in data:
        return jsonify({'error': 'Missing "time_stamp" parameter'}), 400
    if 'plate' not in data:
        return jsonify({'error': 'Missing "plate" parameter'}), 400
    if 'stationID' not in data:
        return jsonify({'error': 'Missing "stationID" parameter'}), 400

    # Insert data into the database
    insert_parking_arrival_in_db(data)

    return jsonify({'message': 'Data inserted successfully'}), 200

def get_parking_arrival_from_db(plate):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM (ParkingArrival) WHERE (Plate) = ?',
        (plate,)
    )
    rows = cursor.fetchall()

    conn.close()

    return rows

@app.route('/parking_arrival/<plate>')
def parking_arrival_by_plate(plate):
    return jsonify(get_parking_arrival_from_db(plate))

# Insert the time of the abusive parking
def insert_abusive_parking_in_db(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO AbusiveParking (Timestamp, Plate, StationID) VALUES (?, ?, ?)',
        (data['time_stamp'], data['plate'], data['stationID'], )
    )
    conn.commit()
    conn.close()

@app.route('/abusive_parking', methods=['POST'])
def abusive_parking():
    data = request.get_json()

    if 'time_stamp' not in data:
        return jsonify({'error': 'Missing "time_stamp" parameter'}), 400
    if 'plate' not in data:
        return jsonify({'error': 'Missing "plate" parameter'}), 400
    if 'stationID' not in data:
        return jsonify({'error': 'Missing "stationID" parameter'}), 400

    # Insert data into the database
    insert_abusive_parking_in_db(data)

    return jsonify({'message': 'Data inserted successfully'}), 200

def get_abusive_parking_from_db(plate):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM (AbusiveParking) WHERE (Plate) = ?',
        (plate,)
    )
    rows = cursor.fetchall()

    conn.close()

    return rows

@app.route('/abusive_parking/<plate>')
def abusive_parking_by_plate(plate):
    return jsonify(get_abusive_parking_from_db(plate))


# Time when the driver gets out of the car
def insert_driver_out_in_db(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO DriverOut (Timestamp, Plate, StationID) VALUES (?, ?, ?)',
        (data['time_stamp'], data['plate'], data['stationID'], )
    )
    conn.commit()
    conn.close()

@app.route('/driver_out', methods=['POST'])
def driver_out():
    data = request.get_json()

    if 'time_stamp' not in data:
        return jsonify({'error': 'Missing "time_stamp" parameter'}), 400
    if 'plate' not in data:
        return jsonify({'error': 'Missing "plate" parameter'}), 400
    if 'stationID' not in data:
        return jsonify({'error': 'Missing "stationID" parameter'}), 400

    # Insert data into the database
    insert_driver_out_in_db(data)

    return jsonify({'message': 'Data inserted successfully'}), 200

def get_driver_out_from_db(plate):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM (DriverOut) WHERE (Plate) = ?',
        (plate,)
    )
    rows = cursor.fetchall()

    conn.close()

    return rows

@app.route('/driver_out/<plate>')
def driver_out_by_plate(plate):
    return jsonify(get_driver_out_from_db(plate))

### Cars management

def insert_car_in_db(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Cars (Plate, Manifacturer, Engine) VALUES (?, ?, ?)',
        (data['plate'], data['manifacturer'], data['engine'], )
    )
    conn.commit()
    conn.close()

@app.route('/insert_car', methods=['POST'])
def insert_car():
    data = request.get_json()

    if 'plate' not in data:
        return jsonify({'error': 'Missing "plate" parameter'}), 400
    if 'manifacturer' not in data:
        return jsonify({'error': 'Missing "manifacturer" parameter'}), 400
    if 'engine' not in data:
        return jsonify({'error': 'Missing "engine" parameter'}), 400
    
    # Insert data into the database
    insert_car_in_db(data)

    return jsonify({'message': 'Data inserted successfully'}), 200

# Check if the car is in the database

def plate_in_db(plate) :
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT COUNT(*) FROM (Customer) WHERE (Targa) = ?',
        (plate,)
    )
    count = cursor.fetchone()[0]

    conn.close()

    return count > 0

@app.route('/car_in_db/<plate>')
def car_in_db(plate):
    return jsonify(present=plate_in_db(plate))

def get_all_cars_from_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM (Cars)')
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    return rows

# Get all the cars from the database

@app.route('/all_cars')
def all_cars():
    return jsonify(get_all_cars_from_db())

### Station management

def insert_station_in_db(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Stations (StationID, Name, Address, Latitude, Longitude) VALUES (?, ?, ?, ?, ?)',
        (data['stationID'], data['name'], data['address'], data['lat'], data['lon'] )
    )
    conn.commit()
    conn.close()

@app.route('/insert_station', methods=['POST'])
def insert_station():
    data = request.get_json()

    if 'stationID' not in data:
        return jsonify({'error': 'Missing "stationID" parameter'}), 400
    if 'name' not in data:
        return jsonify({'error': 'Missing "name" parameter'}), 400
    if 'address' not in data:
        return jsonify({'error': 'Missing "address" parameter'}), 400
    if 'lat' not in data:
        return jsonify({'error': 'Missing "lat" parameter'}), 400
    if 'lon' not in data:
        return jsonify({'error': 'Missing "lon" parameter'}), 400
    
    # Insert data into the database
    insert_station_in_db(data)

    return jsonify({'message': 'Data inserted successfully'}), 200

def get_all_stations_from_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM (Stations)')
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    return rows

@app.route('/all_stations')
def all_stations():
    return jsonify(get_all_stations_from_db())

def get_station_from_db(stationID):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM (Stations) WHERE (StationID) = ?',
        (stationID,)
    )
    rows = cursor.fetchall()

    conn.close()

    return rows

@app.route('/station/<stationID>')
def station_by_id(stationID):
    return jsonify(get_station_from_db(stationID))

if __name__ == '__main__':
    app.run(debug=True)
