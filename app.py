from flask import Flask, render_template, request, flash, redirect, url_for
import easyocr
import os
from werkzeug.utils import secure_filename
import tempfile

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this in production

# Configuration
UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB in bytes
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize EasyOCR reader (English language)
reader = easyocr.Reader(['en'])

def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_file_size(file):
    """Check if file size is within limit"""
    file.seek(0, 2)  # Seek to end of file
    file_size = file.tell()
    file.seek(0)  # Reset file pointer
    return file_size <= MAX_FILE_SIZE

@app.route('/')
def index():
    """Main page with upload form"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and text extraction"""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))
    
    if not allowed_file(file.filename):
        flash('Invalid file type. Please upload JPG, JPEG, or PNG files only.')
        return redirect(url_for('index'))
    
    if not check_file_size(file):
        flash('File size exceeds 10MB limit.')
        return redirect(url_for('index'))
    
    try:
        # Create temporary file to save uploaded image
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            file.save(temp_file.name)
            temp_filename = temp_file.name
        
        # Extract text using EasyOCR
        results = reader.readtext(temp_filename)
        
        # Combine all detected text
        extracted_text = '\n'.join([result[1] for result in results])
        
        # Clean up temporary file
        os.unlink(temp_filename)
        
        if not extracted_text.strip():
            extracted_text = "No text detected in the image."
        
        return render_template('result.html', text=extracted_text, filename=file.filename)
    
    except Exception as e:
        flash(f'Error processing image: {str(e)}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)