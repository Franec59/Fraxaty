from flask import render_template
from werkzeug.utils import redirect
from model.infirmier import Infirmier as InfirmierRepo



class InfirmiersController():
    
    def infirmiers():
        liste_infirmiers = InfirmierRepo().fetchAll()
        return render_template("infirmiers.html", liste_infirmiers=liste_infirmiers)
    
    def infirmier(context, id:int=None):
        infirmier_data = InfirmierRepo().findById(id)
        return render_template("infirmier.html", infirmier_data=infirmier_data, context=context)

    def traitement(context, data):
        if context == "creation" :
            infirmier_id = InfirmierRepo().add(data)
            
        elif context == "update" :
            infirmier_id = InfirmierRepo().update(data)
            
        return redirect(f'/infirmier/detail/{infirmier_id}')