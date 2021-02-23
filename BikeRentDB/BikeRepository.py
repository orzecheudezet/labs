

class BikeRepository:
    def __init__(self, cursor):
        self.cursor = cursor


    def save(self, bike):
        self.cursor.execute("INSERT INTO Bikes (Color, Size, Brand) VALUES('"+bike.color+"', '"+str(bike.size)+"', '"+bike.brand+"')")




# ćwiczenia stożków rotatorów, 4 flex Faceless trójboista z Polski

