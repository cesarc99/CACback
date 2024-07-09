from app.database import get_db

class User:
    def __init__(self, Id=None, NomApe=None, Direccion=None, Contacto=None):
        self.Id = Id
        self.NomApe = NomApe
        self.Direccion = Direccion
        self.Contacto = Contacto

    @staticmethod
    def __get_users_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    
        users = []
        for row in rows:
            users.append(
                User(
                    Id=row[0],
                    NomApe=row[1],
                    Direccion=row[2],
                    Contacto=row[3]
                )
            )
        cursor.close()
        return users

    @staticmethod
    def get_users():
        return User.__get_users_by_query(
            """ 
                SELECT * 
                FROM Users 
                ORDER BY Id
            """
            )
    
    @staticmethod
    def get_user_by_id(Id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Users WHERE id = %s", (Id, ))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return User(
                Id=row[0],
                NomApe=row[1],
                Direccion=row[2],
                Contacto=row[3]
            )
        return None

    def add(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            """
                INSERT INTO Users
                (Id, NomApe, Direccion, Contacto)
                VALUES (%s, %s, %s, %s)
            """,
            (self.Id, self.NomApe, self.Direccion, self.Contacto))
        db.commit()
        cursor.close()

    def upd(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            """
                UPDATE Users
                SET NomApe = %s, Direccion = %s, Contacto = %s
                WHERE Id = %s
            """,
            (self.NomApe, self.Direccion, self.Contacto, self.Id))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            """
                DELETE from Users
                WHERE Id = %s
            """,
            (self.Id))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'Id': self.Id,
            'NomApe': self.NomApe,
            'Direccion': self.Direccion,
            'Contacto': self.Contacto
        }
    
    def toStringArray(self):
        return "[ " + self.Id + ", " + self.NomApe + ", " + self.Direccion + ", " + self.Contacto + " ]" 


    