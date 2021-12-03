from model.db import DB
from model.adresse import Adresse


class Infirmier(DB):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def fetchAll(self):
        cursor=self.getCursor()
        cursor.execute("SELECT * FROM infirmier")
        rows=cursor.fetchall()
        cursor.close()
        return rows

    def add(self, infirmier_data):
        infirmier_data = infirmier_data.to_dict()
        adresse=Adresse()
        adresse_idadresse=adresse.add(infirmier_data)
        infirmier_data["adresse_idadresse"]=adresse_idadresse
        cursor=self.getCursor()
        sql=("""
                INSERT INTO
                infirmier(
                    adresse_idadresse,
                    numero_pro,
                    nom,
                    prenom,
                    tel_pro,
                    tel_perso
                )
                VALUES (
                    "{adresse_idadresse}",
                    "{numero_pro}",
                    "{nom}",
                    "{prenom}",
                    "{tel_pro}",
                    "{tel_perso}"
                );
        """).format(**infirmier_data)
        cursor.execute(sql)
        cursor.close()
        return cursor.lastrowid
   
    
    def update(self, infirmier_data, id_infirmier):
        infirmier_data = infirmier_data.to_dict()
        adresse=Adresse()
        adresse_idadresse=adresse.add(infirmier_data)
        infirmier_data["adresse_idadresse"]=adresse_idadresse
        infirmier_data["idinfirmier"]=id_infirmier
        cursor=self.getCursor()
        sql2=("""
                UPDATE 
                infirmier
                SET
                    adresse_idadresse = "{adresse_idadresse}",
                    numero_pro = "{numero_pro}",
                    nom = "{nom}",
                    prenom = "{prenom}",
                    tel_pro = "{tel_pro}",
                    tel_perso = "{tel_perso}"
                
                WHERE 
                    idinfirmier="{idinfirmier}"
                    
                ;
        """).format(**infirmier_data)
        print(sql2)
        cursor.execute(sql2)
        cursor.close()
        return cursor.lastrowid
    

    def delete(self, id_infirmier):
        cursor=self.getCursor()
        sql3=(f"""
                DELETE FROM infirmier WHERE idinfirmier = "{id_infirmier}"
        """)
        cursor.execute(sql3)
        cursor.close()
    
    def findById(self, id_infirmier):
        cursor=self.getCursor()
        sql4=(f"""
                SELECT
                    idinfirmier,
                    nom,
                    prenom,
                    numero_pro,
                    tel_pro,
                    tel_perso,
                    numero,
                    rue,
                    cp,
                    ville
                FROM
                    infirmier
                JOIN 
                    adresse ON infirmier.adresse_idadresse=adresse.idadresse
                WHERE infirmier.idinfirmier="{id_infirmier}"
                ;
        """)
        cursor.execute(sql4)
        result=cursor.fetchone()
        cursor.close()
        return result