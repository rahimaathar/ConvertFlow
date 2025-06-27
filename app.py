"""
ConvertFlow - Professional File Converter Platform

SECURITY WARNING: This application is for file format conversion only.
DO NOT UPLOAD CONFIDENTIAL, SENSITIVE, OR PRIVATE FILES.
Only upload test files or publicly available content.

For production use, implement additional security measures and data encryption.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
import os
import shutil
from file_converter import file_conversion_map, get_output_formats, convert_file, get_supported_categories, get_supported_formats

app = Flask(__name__)
app.secret_key = 'secret-key'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['APP_NAME'] = 'ConvertFlow'

# Security configuration
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB limit
app.config['SECURITY_WARNING'] = 'Do not upload confidential files'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename

def detect_file_category(filename):
    extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    for category, formats in file_conversion_map.items():
        if extension in formats:
            return category, extension
    return None, extension

@app.route('/', methods=['GET', 'POST'])
def index():
    uploaded_file = None
    detected_category = None
    detected_format = None
    output_formats = []
    conversion_result = None
    converted_file = None
    
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                uploaded_file = filename
                detected_category, detected_format = detect_file_category(filename)
                if detected_category:
                    output_formats = get_output_formats(detected_format, detected_category)
                    flash(f'File uploaded successfully! Detected: {detected_format.upper()} ({detected_category})', 'success')
                else:
                    flash(f'File uploaded but format {detected_format.upper()} is not supported for conversion.', 'warning')
            else:
                flash('Please select a valid file.', 'danger')
        elif 'convert' in request.form:
            uploaded_file = request.form.get('uploaded_file')
            output_format = request.form.get('output_format')
            if uploaded_file and output_format:
                input_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file)
                output_filename = uploaded_file.rsplit('.', 1)[0] + '.' + output_format
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                
                success = convert_file(input_path, output_format)
                if success:
                    conversion_result = 'Success'
                    converted_file = output_filename
                    flash(f'File converted successfully!', 'success')
                else:
                    conversion_result = 'Failed'
                    flash('Conversion failed.', 'danger')
            else:
                flash('Please select an output format.', 'danger')
    
    return render_template('index.html',
        uploaded_file=uploaded_file,
        detected_category=detected_category,
        detected_format=detected_format,
        output_formats=output_formats,
        conversion_result=conversion_result,
        converted_file=converted_file
    )

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)
    except FileNotFoundError:
        flash('File not found.', 'danger')
        return redirect(url_for('index'))

app.jinja_env.globals.update(get_supported_formats=get_supported_formats)

if __name__ == '__main__':
    app.run(debug=True, port=5001) 