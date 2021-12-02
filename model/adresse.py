from db import  DB

class Adresse(DB):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add(self, adresse_data):
        cursor=self.getCursor()
        sql= ("""
                SELECT idadresse
                FROM adresse
                WHERE
                    numero = "{numero}" AND
                    rue = "{rue}" AND
                    cp = "{cp}" AND
                    ville = "{ville}"
                    ;
            """.format(**adresse_data)
        )
        cursor.execute(sql)
        resultat=cursor.fetchone()

        if resultat is None:
            sql2= ("""
                    INSERT INTO
                    adresse(
                        numero,
                        rue,
                        cp,
                        ville
                    )
                    VALUES (
                        "{numero}",
                        "{rue}",
                        "{cp}",
                        "{ville}"
                    );
            """).format(**adresse_data)
            cursor.execute(sql2)
            cursor.close()
            return cursor.lastrowid

        else:
            return resultat.get('idadresse')