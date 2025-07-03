from flask import Blueprint, request, jsonify 

import uuid 

from datetime import datetime 

 

incidents_bp = Blueprint('incidents', __name__) 

INCIDENTS_DB = []  # Replace with MongoDB in production 

 

@incidents_bp.route('/new', methods=['POST']) 

def create_incident(): 

    data = request.get_json() 

    incident = { 

        "id": str(uuid.uuid4()), 

        "title": data.get("title"), 

        "type": data.get("type"),  # Malware, Unauthorized Access, Data Exfiltration 

        "reported_by": data.get("reported_by"), 

        "date_detected": data.get("date_detected", str(datetime.now())), 

        "status": "Open", 

        "assigned_to": data.get("assigned_to"), 

        "severity": None, 

        "artifacts": [], 

        "evidence_path": None 

    } 

    INCIDENTS_DB.append(incident) 

    return jsonify({"message": "Incident created", "id": incident["id"]}), 201 

 

@incidents_bp.route('/', methods=['GET']) 

def list_incidents(): 

    return jsonify(INCIDENTS_DB) 
