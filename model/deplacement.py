#class deplacement

from db import DB


class Deplacement(DB):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def fetchAll(self):
        cursor=self.getCursor()
        cursor.execute("""SELECT 
                        iddeplacement, 
                        patient_idpatient,
                        patient.nom,
                        patient,prenom
                        date, 
                        cout 
                        FROM deplacement
                        INNER JOIN 
                        patient ON patient.idpatient=deplacement.patient_idpatient
                        
                        """)
        rows=cursor.fetchall()
        cursor.close()
        return rows

    def add(self, deplacement_data):
        cursor=self.getCursor()
        sql=("""
                INSERT INTO
                deplacement(
                    patient_idpatient,
                    date,
                    cout
                )
                VALUES (
                    "{patient_idpatient}",
                    "{date}",
                    "{cout}",
                );
        """).format(**deplacement_data)
        cursor.execute(sql)
        cursor.close()
        return cursor.lastrowid
    
    def update(self, deplacement_data, iddeplacement):
        deplacement_data["id"]=iddeplacement
        cursor=self.getCursor()
        sql2=("""
                UPDATE 
                deplacement
                SET
                    patient_idpatient = "{patient_idpatient}",
                    date = "{date}",
                    cout = "{cout}",
                WHERE 
                    {id}=iddeplacement
                    
                ;
        """).format(**deplacement_data)
        cursor.execute(sql2)
        cursor.close()

    def delete(self, iddeplacement):
        cursor=self.getCursor()
        sql3=(f"""
                DELETE FROM deplacement WHERE iddeplacement = "{iddeplacement}"
        """)
        cursor.execute(sql3)
        cursor.close()
    
    def findById(self, iddeplacement):
        cursor=self.getCursor()
        sql4=(f"""
                SELECT
                    iddeplacement,
                    patient_idpatient,
                    patient.nom,
                    patient.prenom,
                    date,
                    cout,
                FROM
                    deplacement
                JOIN 
                    patient ON patient.idpatient=deplacement.patient_idpatient
                WHERE deplacement.iddeplacement="{iddeplacement}"
                ;
        """)
        cursor.execute(sql4)
        result=cursor.fetchone()
        cursor.close()
        return result


depla = Deplacement(password="Onetipi4821!", port="3306", database="medical")
data = {}
data["patient_idpatient"] ="1"
data["date"] = "2021-12-02"
data["cout"] = "300€"

depla.add(data)
print(depla)
