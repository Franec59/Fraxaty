from db import DB
from adresse import Adresse

class Patient(DB):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def fetchAll(self):
        cursor=self.getCursor()
        sql=("""
                SELECT
                    nom,
                    infirmier_idinfirmier,
                    prenom,
                    naissance,
                    sexe,
                    securite_sociale,
                    numero,
                    rue,
                    cp,
                    ville
                FROM
                    patient
                JOIN 
                    adresse ON patient.adresse_idadresse=adresse.idadresse
            """)
        
        cursor.execute(sql)
        rows=cursor.fetchall()
        cursor.close()
        return rows

    def add(self, data):
        adresse=Adresse()
        adresse_idadresse=adresse.add(data)
        data["adresse_idadresse"]=adresse_idadresse
        cursor=self.getCursor()
        sql = ( """
                    INSERT INTO
                    patient (
                        adresse_idadresse,
                        infirmier_idinfirmier,
                        nom,
                        prenom,
                        naissance,
                        sexe,
                        securite_sociale
                    )
                    VALUES (
                        "{adresse_idadresse}",
                        "{infirmier_idinfirmier}",
                        "{nom}",
                        "{prenom}",
                        "{naissance}",
                        "{sexe}",
                        "{securite_sociale}"
                    );
                """).format(**data)
        cursor.execute(sql)
        cursor.close()
    
    def update(self, data, id_patient):
        adresse=Adresse()
        adresse_idadresse=adresse.add(data)
        data["adresse_idadresse"]=adresse_idadresse
        data["id"]= id_patient
        cursor=self.getCursor()
        sql=("""
                UPDATE 
                patient
                SET
                    adresse_idadresse = "{adresse_idadresse}",
                    infirmier_idinfirmier = "{infirmier_idinfirmier}",
                    nom = "{nom}",
                    prenom = "{prenom}",
                    naissance = "{naissance}",
                    sexe = "{sexe}",
                    securite_sociale  = "{securite_sociale}"
                
                WHERE 
                    idpatient = "{id}"
                    
                ;
        """).format(**data)
        cursor.execute(sql)
        cursor.close()

    def delete(self, id_patient):
        cursor=self.getCursor()
        sql=(f"""
                DELETE FROM patient WHERE idpatient = "{id_patient}"
        """)
        cursor.execute(sql)
        cursor.close()
    
    def findById(self, id_patient):
        cursor=self.getCursor()            
        sql=(f"""
                SELECT
                    nom,
                    infirmier_idinfirmier,
                    prenom,
                    naissance,
                    sexe,
                    securite_sociale,
                    numero,
                    rue,
                    cp,
                    ville
                FROM
                    patient
                JOIN 
                    adresse ON patient.adresse_idadresse=adresse.idadresse
                WHERE patient.idpatient="{id_patient}"
                ;
        """)
        cursor.execute(sql)
        result=cursor.fetchone()
        cursor.close()
        return result
    