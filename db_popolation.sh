# stations
curl -i -X POST -H 'Content-Type: application/json' -d '{"stationID": 1, "name": "NOI TechPark Charging Point", "address":"Via Ignota 7","lat":45.464664,"lon": 9.18854}' 127.0.0.1:5000/insert_station
curl -i -X POST -H 'Content-Type: application/json' -d '{"stationID": 2, "name": "Piazza Walther Charging Point", "address":"Piazza Walther 1","lat":46.4983,"lon": 11.3544}' 127.0.0.1:5000/insert_station
curl -i -X POST -H 'Content-Type: application/json' -d '{"stationID": 3, "name": "Piazza Duomo Charging Point", "address":"Piazza Duomo 1","lat":45.464664,"lon": 9.18854}' 127.0.0.1:5000/insert_station
curl -i -X POST -H 'Content-Type: application/json' -d '{"stationID": 4, "name": "Piazza Castello Charging Point", "address":"Piazza Castello 1","lat":45.464664,"lon": 9.18854}' 127.0.0.1:5000/insert_station

# cars
curl -X POST -H "Content-Type: application/json" -d '{"plate": "ABC123","manifacturer": "Toyota","engine": "Hybrid"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "DEF456","manifacturer": "Tesla","engine": "Electric"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "GHI789","manifacturer": "Fiat","engine": "Gasoline"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "LMN101","manifacturer": "Toyota","engine": "Hybrid"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "OPQ112","manifacturer": "Tesla","engine": "Electric"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "RST113","manifacturer": "Fiat","engine": "Gasoline"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "UVW114","manifacturer": "Toyota","engine": "Hybrid"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "XYZ115","manifacturer": "Tesla","engine": "Electric"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "ABC116","manifacturer": "Fiat","engine": "Gasoline"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "DEF117","manifacturer": "Toyota","engine": "Hybrid"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "GHI118","manifacturer": "Tesla","engine": "Electric"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "LMN119","manifacturer": "Fiat","engine": "Gasoline"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "OPQ120","manifacturer": "Toyota","engine": "Hybrid"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "RST121","manifacturer": "Tesla","engine": "Electric"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "UVW122","manifacturer": "Fiat","engine": "Gasoline"}' http://localhost:5000/insert_car
curl -X POST -H "Content-Type: application/json" -d '{"plate": "XYZ123","manifacturer": "Toyota","engine": "Hybrid"}' http://localhost:5000/insert_car

# driver out
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "ABC123","stationID": "1"}' http://localhost:5000/driver_out
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "DEF456","stationID": "1"}' http://localhost:5000/driver_out
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "GHI789","stationID": "2"}' http://localhost:5000/driver_out
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "LMN101","stationID": "3"}' http://localhost:5000/driver_out
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "OPQ112","stationID": "4"}' http://localhost:5000/driver_out
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "RST113","stationID": "1"}' http://localhost:5000/driver_out
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "UVW114","stationID": "2"}' http://localhost:5000/driver_out

# parking abuse
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "ABC123","stationID": "1"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-01T12:00:00Z","plate": "GHI789","stationID": "2"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-02T12:00:00Z","plate": "RST113","stationID": "3"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-03T12:00:00Z","plate": "ABC116","stationID": "3"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-04T12:00:00Z","plate": "GHI118","stationID": "3"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-05T12:00:00Z","plate": "LMN119","stationID": "2"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-06T12:00:00Z","plate": "OPQ120","stationID": "4"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-07T12:00:00Z","plate": "RST121","stationID": "1"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-08T12:00:00Z","plate": "GHI118","stationID": "3"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-09T12:00:00Z","plate": "LMN119","stationID": "4"}' http://localhost:5000/abusive_parking
curl -X POST -H "Content-Type: application/json" -d '{"time_stamp": "2022-01-10T12:00:00Z","plate": "OPQ120","stationID": "2"}' http://localhost:5000/abusive_parking
