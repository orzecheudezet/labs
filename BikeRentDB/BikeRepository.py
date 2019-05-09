

class BikeRepository:
    def __init__(self, cursor):
        self.Cursor = cursor


    def save(self, bike):
        self.Cursor.execute("INSERT INTO Bikes (Color, Size, Brand) VALUES('"+bike.Color+"', '"+bike.Size+"', '"+bike.Brand+"')")




# ćwiczenia stożków rotatorów, 4 flex Faceless trójboista z Polski

