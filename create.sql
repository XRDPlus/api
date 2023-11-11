CREATE TABLE "ParkingArrival" (
	"Timestamp"	REAL NOT NULL,
	"Plate"	TEXT NOT NULL,
	"StationID" INTEGER NOT NULL,
	PRIMARY KEY("Timestamp")
);

CREATE TABLE "AbusiveParking" (
	"Timestamp"	REAL NOT NULL,
	"Plate"	TEXT NOT NULL,
	"StationID" INTEGER NOT NULL,
	PRIMARY KEY("Timestamp")
);

CREATE TABLE "DriverOut" (
	"Timestamp"	REAL NOT NULL,
	"Plate"	TEXT NOT NULL,
	"StationID" INTEGER NOT NULL,
	PRIMARY KEY("Timestamp")
);

CREATE TABLE "Profiling" (
	"Age"	INTEGER NOT NULL,
	"Ethnicity"	TEXT NOT NULL,
	"Gender"	TEXT NOT NULL,
	"Emotion"	TEXT NOT NULL,
	"Plate"	TEXT NOT NULL,
	"StationID" INTEGER NOT NULL,
	PRIMARY KEY("Plate")
);

CREATE TABLE "Cars" (
	"Plate"	TEXT NOT NULL,
	"Manifacturer"	TEXT NOT NULL,
	"Engine"	TEXT NOT NULL,
	PRIMARY KEY("Plate")
)

CREATE TABLE "Stations" (
	"StationID"	INTEGER NOT NULL,
	"Latitude"	REAL NOT NULL,
	"Longitude"	REAL NOT NULL,
	PRIMARY KEY("StationID")
)
