import datetime
import json
import os
from jinja2 import Environment, FileSystemLoader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# In-memory audit log
audit_logs = []

# Log an event
def log_event(event_type, description, user="system"):
    audit_logs.append({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": event_type,
        "description": description,
        "user": user
    })

# Get all logs
def get_logs():
    return audit_logs

# Save to JSON
def save_logs(filepath="upload/audit_logs.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(audit_logs, f, indent=4)

# Generate PDF
def generate_pdf(output_path="upload/audit_report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Digital Forensics Audit Report")
    y = 720
    for log in audit_logs:
        line = f"{log['timestamp']} | {log['event_type']} | {log['description']} | {log['user']}"
        c.drawString(40, y, line)
        y -= 20
        if y < 50:
            c.showPage()
            y = 750
    c.save()

