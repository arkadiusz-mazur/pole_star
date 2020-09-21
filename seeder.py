import csv, sqlite3, os

class Importer:
    
    def __init__(self):
        self.con = sqlite3.connect("db.sqlite3")
        self.cursor = self.con.cursor()

    def __del__(self):
        self.con.close()

    def create_ships(self) -> bool:
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS positions_ship (id INTEGER PRIMARY KEY ASC, imo INTEGER, name);")
            self.con.commit()
        except sqlite3.Error as e:
            print(repr(e))

        try:
            self.cursor.execute("SELECT COUNT(id) FROM positions_ship;")
            self.con.commit()
        except sqlite3.Error as e:
            print(repr(e))
        counter = self.cursor.fetchone()[0]
        if counter >= 3:
            print("Table positions_ship is already filled.")
            return False

        try:
            self.cursor.execute("INSERT INTO positions_ship (imo, name) VALUES \
                        (9632179, 'Mathilde Maersk'), \
                        (9247455, 'Australian Spirit'), \
                        (9595321, 'MSC Preziosa') \
                        ;")
        except sqlite3.Error as e:
            print(repr(e))
        self.con.commit()
        return True


    def create_positions(self) -> bool:
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS positions_position (id INTEGER PRIMARY KEY ASC, \
                imo INTEGER, \
                signal_time DATETIME, \
                lat FLOAT, \
                lon FLOAT, \
                CONSTRAINT fk_ship_imo \
                FOREIGN KEY (imo) \
                REFERENCES ship (imo) \
                ON DELETE CASCADE \
                ON UPDATE NO ACTION );")
        except sqlite3.Error as e:
            print(repr(e))

        try:
            self.cursor.execute("SELECT COUNT(id) FROM positions_position;")
            self.con.commit()
        except sqlite3.Error as e:
            print(repr(e))
        counter = self.cursor.fetchone()[0]
        if counter >= 3:
            print("Table positions_position is already filled.")
            return False

        try:
            with open('positions.csv','r') as csv_row:
                dr = csv.DictReader(csv_row)
                for i in dr:
                    row = list(i.values())
                    self.cursor.execute("INSERT INTO positions_position (imo, signal_time, lat, lon) VALUES (?, ?, ?, ?);", row)
                self.con.commit()
        except sqlite3.Error as e:
            print(repr(e))

        return True

importer = Importer()
importer.create_ships()
importer.create_positions()

# run = "python manage.py runserver 0.0.0.0:8000"
# os.system(run)