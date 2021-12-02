from flask import render_template
from werkzeug.utils import redirect

class InfirmiersController():
    
    def fetchInfirmiers(self, continent):
        result = continent.fetchAll()
        return render_template("infirmiers.html", data= result)