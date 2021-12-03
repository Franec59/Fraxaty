from flask import Flask, render_template, request, abort
from controller.infirmiersController import *


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
    return InfirmiersController.traitement(context, data, id=None)



