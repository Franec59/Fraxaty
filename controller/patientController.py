from flask import render_template
from werkzeug.utils import redirect


class PatientController():
    def fetch_patient(self, patient):
        result=patient.fetchAll()
        return render_template("patient.html", data=result)
    
    def add_patient(self):
        return render_template("creation_patient.html")
    
    def delete_patient(self, patient, id_patient):
        patient.delete(id_patient)
        return redirect("/patient.html")

    def update_patient(self):
        return render_template("patient_update.html")