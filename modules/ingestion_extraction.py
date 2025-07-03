import os 

 

UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'uploads') 

os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

 

def save_uploaded_file(file): 

    if not file or file.filename == '': 

        return None, "Invalid file" 

 

    path = os.path.join(UPLOAD_FOLDER, file.filename) 

    file.save(path) 

    return path, None 
