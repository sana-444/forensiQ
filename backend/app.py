from flask import Flask 

from routes.incidents import incidents_bp 

from routes.ingestion import ingestion_bp 

from routes.severity import severity_bp 

from routes.reports import reports_bp 

 

app = Flask(__name__) 

 

# Register Blueprints 

app.register_blueprint(incidents_bp, url_prefix="/incidents") 

app.register_blueprint(ingestion_bp, url_prefix="/ingest") 

app.register_blueprint(severity_bp, url_prefix="/severity") 

app.register_blueprint(reports_bp, url_prefix="/reports") 

 

if __name__ == '__main__': 

    app.run(debug=True) 
