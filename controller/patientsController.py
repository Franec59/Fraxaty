from flask import render_template
from werkzeug.utils import redirect
from model.patient import Patient as PatientRepo
from model.infirmier import Infirmier as InfirmierRepo



class PatientsController():
    
    def patients():
        liste_patients = PatientRepo().fetchAll()
        return render_template("patients.html", liste_patients=liste_patients)
    
    def patient(context, id:int=None):
        infirmier_data = InfirmierRepo().fetchAll()
        patient_data = PatientRepo().findById(id)
        return render_template("patient.html", patient_data=patient_data, liste_infirmiers=infirmier_data, context=context)

    def traitement(context, data, id=None):
        if context == "creation" :
            patient_id = PatientRepo().add(data)
            
        if context == "update" :
            patient_id = PatientRepo().update(data)
            
        if context == "delete" :
            print("Here")
            PatientRepo().delete(data)
            return redirect(f'/patients')
            
        return redirect(f'/patient/detail/{patient_id}')