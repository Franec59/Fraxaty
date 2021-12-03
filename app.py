from flask import Flask, render_template, request
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


@app.route("/infirmier/detail/<int:id>", methods=['POST', 'GET'])
def detailInfirmier(id):
    return InfirmiersController.infirmier( "detail", id)


@app.route("/infirmier/update/<int:id>", methods=['POST', 'GET'])
def updateInfirmier(id):
    return InfirmiersController.infirmier("update", id)


@app.route("/infirmier/traitement/<context>", methods=['POST', 'GET'])
def traitementInfirmier(context):
    data = request.form
    return InfirmiersController.traitement(context, data)



