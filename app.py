from flask import Flask, render_template, request, abort
from controller.infirmiersController import InfirmiersController
from controller.patientsController import PatientsController


app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template('dashboard.html')


@app.route("/infirmiers", methods=['POST', 'GET'])
def infirmiers():
    return InfirmiersController.infirmiers()

@app.route("/infirmier/creation", methods=['POST', 'GET'])
def creationInfirmier():
    return InfirmiersController.infirmier("creation")

@app.route("/infirmier/<context>/<int:id>", methods=['POST', 'GET'])
def actionInfirmier(context, id):
    if context in ["detail", "update", "delete"] :
        if context == "delete" :
            return InfirmiersController.traitement(context, id)
        
        return InfirmiersController.infirmier(context, id)
    else:
        abort(404)
        
@app.route("/infirmier/traitement/<context>", methods=['POST', 'GET'])
def traitementInfirmier(context, id=None):
    data = request.form
    return InfirmiersController.traitement(context, data)





@app.route("/patients", methods=['POST', 'GET'])
def patientsRoute():
    return PatientsController.patients()


@app.route("/patients", methods=['POST', 'GET'])
def patients():
    return PatientsController.patients()

@app.route("/patient/creation", methods=['POST', 'GET'])
def creationPatient():
    return PatientsController.patient("creation")

@app.route("/patient/<context>/<int:id>", methods=['POST', 'GET'])
def actionPatient(context, id):
    if context in ["detail", "update", "delete"] :
        if context == "delete" :
            return PatientsController.traitement(context, id)
        
        return PatientsController.patient(context, id)
    else:
        abort(404)
        
@app.route("/patient/traitement/<context>", methods=['POST', 'GET'])
def traitementPatient(context, id=None):
    data = request.form
    return PatientsController.traitement(context, data)