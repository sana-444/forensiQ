def classify_severity(incident_type, artifact_count): 

    incident_type = incident_type.lower() 

 

    if incident_type == "malware infection" and artifact_count > 50: 

        return "Critical" 

    elif incident_type == "unauthorized access" and artifact_count > 20: 

        return "High" 

    elif incident_type == "data exfiltration" and artifact_count > 10: 

        return "High" 

    elif artifact_count > 5: 

        return "Medium" 

    else: 

        return "Low" 
