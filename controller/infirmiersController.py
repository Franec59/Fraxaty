from flask import render_template
from werkzeug.utils import redirect

class InfirmiersController():
    
    def fetchInfirmiers(self, infirmier):
        result = infirmier.fetchAll()
        return render_template("infirmiers.html", data= result)
    
    def delete(self,infirmier, id_infirmier):
        infirmier.delete(id_infirmier)
        return redirect("/infirmiers")
    
    def add(self):
        return render_template("creation_infirmier.html")
    
    def traitementInfirmier(self, infirmier, data):
        infirmier.add(data)
        return redirect("/infirmiers")
    
    def update(self, data):
        return render_template("/update_infirmier.html", data = data)
    
    def traitementUpdateInfirmier(self,infirmier, data):
        infirmier.update(data)
        return redirect('/infirmiers')