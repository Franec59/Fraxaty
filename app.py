from flask import Flask
from flask.templating import render_template, request
from werkzeug.utils import redirect
from controller.infirmiersController import InfirmiersController
from model.infirmier import Infimier


infirmier = Infimier()
infirmiersController = InfirmiersController()

app = Flask(__name__)


@app.route("/infirmiers")
def infirmiers():
    return render_template("infirmiers.html")

@app.route("/infirmiers")
def affichage():
    return infirmiersController.fetchInfirmiers(infirmier)

@app.route('/deleteInfirmier/<int:id>')
def deleteInfirmier(id_infirmier):
    return infirmiersController.delete(infirmier, id_infirmier)

@app.route('/addInfirmier')
def addInfirmier():
    return infirmiersController.add()

@app.route('/traitementInfirmier', methods=['POST','GET'])
def traitementInfirmier():
    data = request.form
    return infirmiersController.traitementInfirmier(infirmier, data)

@app.route('/updateInfirmier')
def updateInfirmier():
    data = request.args
    return infirmiersController.update(data)
    
@app.route('/traitementUpdateInfirmier', methods=['POST','GET'])
def traitementUpdateInfirmier():
    data = request.form
    return infirmiersController.traitementUpdateInfirmier(infirmier, data)





# app.run()